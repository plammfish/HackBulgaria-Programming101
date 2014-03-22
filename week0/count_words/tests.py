import unittest
import solution

class TestCountWords(unittest.TestCase):
    """Tests for TestCountWords"""
    def test_count_words(self):
        expected1 = {'apple': 2, 'pie': 1, 'banana': 1}
        self.assertEqual(expected1, solution.count_words(["apple", \
            "banana", "apple", "pie"]))
        expected2 = {'ruby': 1, 'python': 3}
        self.assertEqual(expected2, solution.count_words(["python",\
         "python", "python", "ruby"]))

if __name__ == '__main__':
    unittest.main()
