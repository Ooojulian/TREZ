from errors import TrezRuntimeError

def mse(y_true, y_pred):
    """Calcula el Error Cuadrático Medio entre dos tensores o listas de números."""
    if isinstance(y_true, list) and isinstance(y_pred, list):
        if len(y_true) != len(y_pred):
            raise TrezRuntimeError("Loss mse() mismatch: Las dimensiones de y_true e y_pred no coinciden.")
        return sum((t - p) ** 2 for t, p in zip(y_true, y_pred)) / len(y_true)
    elif isinstance(y_true, (int, float)) and isinstance(y_pred, (int, float)):
        return (y_true - y_pred) ** 2
    else:
        raise TrezRuntimeError("Tipos no soportados para mse(). Se requieren números o listas planas.")

def mse_grad(y_true, y_pred):
    """Calcula el gradiente (derivada) del MSE con respecto a y_pred."""
    if isinstance(y_true, list) and isinstance(y_pred, list):
        if len(y_true) != len(y_pred):
            raise TrezRuntimeError("Loss mse_grad() mismatch: Las dimensiones de y_true e y_pred no coinciden.")
        n = len(y_true)
        return [2 * (p - t) / n for t, p in zip(y_true, y_pred)]
    elif isinstance(y_true, (int, float)) and isinstance(y_pred, (int, float)):
        return 2 * (y_pred - y_true)
    else:
        raise TrezRuntimeError("Tipos no soportados para mse_grad().")
