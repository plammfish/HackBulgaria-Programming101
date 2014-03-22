import unittest
import solution

class ClassNthFibonacci(unittest.TestCase):
    """tests for ClassNthFibonacci"""
    def test_for_nth_fibonacci(self):
        self.assertEqual(1, solution.nth_fibonacci(1))
        self.assertEqual(1, solution.nth_fibonacci(2))
        self.assertEqual(2, solution.nth_fibonacci(3))
        self.assertEqual(55, solution.nth_fibonacci(10))

if __name__ == '__main__':
    unittest.main()
