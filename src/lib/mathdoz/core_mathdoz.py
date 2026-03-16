from errors import TrezRuntimeError

# === Constantes Matemáticas Nativas ===
PI_DOZ = 3.14159265358979323846
E_DOZ  = 2.71828182845904523536

# === Funciones Algebraicas ===
def abs_doz(x):
    """Valor absoluto de x."""
    if isinstance(x, (int, float)):
        return x if x >= 0 else -x
    elif isinstance(x, list):
        return [abs_doz(i) for i in x]
    raise TrezRuntimeError("abs() requiere un número o un tensor.")

def pow_doz(base, exp):
    """Potencia real: base^exp. Maneja enteros positivos y negativos nativamente."""
    if isinstance(base, list):
        return [pow_doz(b, exp) for b in base]
    if isinstance(exp, int):
        if exp == 0:
            return 1.0
        elif exp < 0:
            return 1.0 / pow_doz(base, -exp)
        res = 1.0
        for _ in range(exp):
            res *= base
        return res
    # Para flotantes, base^exp = e^(exp * ln(base))
    return exp_doz(exp * log_doz(base))

def factorial_doz(n):
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

def sqrt_doz(x):
    """Raíz cuadrada usando el Método de Newton-Raphson."""
    if isinstance(x, list):
        return [sqrt_doz(i) for i in x]
    if x < 0:
        raise TrezRuntimeError("sqrt() no soporta números negativos en TREZ (aún no hay complejos).")
    if x == 0:
        return 0.0
    
    # Newton-Raphson: z_{n+1} = 0.5 * (z_n + x / z_n)
    guess = x / 2.0
    for _ in range(20): # Converge muy rápido
        guess = 0.5 * (guess + x / guess)
    return guess

# === Funciones Trascendentales (Series de Taylor/Maclaurin) ===
def exp_doz(x, terms=30):
    """e^x utilizando Serie de Maclaurin."""
    if isinstance(x, list):
        return [exp_doz(i) for i in x]
    if x < 0:
        return 1.0 / exp_doz(-x, terms)
    
    result = 1.0
    term = 1.0
    for i in range(1, terms):
        term *= (x / i)
        result += term
    return result

def log_doz(x, terms=50):
    """Logaritmo natural ln(x) usando Serie de Mercator centrada y ajuste de rango."""
    if isinstance(x, list):
        return [log_doz(i) for i in x]
    if x <= 0:
        raise TrezRuntimeError("log() requiere un número estrictamente positivo.")
    
    # La serie de Mercator solo es precisa cerca de x=1. 
    # Reducimos x repetidamente dividiendo por E_DOZ y sumamos el exponente.
    ln_e_count = 0.0
    while x >= E_DOZ:
        x /= E_DOZ
        ln_e_count += 1.0
    while x <= 1.0/E_DOZ:
        x *= E_DOZ
        ln_e_count -= 1.0
        
    # Método numérico algebraico rápido para ln(x) cercano a 1: 
    # ln(x) = 2 * sum_{n=1,3,5..} (1/n) * ((x-1)/(x+1))^n
    y = (x - 1) / (x + 1)
    y2 = y * y
    result = 0.0
    term = y
    for n in range(1, terms*2, 2):
        result += term / n
        term *= y2
        
    return 2.0 * result + ln_e_count

def sin_doz(x, terms=20):
    """Seno de x en radianes usando Serie de Taylor."""
    if isinstance(x, list):
        return [sin_doz(i) for i in x]
    
    # Reducir el rango al periodo 2*PI para que la serie no falle por grandes números
    x = x % (2 * PI_DOZ)
    if x > PI_DOZ:
        x -= 2 * PI_DOZ
        
    result = 0.0
    sign = 1
    for n in range(terms):
        term = pow_doz(x, 2*n + 1) / factorial_doz(2*n + 1)
        result += sign * term
        sign *= -1
    return result

def cos_doz(x, terms=20):
    """Coseno de x en radianes usando Serie de Taylor."""
    if isinstance(x, list):
        return [cos_doz(i) for i in x]
    
    x = x % (2 * PI_DOZ)
    if x > PI_DOZ:
        x -= 2 * PI_DOZ
        
    result = 0.0
    sign = 1
    for n in range(terms):
        term = pow_doz(x, 2*n) / factorial_doz(2*n)
        result += sign * term
        sign *= -1
    return result

def tan_doz(x):
    """Tangente de x (sen(x) / cos(x))"""
    if isinstance(x, list):
        return [tan_doz(i) for i in x]
    cosine = cos_doz(x)
    if abs_doz(cosine) < 1e-10:
        raise TrezRuntimeError("tan() indefinida (división por asintota PI/2).")
    return sin_doz(x) / cosine
