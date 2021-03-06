import unittest

from ps3 import *


class GetWordScoreTest(unittest.TestCase):
    def test_get_word_score(self):
        words = {("", 7): 0, ("it", 7): 2, ("was", 7): 54, ("weed", 6): 176,
                 ("scored", 7): 351, ("WaYbILl", 7): 735, ("Outgnaw", 7): 539,
                 ("fork", 7): 209, ("FORK", 4): 308}
        for word, n in words.keys():
            self.assertEqual(get_word_score(word, n), words[(word, n)])


class UpdateHandTests(unittest.TestCase):
    def test_no_side_effects(self):
        original_hand = {'a': 1, 'q': 1, 'l': 2, 'm': 1, 'u': 1, 'i': 1}
        original_hand_copy = original_hand.copy()
        word = "quail"

        update_hand(original_hand_copy, word)

        # Test it doesn't modify the hand
        self.assertDictEqual(original_hand, original_hand_copy)

    def test_update_hand_1(self):
        original_hand = {'a': 1, 'q': 1, 'l': 2, 'm': 1, 'u': 1, 'i': 1}
        original_hand_copy = original_hand.copy()
        word = "quail"

        new_hand = update_hand(original_hand_copy, word)
        expected_new_hand = {'l': 1, 'm': 1}

        self.assertDictEqual(new_hand, expected_new_hand)

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


class IsValidWordTests(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.word_list = load_words()

    def test_no_side_effects(self):
        word = "hello"
        original_hand = get_frequency_dict(word)
        original_hand_copy = original_hand.copy()

        is_valid_word(
            word, original_hand_copy, self.word_list)

        self.assertDictEqual(original_hand, original_hand_copy)

    def test_is_valid_word_1(self):
        word = "hello"
        hand = get_frequency_dict(word)

        self.assertTrue(is_valid_word(
            word, hand, self.word_list))

    def test_is_valid_word_2(self):
        word = "Rapture"
        hand = {'r': 1, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u': 1}

        self.assertFalse(is_valid_word(
            word, hand, self.word_list))

    def test_is_valid_word_3(self):
        word = "honey"
        hand = {'n': 1, 'h': 1, 'o': 1, 'y': 1, 'd': 1, 'w': 1, 'e': 2}

        self.assertTrue(is_valid_word(
            word, hand, self.word_list))

    def test_is_valid_word_4(self):
        word = "honey"
        hand = {'r': 1, 'a': 3, 'p': 2, 't': 1, 'u': 2}

        self.assertFalse(is_valid_word(
            word, hand, self.word_list))

    def test_is_valid_word_5(self):
        word = "EVIL"
        hand = {'e': 1, 'v': 2, 'n': 1, 'i': 1, 'l': 2}

        self.assertTrue(is_valid_word(
            word, hand, self.word_list))

    def test_is_valid_word_6(self):
        word = "Even"
        hand = {'e': 1, 'v': 2, 'n': 1, 'i': 1, 'l': 2}

        self.assertFalse(is_valid_word(
            word, hand, self.word_list))


class WildcardTests(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.word_list = load_words()

    def test_wilcard_false_1(self):
        hand = {'a': 1, 'r': 1, 'e': 1, 'j': 2, 'm': 1, '*': 1}
        word = "e*m"

        self.assertFalse(is_valid_word(word, hand, self.word_list))

    def test_wilcard_false_2(self):
        hand = {'n': 1, 'h': 1, '*': 1, 'y': 1, 'd': 1, 'w': 1, 'e': 2}
        word = "honey"

        self.assertFalse(is_valid_word(word, hand, self.word_list))

    def test_wilcard_false_3(self):
        hand = {'c': 1, 'o': 1, '*': 1, 'w': 1, 's': 1, 'z': 1, 'y': 2}
        word = "c*wz"

        self.assertFalse(is_valid_word(word, hand, self.word_list))

    def test_wildcard_true(self):
        hand = {'n': 1, 'h': 1, '*': 1, 'y': 1, 'd': 1, 'w': 1, 'e': 2}
        word = "h*ney"

        self.assertTrue(is_valid_word(word, hand, self.word_list))

    def test_scores_with_wildcards(self):
        words = {("h*ney", 7): 290, ("c*ws", 6): 176, ("wa*ls", 7): 203}

        for (word, n) in words.keys():
            score = get_word_score(word, n)

            self.assertEqual(score, words[((word, n))])
