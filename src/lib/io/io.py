import os
from errors import TrezRuntimeError

def read_file(filename):
    """Lee el contenido de un archivo de texto/csv plano."""
    if not isinstance(filename, str):
        raise TrezRuntimeError(f"read_file(): Se esperaba un texto (ruta), se recibió: {type(filename).__name__}")

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        raise TrezRuntimeError(f"TREZ IO Error: El archivo '{filename}' no existe o no se pudo encontrar.")
    except Exception as e:
        raise TrezRuntimeError(f"TREZ IO Error al leer el archivo: {e}")

def write_file(filename, content):
    """Escribe o sobreescribe contenido de texto en un archivo."""
    if not isinstance(filename, str):
        raise TrezRuntimeError(f"write_file(): La ruta del archivo debe ser texto.")

    if not isinstance(content, str):
        content = str(content)

    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    except Exception as e:
        raise TrezRuntimeError(f"TREZ IO Error al escribir en '{filename}': {e}")
