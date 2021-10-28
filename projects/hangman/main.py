# Hangman Console Game
import random
import hangman_art
from hangman_words import words
import hangman

random_word = random.choice(words)
guessed_letters = []
total_number_of_guesses = 6
user_number_of_guesses = 0
hasUserWon = False

print(hangman_art.title_art)
# hangman.display_hangman(user_number_of_guesses)
hangman.display_word_progress(random_word, guessed_letters)

while user_number_of_guesses < total_number_of_guesses and not hasUserWon:
    user_guess = hangman.get_user_guess()

    if user_guess in random_word:
        guessed_letters.append(user_guess)
        hasUserWon = hangman.check_user_answer(random_word, guessed_letters)
    else:
        user_number_of_guesses += 1

    hangman.display_hangman(user_number_of_guesses)
    hangman.display_word_progress(random_word, guessed_letters)

print("\nGAME OVER")

if hasUserWon:
    print("You won!")
else:
    print("Better luck next time!")
