# Functions with inputs

import math

# def greet(name):
#     print(f"Hello {name}")


# def calculate_paint_needed(height, width, coverage_per_can):
#     area = height * width
#     return int(math.ceil(area / coverage_per_can))


# def prime_checker(number):
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#     if is_prime:
#         print("It is prime.")
#     else:
#         print("It is not prime.")


# number = int(input("Check this number: "))
# prime_checker(number)

# Caesar Cipher
def get_new_letter(letter, shift):
    alphabet_index = alphabet.index(letter)
    encrypted_index = alphabet_index + shift
    if encrypted_index > 26 or encrypted_index < 1:
        encrypted_index = encrypted_index % 26
    return alphabet[encrypted_index]


def caesar(start_text, shift, cipher_direction):
    if cipher_direction == "decrypt":
        shift *= -1
    end_text = ""
    for char in start_text:
        if char in alphabet:
            end_text += get_new_letter(char, shift)
        else:
            end_text += char
    print(f"The {cipher_direction}ed is {end_text}\n")


alphabet = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
direction = input(
    "Type 'encrypt' to encrypt or type 'decrypt' to decrypt.\nPress any other key to exit:\n").lower()
do_continue = True if direction == "encrypt" or direction == "decrypt" else False

while do_continue:
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)

    direction = input(
        "Type 'encrypt' to encrypt or type 'decrypt' to decrypt.\nPress any other key to exit:\n").lower()
    do_continue = True if direction == "encrypt" or direction == "decrypt" else False
