from errors import TrezRuntimeError

def dot(a, b):
    # a and b are either numbers, 1D lists (vectors) or 2D lists (matrices)
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a * b

    # Dot product of two vectors
    if isinstance(a, list) and isinstance(b, list) and isinstance(a[0], (int, float)) and isinstance(b[0], (int, float)):
        if len(a) != len(b):
            raise TrezRuntimeError(f"Dimension mismatch for vector dot product: {len(a)} != {len(b)}")
        return sum(x * y for x, y in zip(a, b))

    # Matrix multiplication
    if isinstance(a, list) and isinstance(a[0], list) and isinstance(b, list) and isinstance(b[0], list):
        if len(a[0]) != len(b):
            raise TrezRuntimeError(f"Inner matrix dimensions must agree: ({len(a)}x{len(a[0])}) vs ({len(b)}x{len(b[0])})")
        
        result = []
        for i in range(len(a)):
            row = []
            for j in range(len(b[0])):
                val = 0
                for k in range(len(b)):
                    val += a[i][k] * b[k][j]
                row.append(val)
            result.append(row)
        return result

    # Vector-Matrix multiplication (assuming column vector)
    if isinstance(a, list) and isinstance(a[0], list) and isinstance(b, list) and isinstance(b[0], (int, float)):
         if len(a[0]) != len(b):
             raise TrezRuntimeError("Dimension mismatch in Vector-Matrix multiplication")
         return [dot(row, b) for row in a]

    raise TrezRuntimeError("Unsupported types for dot() product")

def transpose(m):
    if not isinstance(m, list) or not isinstance(m[0], list):
        raise TrezRuntimeError("transpose() only accepts a 2D matrix")
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
