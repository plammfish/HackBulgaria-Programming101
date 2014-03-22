import unittest
import solution

class TestIsPrime(unittest.TestCase):
    """Tests for TestIsPrime"""
    def test_is_prime(self):
        self.assertFalse(solution.is_prime(1))
        self.assertTrue(solution.is_prime(2))
        self.assertFalse(solution.is_prime(8))
        self.assertTrue(solution.is_prime(11))
        self.assertFalse(solution.is_prime(-10))

if __name__ == '__main__':
    unittest.main()
