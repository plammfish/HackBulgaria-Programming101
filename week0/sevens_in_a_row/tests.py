import unittest
import solution

class TestSevensInARow(unittest.TestCase):
    """TestCase for TestSevensInARow"""
    def test_sevens_in_a_row(self):
        self.assertTrue(solution.sevens_in_a_row([10,8,7,6,7,7,7,20,-7], 3))
        self.assertFalse(solution.sevens_in_a_row([1,7,1,7,7], 4))
        self.assertTrue(solution.sevens_in_a_row([7,7,7,1,1,1,7,7,7,7], 3))
        self.assertTrue(solution.sevens_in_a_row([7,2,1,6,2], 1))


if __name__ == '__main__':
    unittest.main()
