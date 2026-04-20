from errors import TrezRuntimeError

# === Constantes Matemáticas Nativas ===
PI = 3.14159265358979323846
E  = 2.71828182845904523536

# === Funciones Algebraicas ===
def abs(x):
    """Valor absoluto de x."""
    if isinstance(x, (int, float)):
        return x if x >= 0 else -x
    elif isinstance(x, list):
        return [abs(i) for i in x]
    raise TrezRuntimeError("abs() requiere un número o un tensor.")

def pow(base, exp):
    """Potencia real: base^exp. Maneja enteros positivos y negativos nativamente."""
    if isinstance(base, list):
        return [pow(b, exp) for b in base]
    if isinstance(exp, int):
        if exp == 0:
            return 1.0
        elif exp < 0:
            return 1.0 / pow(base, -exp)
        res = 1.0
        for _ in range(exp):
            res *= base
        return res
    # Para flotantes, base^exp = e^(exp * ln(base))
    return exp(exp * log(base))

def factorial(n):
    """Calcula n! iterativamente."""
    if isinstance(n, float) and n.is_integer():
        n = int(n)
    if not isinstance(n, int) or n < 0:
        raise TrezRuntimeError("factorial() requiere un número entero positivo.")
    if n == 0:
        return 1
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

def sqrt(x):
    """Raíz cuadrada usando el Método de Newton-Raphson."""
    if isinstance(x, list):
        return [sqrt(i) for i in x]
    if x < 0:
        raise TrezRuntimeError("sqrt() no soporta números negativos en TREZ (aún no hay complejos).")
    if x == 0:
        return 0.0

    # Newton-Raphson: z_{n+1} = 0.5 * (z_n + x / z_n)
    guess = x / 2.0
    for _ in range(20):
        guess = 0.5 * (guess + x / guess)
    return guess

# === Funciones Trascendentales (Series de Taylor/Maclaurin) ===
def exp(x, terms=30):
    """e^x utilizando Serie de Maclaurin."""
    if isinstance(x, list):
        return [exp(i) for i in x]
    if x < 0:
        return 1.0 / exp(-x, terms)

    result = 1.0
    term = 1.0
    for i in range(1, terms):
        term *= (x / i)
        result += term
    return result

def log(x, terms=50):
    """Logaritmo natural ln(x) usando Serie de Mercator centrada y ajuste de rango."""
    if isinstance(x, list):
        return [log(i) for i in x]
    if x <= 0:
        raise TrezRuntimeError("log() requiere un número estrictamente positivo.")

    ln_e_count = 0.0
    while x >= E:
        x /= E
        ln_e_count += 1.0
    while x <= 1.0/E:
        x *= E
        ln_e_count -= 1.0

    y = (x - 1) / (x + 1)
    y2 = y * y
    result = 0.0
    term = y
    for n in range(1, terms*2, 2):
        result += term / n
        term *= y2

    return 2.0 * result + ln_e_count

def sin(x, terms=20):
    """Seno de x en radianes usando Serie de Taylor."""
    if isinstance(x, list):
        return [sin(i) for i in x]

    x = x % (2 * PI)
    if x > PI:
        x -= 2 * PI

    result = 0.0
    sign = 1
    for n in range(terms):
        term = pow(x, 2*n + 1) / factorial(2*n + 1)
        result += sign * term
        sign *= -1
    return result

def cos(x, terms=20):
    """Coseno de x en radianes usando Serie de Taylor."""
    if isinstance(x, list):
        return [cos(i) for i in x]

    x = x % (2 * PI)
    if x > PI:
        x -= 2 * PI

    result = 0.0
    sign = 1
    for n in range(terms):
        term = pow(x, 2*n) / factorial(2*n)
        result += sign * term
        sign *= -1
    return result

def tan(x):
    """Tangente de x (sen(x) / cos(x))"""
    if isinstance(x, list):
        return [tan(i) for i in x]
    cosine = cos(x)
    if abs(cosine) < 1e-10:
        raise TrezRuntimeError("tan() indefinida (división por asintota PI/2).")
    return sin(x) / cosine
