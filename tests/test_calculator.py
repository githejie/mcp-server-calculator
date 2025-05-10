import math
import unittest
from src.mcp_server_calculator.calculator import evaluate

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(evaluate("1 + 1"), "2")

    def test_subtraction(self):
        self.assertEqual(evaluate("5 - 3"), "2")

    def test_multiplication(self):
        self.assertEqual(evaluate("2 * 3"), "6")
        self.assertEqual(evaluate("2 × 3"), "6")

    def test_division(self):
        self.assertEqual(evaluate("8 / 2"), "4.0")
        self.assertEqual(evaluate("8 ÷ 2"), "4.0")

    def test_floor_division(self):
        self.assertEqual(evaluate("7 // 2"), "3")

    def test_modulus(self):
        self.assertEqual(evaluate("10 % 3"), "1")

    def test_power(self):
        self.assertEqual(evaluate("2 ** 3"), "8")
        self.assertEqual(evaluate("2 ^ 3"), "8")

    def test_unary_minus(self):
        self.assertEqual(evaluate("-5"), "-5")

    def test_complex_expression(self):
        self.assertEqual(evaluate("2 + 3 * (4 - 1) / 2 ** 2"), "4.25")

    def test_parentheses_expression(self):
        self.assertEqual(evaluate("(2 + 3) * 4"), "20")

    def test_negative_numbers(self):
        self.assertEqual(evaluate("-2 + 3"), "1")
        self.assertEqual(evaluate("4 * -2"), "-8")
        self.assertEqual(evaluate("-6 / 2"), "-3.0")

    def test_floating_point_operations(self):
        self.assertEqual(evaluate("0.5 + 0.25"), "0.75")
        self.assertEqual(evaluate("2.5 * 2"), "5.0")
        self.assertEqual(evaluate("5.0 / 2"), "2.5")

    def test_large_numbers(self):
        self.assertEqual(evaluate("123456789 * 987654321"), str(123456789 * 987654321))

    def test_floating_point_precision(self):
        self.assertAlmostEqual(float(evaluate("0.1 + 0.2")), 0.3, places=7)

    def test_unsupported_operation(self):
        with self.assertRaises(ValueError):
            evaluate("unknown")

    def test_empty_string(self):
        with self.assertRaises(SyntaxError):
            evaluate("")

    def test_whitespace_string(self):
        with self.assertRaises(SyntaxError):
            evaluate("   ")

    def test_invalid_expression(self):
        with self.assertRaises(SyntaxError):
            evaluate("2 +")

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            evaluate("1 / 0")

    def test_floor_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            evaluate("1 // 0")

    def test_modulus_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            evaluate("1 % 0")

    def test_math_functions(self):
        self.assertAlmostEqual(float(evaluate("sin(pi/2)")), math.sin(math.pi/2), places=7)
        self.assertAlmostEqual(float(evaluate("cos(0)")), math.cos(0), places=7)
        self.assertAlmostEqual(float(evaluate("sqrt(16)")), math.sqrt(16), places=7)
        self.assertAlmostEqual(float(evaluate("log(e)")), math.log(math.e), places=7)
        self.assertAlmostEqual(float(evaluate("exp(1)")), math.exp(1), places=7)
        self.assertAlmostEqual(float(evaluate("tan(0)")), math.tan(0), places=7)
        self.assertAlmostEqual(float(evaluate("fabs(-5)")), math.fabs(-5), places=7)
        self.assertAlmostEqual(float(evaluate("factorial(5)")), math.factorial(5), places=7)
        self.assertAlmostEqual(float(evaluate("pow(2, 5)")), math.pow(2, 5), places=7)
        self.assertAlmostEqual(float(evaluate("degrees(pi)")), math.degrees(math.pi), places=7)
        self.assertAlmostEqual(float(evaluate("radians(180)")), math.radians(180), places=7)
        self.assertAlmostEqual(float(evaluate("pi")), math.pi, places=7)
        self.assertAlmostEqual(float(evaluate("e")), math.e, places=7)

if __name__ == '__main__':
    unittest.main()
