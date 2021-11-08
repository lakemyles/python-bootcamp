import random

card_value = {
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
    10: 10,
    "J": 10,
    "Q": 10,
    "K": 10,
    "A": 11
}


def get_new_deck_of_cards():
    return [
        2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4,
        5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7,
        8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10,
        'J', 'J', 'J', 'J', 'Q', 'Q', 'Q', 'Q',
        'K', 'K', 'K', 'K', 'A', 'A', 'A', 'A'
    ]


def shuffle_cards(deck_of_cards):
    random.shuffle(deck_of_cards)
    random.shuffle(deck_of_cards)
    random.shuffle(deck_of_cards)


def deal_card(deck_of_cards):
    return deck_of_cards.pop()


def get_cards_score(hand):
    total = 0
    for card in hand:
        total += card_value[card]
    while total > 21 and "A" in hand:
        index = hand.index("A")
        hand[index] = 1
        total = 0
        for card in hand:
            total += card_value[card]
    return total


def start_new_game():
    deck_of_cards = get_new_deck_of_cards()
    shuffle_cards(deck_of_cards)
    return deck_of_cards
