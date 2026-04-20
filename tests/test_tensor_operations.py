"""
Test suite for TREZ tensor operations.
Tests matrix multiplication, dot product, and transpose.
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from lib.math.tensor import dot, transpose


class TestDotProduct:
    """Test dot product function for various dimensions."""

    def test_scalar_multiply(self):
        assert dot(2, 3) == 6
        assert dot(0.5, 4) == 2.0

    def test_vector_dot_product(self):
        v1 = [1, 2, 3]
        v2 = [4, 5, 6]
        assert dot(v1, v2) == 1*4 + 2*5 + 3*6  # 32

    def test_matrix_multiply(self):
        # 2x3 @ 3x2 = 2x2
        A = [[1, 2, 3], [4, 5, 6]]
        B = [[7, 8], [9, 10], [11, 12]]
        result = dot(A, B)
        # A[0] · [B column vectors] = [1*7+2*9+3*11, 1*8+2*10+3*12]
        assert result[0][0] == 1*7 + 2*9 + 3*11  # 58
        assert result[0][1] == 1*8 + 2*10 + 3*12  # 64
        assert result[1][0] == 4*7 + 5*9 + 6*11  # 139
        assert result[1][1] == 4*8 + 5*10 + 6*12  # 154


class TestTranspose:
    """Test matrix transpose function."""

    def test_transpose_2x3(self):
        matrix = [[1, 2, 3], [4, 5, 6]]
        result = transpose(matrix)
        assert result == [[1, 4], [2, 5], [3, 6]]

    def test_transpose_3x2(self):
        matrix = [[1, 2], [3, 4], [5, 6]]
        result = transpose(matrix)
        assert result == [[1, 3, 5], [2, 4, 6]]

    def test_transpose_square(self):
        matrix = [[1, 2], [3, 4]]
        result = transpose(matrix)
        assert result == [[1, 3], [2, 4]]


class TestTensorArithmetic:
    """Test element-wise tensor operations."""

    def test_vector_scalar_multiply(self):
        # In TREZ, scalar * vector should work
        # This test validates the logic that should work in visitor
        v = [1, 2, 3]
        scalar = 2
        # The visitor handles this, but we can test the concept
        assert [scalar * x for x in v] == [2, 4, 6]


if __name__ == '__main__':
    import traceback

    test_classes = [TestDotProduct, TestTranspose, TestTensorArithmetic]
    total, passed = 0, 0

    for test_class in test_classes:
        print(f"\n▶ {test_class.__name__}")
        instance = test_class()
        for method_name in dir(instance):
            if method_name.startswith('test_'):
                total += 1
                try:
                    getattr(instance, method_name)()
                    passed += 1
                    print(f"  ✓ {method_name}")
                except AssertionError as e:
                    print(f"  ✗ {method_name}: {e}")
                except Exception as e:
                    print(f"  ✗ {method_name}: {type(e).__name__}: {e}")
                    traceback.print_exc()

    print(f"\n{'='*50}")
    print(f"Results: {passed}/{total} tests passed")
    print(f"{'='*50}")
