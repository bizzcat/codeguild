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
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return "Card({})".format(self.name, self.value)

class Hand:
    def __init__(self, hand):
        self.hand = hand
    def __str__(self):
        return "Hand({})".format(hand)

# c2 = Card('two', 2)
# print(c2.value)

def get_card_selection():
    print('\n\nCurrent hand:  {}\n\nSelect a card to add to your deck:\nAces are worth either 1 or 11 points, face cards are all 10 points each\n\n2 3 4 5 6 7 8 9 10\nJ Q K A\n\n'.format(cards_in_hand))
    user_card_selection = input('  > > >  ').upper()
    if user_card_selection == 'J':
        user_card_selection = 10
    if user_card_selection == 'Q':
        user_card_selection = 10
    if user_card_selection == 'K':
        user_card_selection = 10
    if user_card_selection == 'A':
        user_card_selection = 1 or 11
    user_card_selection = str(user_card_selection)
    return user_card_selection

def add_card_to_hand(cards_in_hand, user_card_selection):
    cards_in_hand.append(Card(user_card_selection))
    return cards_in_hand

def get_score_from_hand(cards_in_hand):
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
    user_card_selection = get_card_selection()
    cards_in_hand = add_card_to_hand(cards_in_hand, user_card_selection)
    current_score = get_score_from_hand(cards_in_hand)
    cont = return_score_if_over_21(cont, current_score)



#
# def get_user_card_selection():
#     print('Card options (type only with spaces):\n2 3 4 5 6 7 8 9 10\nJ Q K A\n\nAces are worth either 1 or 11 points, face cards are all 10 points each\n\n\n')
#     user_card_selection = input('  > > >  ').upper()
#     user_card_selection = ('c' + user_card_selection)
#     return user_card_selection














#
