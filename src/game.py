import random
from src.words import get_word_list
from src.utils import display_hangman

def play():
    word_list = get_word_list()  # Get the list of words
    word = random.choice(word_list).upper()  # Randomly choose a word and convert it to uppercase
    word_completion = '_' * len(word)  # Create the initial word display with underscores
    guessed = False  # Flag to track if the word has been guessed
    guessed_letters = []  # List to store guessed letters
    guessed_words = []  # List to store guessed words
    tries = 6  # Number of tries the player has

    print('Let\'s play Hangman!')
    print(display_hangman(tries))  # Display initial hangman state
    print(word_completion)  # Display the word with underscores
    print('\n')

    while not guessed and tries > 0:
        guess = input('Please guess a letter or word: ').upper()  # Get the player's guess and convert it to uppercase
        if len(guess) == 1 and guess.isalpha():  # Check if the guess is a single letter
            if guess in guessed_letters:  # Check if the letter was already guessed
                print('You already guessed the letter', guess)
            elif guess not in word:  # Check if the guess is incorrect
                print(guess, 'is not in the word.')
                tries -= 1  # Decrease the number of tries
                guessed_letters.append(guess)  # Add the letter to the list of guessed letters
            else:
                print('Good job,', guess, 'is in the word!')
                guessed_letters.append(guess)  # Add the correct guess to the list
                word_as_list = list(word_completion)  # Convert the word display to a list
                indices = [i for i, letter in enumerate(word) if letter == guess]  # Find all indices of the guessed letter
                for index in indices:
                    word_as_list[index] = guess  # Reveal the guessed letter in the word display
                word_completion = ''.join(word_as_list)  # Convert the list back to a string
                if '_' not in word_completion:  # Check if the word has been completely guessed
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():  # Check if the guess is the whole word
            if guess in guessed_words:  # Check if the word was already guessed
                print('You already guessed the word', guess)
            elif guess != word:  # Check if the guess is incorrect
                print(guess, 'is not the word.')
                tries -= 1  # Decrease the number of tries
                guessed_words.append(guess)  # Add the word to the list of guessed words
            else:
                guessed = True  # The word is guessed correctly
                word_completion = word
        else:
            print('Not a valid guess.')  # Handle invalid guesses
        print(display_hangman(tries))  # Display the current hangman state
        print(word_completion)  # Display the current state of the word
        print('\n')

    if guessed:
        print('Congratulations, you guessed the word! You win!')  # The player wins
    else:
        print('Sorry, you ran out of tries. The word was ' + word + '. Maybe next time!')  # The player loses

if __name__ == '__main__':
    play()  # Start the game
