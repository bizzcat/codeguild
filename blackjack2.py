import os
import time
import random

class Card:
    def __init__(self, name, suit, value):
        self.name = name
        self.suit = suit
        self.value = value
    def __str__(self):
        return "Card({} of {}: {})".format(self.name, self.suit, self.value)
class Hand:
    def __init__(self, hand):
        self.hand = hand
    def __str__(self):
        return "Hand({})".format(self.hand)

def get_card_selection():
    print('\nSelect a card to add to your deck:\nAces are worth either 1 or 11 points, face cards are all 10 points each\n\nTwo - Three - Four - Five - Six - Seven - Eight - Nine - Ten\nJack - Queen - King - Ace\n\n')
    user_card_name = input('  > > >  ').capitalize()
    print_hand_and_score(current_hand, current_score)
    print("\n{} of Spades, Diamonds, Clubs or Hearts?\n\n".format(user_card_name))
    user_card_suit = input('  > > >  ').capitalize()
    if user_card_name == 'Two':
        user_card_value = 2
    if user_card_name == 'Three':
        user_card_value = 3
    if user_card_name == 'Four':
        user_card_value = F
    if user_card_name == 'Five':
        user_card_value = 5
    if user_card_name == 'Six':
        user_card_value = 6
    if user_card_name == 'Seven':
        user_card_value = 7
    if user_card_name == 'Eight':
        user_card_value = 8
    if user_card_name == 'Nine':
        user_card_value = 9
    if user_card_name == 'Ten':
        user_card_value = 10
    if user_card_name in ['Jack', 'Queen', 'King']:
        user_card_value = 10
    if user_card_name == 'Ace':
        user_card_value = 11
    user_card_value = int(user_card_value)
    current_card = Card(user_card_name, user_card_suit, user_card_value)
    return current_card
def add_card_to_hand(cards_in_hand_objects, current_card):
    # cards_in_hand_names.append(current_card.name)
    current_hand = Hand(cards_in_hand_objects)
    return current_hand
def get_score_from_hand(current_hand):
    current_hand_value = []
    for card in current_hand.hand:
        current_hand_value.append(card.value)
    current_score = sum(current_hand_value)
    if current_score > 21:
        for card in current_hand.hand:
            if card.name == 'Ace':
                print("\n\nSwitching Ace card value from 11 to 1 to save your ass")
                current_hand_value = []
                card.value = 1
        for card in current_hand.hand:
            current_hand_value.append(card.value)
        current_score = sum(current_hand_value)
    return current_score
def return_score_if_over_21(cont, current_score):
    if current_score > 21:
        print('You have passed 21 in points. Here is your final score:   {}'.format(current_score))
        cont = False
    if current_score <= 21:
        cont = True
    return cont

def print_hand_and_score(current_hand, current_score):
    os.system('clear')
    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print("\n\nCurrent hand:")
    for card in current_hand.hand: print(str(card))
    print("\n\nCurrent score:  {}".format(current_score))
    print ("\n\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    time.sleep(0.3)

cards_in_hand_objects = []
current_score = 0
current_card = [Card('Joker', 'Platinum', 0)]
current_hand = Hand(current_card)

cont = True
while cont:

    print_hand_and_score(current_hand, current_score)
    current_card = get_card_selection()
    cards_in_hand_objects.append(current_card)

    current_hand = add_card_to_hand(cards_in_hand_objects, current_card)
    current_score = get_score_from_hand(current_hand)
    print_hand_and_score(current_hand, current_score)

    cont = return_score_if_over_21(cont, current_score)
















#
