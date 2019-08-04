import unittest
from source.Longest_Word import LongestWord

class LongestWordTest(unittest.TestCase):
    def test_empty_string(self):
        lw = LongestWord()
        self.assertEqual(lw.find_longest_word(''), (0, ''))

    def test_one_word(self):
        lw = LongestWord()
        self.assertEqual(lw.find_longest_word('Hello'), (5, 'Hello'))

    def test_normal_string(self):
        lw = LongestWord()
        self.assertEqual(lw.find_longest_word('Longest Word is VeryLong'), (8, 'VeryLong'))


if __name__ == '__main__':
    unittest.main()


