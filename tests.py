import unittest
import sum_of_digits

class SumOfDigitsTests(unittest.TestCase):
    def test_for_sum_of_digits(self):
        self.assertEqual(43, sum_of_digits.sum_of_digits(1325132435356))
        self.assertEqual(6, sum_of_digits.sum_of_digits(123))
        self.assertEqual(6, sum_of_digits.sum_of_digits(6))
        self.assertEqual(1, sum_of_digits.sum_of_digits(-10))

if __name__ == '__main__':
    unittest.main()
