import unittest
import solution

class TestUniqueWordsCount(unittest.TestCase):
    """Tests for TestUniqueWordsCount"""
    def test_unique_words_count(self):
        self.assertEqual(3, solution.unique_words_count(["apple", \
            "banana", "apple", "pie"]))
        self.assertEqual(2, solution.unique_words_count(["python", \
            "python", "python", "ruby"]))
        self.assertEqual(1, solution.unique_words_count(["HELLO!"] * 10))

if __name__ == '__main__':
    unittest.main()
