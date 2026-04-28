import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
import random
from errors import TrezRuntimeError


class Datadoz:
    """
    Clase base para datasets en TREZ.
    Subclasificar e implementar len_doz() y get_doz(idx).
    """
    def len_doz(self):
        raise NotImplementedError("Datadoz: implementar len_doz().")

    def get_doz(self, idx):
        raise NotImplementedError("Datadoz: implementar get_doz(idx).")


class ListDatadoz(Datadoz):
    """Dataset a partir de listas Python: X (features) e Y (labels)."""
    def __init__(self, X, Y):
        if len(X) != len(Y):
            raise TrezRuntimeError("Datadoz: X e Y deben tener el mismo número de muestras.")
        self.X = X
        self.Y = Y

    def len_doz(self):
        return len(self.X)

    def get_doz(self, idx):
        return self.X[idx], self.Y[idx]


class Loaderdoz:
    """
    Itera un Datadoz en batches con shuffle opcional.
    Retorna batches como listas de listas (batch_x, batch_y).
    """
    def __init__(self, dataset, batch_size=1, shuffle=False):
        if not isinstance(dataset, Datadoz):
            raise TrezRuntimeError("Loaderdoz: dataset debe ser instancia de Datadoz.")
        self.dataset = dataset
        self.batch_size = batch_size
        self.shuffle = shuffle
        self._indices = list(range(dataset.len_doz()))

    def batches(self):
        """Retorna lista de (batch_x, batch_y). Cada uno es lista de listas."""
        indices = self._indices[:]
        if self.shuffle:
            random.shuffle(indices)
        result = []
        for start in range(0, len(indices), self.batch_size):
            chunk = indices[start:start + self.batch_size]
            batch_x, batch_y = [], []
            for idx in chunk:
                x, y = self.dataset.get_doz(idx)
                batch_x.append(x if isinstance(x, list) else [x])
                batch_y.append(y if isinstance(y, list) else [y])
            result.append((batch_x, batch_y))
        return result

    def num_batches(self):
        n = self.dataset.len_doz()
        return (n + self.batch_size - 1) // self.batch_size


# ------------------------------------------------------------------
# API funcional expuesta al visitor de TREZ
# ------------------------------------------------------------------

def from_lists(X, Y):
    """Crea un ListDatadoz a partir de dos listas."""
    return ListDatadoz(X, Y)


def make_loader(dataset, batch_size=1, shuffle=False):
    """Crea un Loaderdoz para un dataset."""
    return Loaderdoz(dataset, batch_size, shuffle)


def get_batches(loader):
    """Retorna todos los batches del loader como lista de pares [batch_x, batch_y]."""
    return [[bx, by] for bx, by in loader.batches()]


def train_test_split(X, Y, test_ratio=0.2):
    """
    Divide X e Y en train/test aleatoriamente.
    Retorna [X_train, Y_train, X_test, Y_test].
    """
    if len(X) != len(Y):
        raise TrezRuntimeError("Datadoz.train_test_split: X e Y deben tener el mismo largo.")
    indices = list(range(len(X)))
    random.shuffle(indices)
    split = int(len(indices) * (1 - test_ratio))
    train_idx, test_idx = indices[:split], indices[split:]
    X_train = [X[i] for i in train_idx]
    Y_train = [Y[i] for i in train_idx]
    X_test  = [X[i] for i in test_idx]
    Y_test  = [Y[i] for i in test_idx]
    return [X_train, Y_train, X_test, Y_test]
