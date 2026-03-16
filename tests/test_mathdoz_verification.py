import sys
import os
import math # Only used to assert correctness of our native implementation

# Add src to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))

from lib.mathdoz.core_mathdoz import (
    PI_DOZ, E_DOZ, abs_doz, pow_doz, sqrt_doz, 
    exp_doz, log_doz, sin_doz, cos_doz, tan_doz, factorial_doz
)
from lib.mathdoz.tensor_mathdoz import dot, transpose

def test_core_math():
    print("--- Probando Native Core Math (core_mathdoz) ---")
    
    # Tolerancia aceptable para algoritmos numéricos
    TOLERANCE = 1e-5

    # 1. Constantes
    assert abs(PI_DOZ - math.pi) < TOLERANCE, "PI_DOZ falló"
    assert abs(E_DOZ - math.e) < TOLERANCE, "E_DOZ falló"
    print("✅ Constantes PI y E correctas")

    # 2. Funciones Algebraicas
    assert abs_doz(-42.5) == 42.5
    assert abs_doz(10) == 10
    print("✅ Valor absoluto correcto")

    assert pow_doz(2, 8) == 256.0
    assert pow_doz(5, 0) == 1.0
    assert abs(pow_doz(2, -2) - 0.25) < TOLERANCE
    print("✅ Potencias correctas")

    assert factorial_doz(5) == 120
    assert factorial_doz(0) == 1
    print("✅ Factoriales iterativos correctos")

    assert abs(sqrt_doz(16) - 4.0) < TOLERANCE
    assert abs(sqrt_doz(2) - math.sqrt(2)) < TOLERANCE
    assert sqrt_doz(0) == 0.0
    print("✅ Raíz cuadrada (Newton-Raphson) correcta")

    # 3. Trascendentales
    assert abs(exp_doz(5) - math.exp(5)) < TOLERANCE
    assert abs(exp_doz(-2) - math.exp(-2)) < TOLERANCE
    print("✅ Exponencial (Maclaurin) correcta")

    assert abs(log_doz(E_DOZ) - 1.0) < TOLERANCE
    assert abs(log_doz(10) - math.log(10)) < TOLERANCE
    print("✅ Logaritmo Natural (Taylor) correcto")

    assert abs(sin_doz(PI_DOZ / 2) - 1.0) < TOLERANCE
    assert abs(sin_doz(PI_DOZ) - 0.0) < TOLERANCE
    assert abs(cos_doz(PI_DOZ) - (-1.0)) < TOLERANCE
    assert abs(cos_doz(0) - 1.0) < TOLERANCE
    
    # Tangente aproximada
    assert abs(tan_doz(PI_DOZ / 4) - 1.0) < TOLERANCE
    print("✅ Funciones Trigonométricas (Taylor) correctas")

def test_tensor_math():
    print("\n--- Probando Operaciones de Tensores (tensor_mathdoz) ---")
    
    vec1 = [1, 2, 3]
    vec2 = [4, 5, 6]
    # dot product: 1*4 + 2*5 + 3*6 = 4 + 10 + 18 = 32
    assert dot(vec1, vec2) == 32
    print("✅ Producto Punto de Vectores correcto")

    mat1 = [[1, 2], [3, 4]]
    mat2 = [[2, 0], [1, 2]]
    # Mat mul: [[1*2+2*1, 1*0+2*2], [3*2+4*1, 3*0+4*2]] = [[4, 4], [10, 8]]
    expected_mat = [[4, 4], [10, 8]]
    assert dot(mat1, mat2) == expected_mat
    print("✅ Multiplicación de Matrices correcta")

    vec_col = [1, 2] # Treated as column for mat*vec
    # Mat * Vec: [1*1+2*2, 3*1+4*2] = [5, 11]
    assert dot(mat1, vec_col) == [5, 11]
    print("✅ Multiplicación Matriz-Vector correcta")

    m = [[1, 2, 3], [4, 5, 6]]
    expected_t = [[1, 4], [2, 5], [3, 6]]
    assert transpose(m) == expected_t
    print("✅ Transposición de Matrices correcta")

if __name__ == "__main__":
    try:
        test_core_math()
        test_tensor_math()
        print("\n🎉 ¡Todos los tests de mathdoz pasaron exitosamente!")
    except AssertionError as e:
        print(f"\n❌ Error en la aserción: {e}")
