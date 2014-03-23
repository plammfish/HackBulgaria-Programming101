import unittest
import solution

class TestIsAnBn(unittest.TestCase):
    """Tests for TestIsAnBn"""
    def test_is_an_bn(self):
        self.assertTrue(solution.is_an_bn(""))
        self.assertFalse(solution.is_an_bn("rado"))
        self.assertFalse(solution.is_an_bn("aaabb"))
        self.assertTrue(solution.is_an_bn("aaabbb"))
        self.assertFalse(solution.is_an_bn("aabbaabb"))
        self.assertFalse(solution.is_an_bn("bbbaaa"))
        self.assertTrue(solution.is_an_bn("aaaaabbbbb"))

if __name__ == '__main__':
    unittest.main()

