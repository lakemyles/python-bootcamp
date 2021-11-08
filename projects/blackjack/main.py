import os
import blackjack_art
import blackjack


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(blackjack_art.title)
    print("\n")


def get_user_input(question):
    user_input = input(question)
    if(user_input.lower() == 'y'):
        return True


def display_game_status():
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {dealer_cards[0]}\n")


def display_game_results():
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(
        f"Computer's final hand: {dealer_cards}, final score: {dealer_score}\n")


new_game_question = "Do you want to play a game of Blackjack? Type 'y' or 'n': "
another_card_question = "Type 'y' to get another card, type 'n' to pass: "
user_cards = []
dealer_cards = []
user_score = 0
dealer_score = 0

clear_screen()
do_continue = get_user_input(new_game_question)

while do_continue:
    clear_screen()
    deck = blackjack.start_new_game()
    user_cards.clear()
    dealer_cards.clear()

    for _ in range(2):
        user_cards.append(blackjack.deal_card(deck))
        dealer_cards.append(blackjack.deal_card(deck))

    user_score = blackjack.get_cards_score(user_cards)
    display_game_status()

    hit_user = get_user_input(another_card_question)
    while hit_user:
        clear_screen()
        user_cards.append(blackjack.deal_card(deck))
        user_score = blackjack.get_cards_score(user_cards)
        display_game_status()
        if user_score < 21:
            hit_user = get_user_input(another_card_question)
        else:
            hit_user = False

    game_result = "You Lose"

    if user_score <= 21:
        dealer_score = blackjack.get_cards_score(dealer_cards)
        while dealer_score < 17 or user_score > dealer_score:
            dealer_cards.append(blackjack.deal_card(deck))
            dealer_score = blackjack.get_cards_score(dealer_cards)

        if dealer_score > 21:
            game_result = "You Win"

        if dealer_score == user_score:
            game_result = "Draw"

    clear_screen()
    display_game_results()
    print(f"{game_result}\n")

    do_continue = get_user_input(new_game_question)
