import unittest
import solution

class TestIsIntPalindrome(unittest.TestCase):
    """Tests for TestIsIntPalindrome"""
    def test_is_int_palindrome(self):
        self.assertTrue(solution.is_int_palindrome(1))
        self.assertFalse(solution.is_int_palindrome(42))
        self.assertTrue(solution.is_int_palindrome(100001))
        self.assertTrue(solution.is_int_palindrome(999))
        self.assertFalse(solution.is_int_palindrome(123))

if __name__ == '__main__':
    unittest.main()
