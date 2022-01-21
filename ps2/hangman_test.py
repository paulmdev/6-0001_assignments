import unittest

from hangman import get_available_letters, get_guessed_word, is_word_guessed, match_with_gaps


class HangmanProblem3(unittest.TestCase):
    def test_the_word_is_not_guessed(self):
        secret_word = "apple"
        letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']

        self.assertFalse(is_word_guessed(
            secret_word, letters_guessed))

    def test_return_hidden_letters(self):
        secret_word = "apple"
        letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']

        self.assertEqual("_ pp_ e", get_guessed_word(
            secret_word, letters_guessed))

    def test_available_letters(self):
        letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
        self.assertEqual("abcdfghjlmnoqtuvwxyz",
                         get_available_letters(letters_guessed))


class HangmanMatchGaps(unittest.TestCase):
    def test_not_match_tact(self):
        self.assertFalse(match_with_gaps("te_ t", "tact"))

    def test_not_match_banana(self):
        self.assertFalse(match_with_gaps("a_ _ le", "banana"))

    def test_match_apple(self):
        self.assertTrue(match_with_gaps("a_ _ le", "apple"))

    def test_not_match_apples(self):
        self.assertFalse(match_with_gaps("a_ ple", "apple"))
