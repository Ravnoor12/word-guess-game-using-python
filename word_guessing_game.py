import random

LEXICON_FILE = "Lexicon-2.txt"  # File to read word list from
INITIAL_GUESSES = 10  # Initial number of guesses player starts with


def update_word(guessed_letter, secret_word, print_underscore):
    index = 0
    letter = guessed_letter.upper()
    while index < len(secret_word):
        if letter == secret_word[index]:
            print_underscore[index] = letter
        index += 1
    return print_underscore


def play_game(secret_word):
    guess_limit = INITIAL_GUESSES
    word_length = len(secret_word)
    print_underscore = list("")
    check = "_"
    for i in range(1, word_length):
        print_underscore += "_"
    print("The word now looks like: " + str(print_underscore))
    print("You have " + str(INITIAL_GUESSES) + " guesses left")
    while guess_limit > 0:
        guess_letter = str(input('Type a single letter here, then press enter: '))
        letter = guess_letter.upper()
        print_underscore = update_word(guess_letter, secret_word, print_underscore)
        if letter in secret_word:
            print("That guess is correct.")
        else:
            print("There are no " + str(guess_letter) + "'s in the word")
            guess_limit -= 1
        print("The word now looks like this: " + str(print_underscore))
        print("You have " + str(guess_limit) + " guesses left")
        if "_" not in print_underscore:
            print("Congratulations, the word is: " + str(secret_word))
            break
    if guess_limit == 0:
        print("Sorry, you lost. The secret word was: " + str(secret_word))


def get_word():
    f = open(LEXICON_FILE)
    word_list = ["KAREL"]
    for line in f:
        word_list.append(line)

    """
    This function returns a secret word that the player is trying
    to guess in the game.  This function initially has a very small
    list of words that it can select from to make it easier for you
    to write and debug the main game playing program.  In Part II of
    writing this program, you will re-implement this function to
    select a word from a much larger list by reading a list of words
    from the file specified by the constant LEXICON_FILE.
    """
    index = random.randint(0, len(word_list))
    # index = random.randrange(3)
    return word_list[index]




def main():
    secret_word = get_word()
    play_game(secret_word)

if __name__ == "__main__":
    main()