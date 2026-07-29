import unittest

from fibonacci import fibonacci


class FibonacciTests(unittest.TestCase):
    def test_first_numbers(self):
        self.assertEqual(
            [fibonacci(n) for n in range(11)],
            [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55],
        )

    def test_large_number(self):
        self.assertEqual(fibonacci(100), 354224848179261915075)

    def test_negative_number_is_rejected(self):
        with self.assertRaises(ValueError):
            fibonacci(-1)

    def test_non_integer_is_rejected(self):
        for value in (1.5, "5", True, None):
            with self.subTest(value=value):
                with self.assertRaises(TypeError):
                    fibonacci(value)


if __name__ == "__main__":
    unittest.main()
