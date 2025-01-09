import unittest
from math_fmod_program import compute_fmod

class TestComputeFmod(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(compute_fmod(10, 3), 1.0)
        self.assertEqual(compute_fmod(20, 5), 0.0)

    def test_negative_numbers(self):
        self.assertEqual(compute_fmod(-10, 3), -1.0)
        self.assertEqual(compute_fmod(-20, -6), -2.0)

    def test_mixed_sign_numbers(self):
        self.assertEqual(compute_fmod(10, -3), 1.0)
        self.assertEqual(compute_fmod(-10, 3), -1.0)

    def test_zero_division(self):
        self.assertEqual(compute_fmod(10, 0), "Division by zero is not allowed")

    def test_float_inputs(self):
        self.assertAlmostEqual(compute_fmod(10.5, 3.2), 0.8999999999999995)
        self.assertAlmostEqual(compute_fmod(-10.5, 3.2), -0.8999999999999995)

if __name__ == "__main__":
    unittest.main()
