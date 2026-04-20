"""
Test suite for TREZ core mathematical functions.
Tests all native math implementations without external dependencies.
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from lib.math.core import abs, pow, sqrt, exp, log, sin, cos, tan, factorial, PI, E


class TestAlgebraic:
    """Test basic algebraic functions."""

    def test_abs_positive(self):
        assert abs(5) == 5

    def test_abs_negative(self):
        assert abs(-5) == 5

    def test_abs_zero(self):
        assert abs(0) == 0

    def test_abs_array(self):
        assert abs([-1, -2, 3]) == [1, 2, 3]

    def test_pow_positive_exp(self):
        assert pow(2, 3) == 8
        assert pow(3, 2) == 9

    def test_pow_zero_exp(self):
        assert pow(5, 0) == 1.0

    def test_pow_negative_exp(self):
        result = pow(2, -2)
        assert abs(result - 0.25) < 1e-6

    def test_sqrt(self):
        assert abs(sqrt(16) - 4) < 1e-6
        assert abs(sqrt(2) - 1.41421356) < 1e-5

    def test_sqrt_zero(self):
        assert sqrt(0) == 0.0

    def test_factorial(self):
        assert factorial(0) == 1
        assert factorial(5) == 120
        assert factorial(1) == 1


class TestTranscendental:
    """Test transcendental functions (exp, log, trig)."""

    def test_exp_zero(self):
        assert abs(exp(0) - 1.0) < 1e-6

    def test_exp_one(self):
        assert abs(exp(1) - E) < 1e-6

    def test_log_e(self):
        assert abs(log(E) - 1.0) < 1e-6

    def test_log_one(self):
        assert abs(log(1.0) - 0.0) < 1e-6

    def test_sin_zero(self):
        assert abs(sin(0)) < 1e-6

    def test_sin_pi_half(self):
        assert abs(sin(PI / 2) - 1.0) < 1e-6

    def test_cos_zero(self):
        assert abs(cos(0) - 1.0) < 1e-6

    def test_cos_pi(self):
        assert abs(cos(PI) + 1.0) < 1e-6

    def test_tan_zero(self):
        assert abs(tan(0)) < 1e-6


class TestConstants:
    """Test mathematical constants."""

    def test_pi_value(self):
        assert abs(PI - 3.14159265) < 1e-6

    def test_e_value(self):
        assert abs(E - 2.71828182) < 1e-6


if __name__ == '__main__':
    # Simple runner for basic validation
    import traceback

    test_classes = [TestAlgebraic, TestTranscendental, TestConstants]
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
