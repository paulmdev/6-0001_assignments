import unittest

from hangman import get_available_letters, get_guessed_word, is_word_guessed


class HangmanTesting(unittest.TestCase):
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
