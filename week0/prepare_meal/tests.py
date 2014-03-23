import unittest
import solution

class TestPrepareMeal(unittest.TestCase):
    """Tests for TestPrepareMeal"""
    def test_prepare_meal(self):
        self.assertEqual(solution.prepare_meal(5), "eggs")
        self.assertEqual(solution.prepare_meal(3), "spam")
        self.assertEqual(solution.prepare_meal(27), "spam spam spam")
        self.assertEqual(solution.prepare_meal(15), "spam and eggs")
        self.assertEqual(solution.prepare_meal(45), "spam spam and eggs")
        self.assertEqual(solution.prepare_meal(7), "")

if __name__ == '__main__':
    unittest.main()
