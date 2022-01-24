import unittest

from ps3 import get_word_score


class Tests(unittest.TestCase):
    def test_get_word_score(self):
        words = {("", 7): 0, ("it", 7): 2, ("was", 7): 54, ("weed", 6): 176,
                 ("scored", 7): 351, ("WaYbILl", 7): 735, ("Outgnaw", 7): 539,
                 ("fork", 7): 209, ("FORK", 4): 308}
        for word, n in words.keys():
            self.assertEqual(get_word_score(word, n), words[(word, n)])
