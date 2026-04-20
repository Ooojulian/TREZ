"""
Test suite for TREZ activation functions.
Tests ReLU, Sigmoid, and other neural network activations.
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from lib.activations import relu, sigmoid


class TestReLU:
    """Test Rectified Linear Unit activation."""

    def test_relu_positive(self):
        assert relu(5) == 5

    def test_relu_negative(self):
        assert relu(-3) == 0

    def test_relu_zero(self):
        assert relu(0) == 0

    def test_relu_vector(self):
        result = relu([1, -2, 3, -4])
        assert result == [1, 0, 3, 0]


class TestSigmoid:
    """Test Sigmoid activation function."""

    def test_sigmoid_zero(self):
        # sigmoid(0) = 1 / (1 + e^0) = 1/2 = 0.5
        result = sigmoid(0)
        assert abs(result - 0.5) < 1e-6

    def test_sigmoid_positive(self):
        # sigmoid(x) should be between 0 and 1
        result = sigmoid(2)
        assert 0 < result < 1

    def test_sigmoid_negative(self):
        # sigmoid(-x) = 1 - sigmoid(x)
        result = sigmoid(-2)
        assert 0 < result < 1

    def test_sigmoid_vector(self):
        result = sigmoid([-1, 0, 1])
        assert len(result) == 3
        assert all(0 < r < 1 for r in result)

    def test_sigmoid_symmetry(self):
        # sigmoid(x) + sigmoid(-x) ≈ 1
        s_pos = sigmoid(1.5)
        s_neg = sigmoid(-1.5)
        assert abs((s_pos + s_neg) - 1.0) < 1e-6


if __name__ == '__main__':
    import traceback

    test_classes = [TestReLU, TestSigmoid]
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
