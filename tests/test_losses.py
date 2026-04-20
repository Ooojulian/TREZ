"""
Test suite for TREZ loss functions.
Tests Mean Squared Error and other training loss calculations.
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from lib.losses import mse, mse_grad


class TestMSE:
    """Test Mean Squared Error loss function."""

    def test_mse_scalar_exact_match(self):
        # When predictions match truth, MSE should be 0
        assert mse(5.0, 5.0) == 0

    def test_mse_scalar_off_by_one(self):
        # (5 - 4)^2 = 1
        assert mse(5.0, 4.0) == 1

    def test_mse_vector_simple(self):
        y_true = [1, 2, 3]
        y_pred = [1, 2, 3]
        assert mse(y_true, y_pred) == 0

    def test_mse_vector(self):
        y_true = [1, 2, 3]
        y_pred = [2, 3, 4]
        # MSE = ((1-2)^2 + (2-3)^2 + (3-4)^2) / 3 = (1 + 1 + 1) / 3 = 1
        assert mse(y_true, y_pred) == 1.0

    def test_mse_vector_with_floats(self):
        y_true = [0.0, 1.0, 0.0]
        y_pred = [0.1, 0.9, 0.2]
        result = mse(y_true, y_pred)
        # MSE = ((0.1)^2 + (0.1)^2 + (0.2)^2) / 3 = (0.01 + 0.01 + 0.04) / 3 ≈ 0.0200
        assert abs(result - 0.02) < 1e-6


class TestMSEGradient:
    """Test Mean Squared Error gradient (for backpropagation)."""

    def test_mse_grad_scalar(self):
        # grad = 2 * (y_pred - y_true)
        grad = mse_grad(5.0, 6.0)
        assert grad == 2 * (6.0 - 5.0)  # 2.0

    def test_mse_grad_vector(self):
        y_true = [1, 2, 3]
        y_pred = [2, 3, 4]
        grad = mse_grad(y_true, y_pred)
        # For each element: 2 * (pred - true) / n
        # [2*(2-1)/3, 2*(3-2)/3, 2*(4-3)/3] = [2/3, 2/3, 2/3]
        expected = [2/3, 2/3, 2/3]
        assert len(grad) == 3
        assert all(abs(g - e) < 1e-6 for g, e in zip(grad, expected))

    def test_mse_grad_vector_exact_match(self):
        y_true = [1, 2, 3]
        y_pred = [1, 2, 3]
        grad = mse_grad(y_true, y_pred)
        assert grad == [0, 0, 0]

    def test_mse_grad_proportional_to_error(self):
        # Larger error should produce larger gradient
        grad1 = mse_grad(1.0, 2.0)  # error = 1
        grad2 = mse_grad(1.0, 3.0)  # error = 2
        assert abs(grad2) > abs(grad1)


if __name__ == '__main__':
    import traceback

    test_classes = [TestMSE, TestMSEGradient]
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
