import unittest

from ps3 import get_word_score, update_hand


class Tests(unittest.TestCase):
    def test_get_word_score(self):
        words = {("", 7): 0, ("it", 7): 2, ("was", 7): 54, ("weed", 6): 176,
                 ("scored", 7): 351, ("WaYbILl", 7): 735, ("Outgnaw", 7): 539,
                 ("fork", 7): 209, ("FORK", 4): 308}
        for word, n in words.keys():
            self.assertEqual(get_word_score(word, n), words[(word, n)])


class UpdateHandTests(unittest.TestCase):
    def test_update_hand_1(self):
        original_hand = {'a': 1, 'q': 1, 'l': 2, 'm': 1, 'u': 1, 'i': 1}
        original_hand_copy = original_hand.copy()
        word = "quail"

        new_hand = update_hand(original_hand_copy, word)
        expected_new_hand = {'l': 1, 'm': 1}

        self.assertDictEqual(new_hand, expected_new_hand)

        # Test it doesn't modify the hand
        self.assertDictEqual(original_hand, original_hand_copy)

    def test_update_hand_2(self):
        original_hand = {'e': 1, 'v': 2, 'n': 1, 'i': 1, 'l': 2}
        original_hand_copy = original_hand.copy()
        word = "Evil"

        new_hand = update_hand(original_hand_copy, word)
        expected_new_hand = {'v': 1, 'n': 1, 'l': 1}

        self.assertDictEqual(new_hand, expected_new_hand)

        self.assertDictEqual(original_hand, original_hand_copy)

    def test_update_hand_3(self):
        original_hand = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
        original_hand_copy = original_hand.copy()
        word = "HELLO"

        new_hand = update_hand(original_hand_copy, word)
        expected_new_hand = {}

        self.assertDictEqual(new_hand, expected_new_hand)

        self.assertDictEqual(original_hand, original_hand_copy)
