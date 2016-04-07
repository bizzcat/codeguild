# func for a card
# func for a hand
# func for a deck

# Implement scoring a single hand of blackjack.
#
# Cards have point values. Aces are 1 or 11, number cards are their number,
# face cards are all 10. A hand is worth the sum of all the points of the cards
# in it. An ace is worth 1 when the hand it's a part of would be over 21 if it
# was worth 11.
#
# Make a class that represents a card.
# Make a class that represents a hand.
# Add functions that adds a card to a hand, one that scores a hand, and one that
# returns if the score is over 21.
# Allow a user to type in a hand and have it be converted into card objects and
# then scored.
# While you're working, use arbitrary cards that you enter. Don't worry about
# modeling a deck yet.


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
    print('\n\nCurrent hand:  {}\n\nSelect a card to add to your deck:\nAces are worth either 1 or 11 points, face cards are all 10 points each\n\ntwo three four five six seveb eight nine ten\nJ Q K A\n\n'.format(cards_in_hand))
    user_card_name = input('  > > >  ').upper()
    print("{} of spades, diamonds, clubs or hearts?")
    user_card_suit = input('  > > >  ').upper()
    if user_card_name == 'two':
        user_card_value = 2
    if user_card_name == 'three':
        user_card_value = 3
    if user_card_name == 'four':
        user_card_value = 4
    if user_card_name == 'five':
        user_card_value = 5
    if user_card_name == 'six':
        user_card_value = 6
    if user_card_name == 'seven':
        user_card_value = 7
    if user_card_name == 'eight':
        user_card_value = 8
    if user_card_name == 'nine':
        user_card_value = 9
    if user_card_name == 'ten':
        user_card_value = 10
    if user_card_name in ['J', 'Q', 'K']:
        user_card_value = 10
    if user_card_name == 'A':
        user_card_value = 11
    user_card_value = int(user_card_name)
    current_card = Card(user_card_name, user_card_suit, user_card_value)
    return current_card

# default_card = {'name': 'Jack', 'suit': 'Clubs', 'value': 10}

cards_in_hand = []

def add_card_to_hand(cards_in_hand, current_card):
    cards_in_hand.append(current_card.name)
    current_hand = Hand(cards_in_hand)
    return current_hand

def get_score_from_hand(current_hand):
    current_hand = Hand(cards_in_hand)
    current_hand_value = []
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

cards_in_hand = []
cont = True
while cont:
    # user_card_name = get_card_selection()
    current_hand = add_card_to_hand(cards_in_hand, default_card)
    for card in current_hand.hand:
        print(card)
    input('')
    current_score = get_score_from_hand(cards_in_hand)
    cont = return_score_if_over_21(cont, current_score)

smbfdjhdb

#
# def get_user_card_name():
#     print('Card options (type only with spaces):\n2 3 4 5 6 7 8 9 10\nJ Q K A\n\nAces are worth either 1 or 11 points, face cards are all 10 points each\n\n\n')
#     user_card_name = input('  > > >  ').upper()
#     user_card_name = ('c' + user_card_name)
#     return user_card_name














#
