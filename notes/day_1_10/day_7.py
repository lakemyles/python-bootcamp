# Hangman Console Game
import random

title_art = '''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
'''

hangman_images = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

def display_hangman(user_number_of_guesses):
    print(hangman_images[user_number_of_guesses])

def get_user_guess():
    return input("Guess a letter: ").lower()

def display_word_progress(random_word, guessed_letters):
    progress_display = ""
    
    for char in random_word:
        if char in guessed_letters:
            progress_display += char
        else:
            progress_display += "_"

    print(progress_display)

def check_user_answer(random_word, guessed_letters):
    is_solved = True
    
    for char in random_word:
        if char not in guessed_letters:
            is_solved = False
        
    return is_solved

random_word = random.choice(words)
guessed_letters = []
total_number_of_guesses = 6
user_number_of_guesses = 0
hasUserWon = False

print(title_art)
display_hangman(user_number_of_guesses)
display_word_progress(random_word, guessed_letters)

while user_number_of_guesses < total_number_of_guesses and not hasUserWon:
    user_guess = get_user_guess()

    if user_guess in random_word:
        guessed_letters.append(user_guess)
        hasUserWon = check_user_answer(random_word, guessed_letters)
    else:
        user_number_of_guesses += 1
        
    display_hangman(user_number_of_guesses)
    display_word_progress(random_word, guessed_letters)

print("\nGAME OVER")

if hasUserWon:
    print("You won!")
else:
    print("Better luck next time!")











