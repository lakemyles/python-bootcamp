import random
import os
import higher_lower_art
from higher_lower_data import instagram_users


LOGO = higher_lower_art.logo
VS = higher_lower_art.vs


def print_logo():
    print(LOGO)


def print_current_score(user_score):
    if user_score > 0:
        print(f"You're right! Current score: {user_score}")


def print_final_score(user_score):
    print(f"Sorry, that's wrong. Final score: {user_score}")


def print_question(user_a, user_b):
    print(
        f"Compare A: {user_a['name']}, a {user_a['description']}, from {user_a['country']}")
    print(VS)
    print(
        f"Against B: {user_b['name']}, a {user_b['description']}, from {user_b['country']}")


def get_random_instagram_user():
    return random.choice(instagram_users)


def get_user_answer():
    return input("Who has more followers? Type 'A' or 'B': ")


def calculate_highest_followers(follower_count_a, follower_count_b):
    if follower_count_a > follower_count_b:
        return 'A'
    return 'B'


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n")
