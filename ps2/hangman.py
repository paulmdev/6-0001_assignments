# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    for letter in secret_word:
        if letter not in letters_guessed:
            secret_word = secret_word.replace(letter, "_ ")

    return secret_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    available_letters = string.ascii_lowercase

    for letter in letters_guessed:
        available_letters = available_letters.replace(letter, '')

    return available_letters


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")

    print("-" * 13)

    guess_remaining = 6
    warnings_remaining = 3
    letters_guessed = []

    while guess_remaining > 0:
        print(f"You have {guess_remaining} guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))

        letter = input("Please guess a letter: ").lower()

        # Check if user input is valid.
        if not letter.isalpha() and warnings_remaining > 0:
            warnings_remaining -= 1
            print(f"Oops! That is not a valid letter. You have {warnings_remaining} warnings left:",
                  get_guessed_word(secret_word, letters_guessed))

            print("-" * 13)
            continue
        elif not letter.isalpha() and warnings_remaining == 0:
            print(f"Not a letter! You have {warnings_remaining} warnings: ",
                  get_guessed_word(secret_word, letters_guessed))

            guess_remaining -= 1

            print("-" * 13)
            continue

        # Check if the letter has already been guessed before.
        if letter in letters_guessed and warnings_remaining > 0:
            warnings_remaining -= 1
            print(f"Oops! You already guessed that letter. You have {warnings_remaining} warnings left:",
                  get_guessed_word(secret_word, letters_guessed))

            print("-" * 13)
            continue
        elif letter in letters_guessed and warnings_remaining == 0:
            print(f"You already guessed that letter! You have {warnings_remaining} warnings: ",
                  get_guessed_word(secret_word, letters_guessed))

            guess_remaining -= 1

            print("-" * 13)
            continue

        letters_guessed.append(letter)

        if letter in secret_word:
            print("Good guess:", get_guessed_word(
                secret_word, letters_guessed))
        else:
            print("Oops! That letter is not in my word:",
                  get_guessed_word(secret_word, letters_guessed))

            # If the letter is a vowel, the user loses two guesses.
            if letter in "aeiou":
                guess_remaining -= 2
            else:
                guess_remaining -= 1

        print("-" * 13)

        if secret_word == get_guessed_word(secret_word, letters_guessed):
            print("Congratulations, you won!")
            print("Your total score for this game is:",
                  guess_remaining * len(letters_guessed))
            break
    else:
        print("I'm sorry, you ran out of guesses.")
        print("The word was:", secret_word)


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word: str, other_word: str):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word = my_word.strip().replace(" ", "")

    if len(my_word) != len(other_word):
        return False

    for my_letter, other_letter in zip(my_word, other_word):
        if my_letter == "_":
            # If the current letter in other_word is present in my word.
            # When a letter is guessed, your code reveals all the positions at which
            # that letter occurs in the secret word. Therefore, the hidden letter (_ ) ???cannot be ???one
            # of the letters in the word that has already been revealed
            if other_letter in my_word:
                return False
        elif my_letter != other_letter:
            return False

    return True


def show_possible_matches(my_word, wordlist):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    return list(filter(lambda word: match_with_gaps(my_word, other_word=word), wordlist))


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")

    print("-" * 13)

    guess_remaining = 6
    warnings_remaining = 3
    letters_guessed = []

    while guess_remaining > 0:
        print(f"You have {guess_remaining} guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))

        letter = input("Please guess a letter: ").lower()

        if letter == "*":
            print("Possible word matches are:")
            print(*show_possible_matches(get_guessed_word(secret_word,
                  letters_guessed), wordlist))
            print("-" * 13)
            continue

        # Check if user input is valid.
        if not letter.isalpha() and warnings_remaining > 0:
            warnings_remaining -= 1
            print(f"Oops! That is not a valid letter. You have {warnings_remaining} warnings left:",
                  get_guessed_word(secret_word, letters_guessed))

            print("-" * 13)
            continue
        elif not letter.isalpha() and warnings_remaining == 0:
            print(f"Not a letter! You have {warnings_remaining} warnings: ",
                  get_guessed_word(secret_word, letters_guessed))

            guess_remaining -= 1

            print("-" * 13)
            continue

        # Check if the letter has already been guessed before.
        if letter in letters_guessed and warnings_remaining > 0:
            warnings_remaining -= 1
            print(f"Oops! You already guessed that letter. You have {warnings_remaining} warnings left:",
                  get_guessed_word(secret_word, letters_guessed))

            print("-" * 13)
            continue
        elif letter in letters_guessed and warnings_remaining == 0:
            print(f"You already guessed that letter! You have {warnings_remaining} warnings: ",
                  get_guessed_word(secret_word, letters_guessed))

            guess_remaining -= 1

            print("-" * 13)
            continue

        letters_guessed.append(letter)

        if letter in secret_word:
            print("Good guess:", get_guessed_word(
                secret_word, letters_guessed))
        else:
            print("Oops! That letter is not in my word:",
                  get_guessed_word(secret_word, letters_guessed))

            # If the letter is a vowel, the user loses two guesses.
            if letter in "aeiou":
                guess_remaining -= 2
            else:
                guess_remaining -= 1

        print("-" * 13)

        if secret_word == get_guessed_word(secret_word, letters_guessed):
            print("Congratulations, you won!")
            print("Your total score for this game is:",
                  guess_remaining * len(letters_guessed))
            break
    else:
        print("I'm sorry, you ran out of guesses.")
        print("The word was:", secret_word)


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.

if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

    ###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
