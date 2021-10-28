# Hangman Console Game
import random
import hangman_art
import hangman_words


def display_hangman(user_number_of_guesses):
    print(hangman_art.hangman_images[user_number_of_guesses])


def get_user_guess():
    return input("Guess a letter: ").lower()


def display_word_progress(random_word, guessed_letters):
    progress_display = ""

    for char in random_word:
        if char in guessed_letters:
            progress_display += char + " "
        else:
            progress_display += "_ "

    print(progress_display.rstrip().upper())


def check_user_answer(random_word, guessed_letters):
    is_solved = True

    for char in random_word:
        if char not in guessed_letters:
            is_solved = False

    return is_solved
