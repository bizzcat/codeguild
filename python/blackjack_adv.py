# Winning
#
# The goal is to be the closest player to 21 points in your hand without going over.
#
# Play
#
# Two cards are dealt to the player and the dealer.
#
# The player goes first. They can "hit" and get a new random card from the deck to
# increase the points in their hand. If you hit and go over 21, you're out. They
# can also "stand" and keep their current hand and end their turn.
#
# Then the dealer plays identically. The computer dealer will decide to hit if
# their current hand is less than 17 points; they will stand otherwise.
#
# Step-by-Step
#
# Copy your blackjack hand scoring code.
# Make a class that represents a deck.
# Ensure that a deck is initialized with all of the cards.
# Add a function that removes and returns a random card from the deck.
# Implement the play above: The user can decide whether to hit or stay. The
# computer will play according to the dealer rules above.
# Advanced
#
# Allow multiple hands to be played with the same deck.
# Add a "card counting assistant". When given the option to draw another card,
# print out the probability that your next card will keep you under 21.


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import os
import time
import random

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Card:
    def __init__(self, name, suit):
        self.name = name
        self.suit = suit
    def __str__(self):
        return "Card({} of {})".format(self.name, self.suit)
    def assign_points_to_card(self, user_hand, comp_hand):
        if user_score > 21:
            for card in user_hand.hand:
                if card.name == 'Ace':
                    print('\n\n{:^95}'.format("Switching user's Ace card value from 11 to 1 to save user's ass"))
                    **card.value** = 1
                    **user_score = sum([card.value*** for card in user_hand.hand])


class Hand:
    def __init__(self, hand):
        self.hand = hand
    def __str__(self):
        return "Hand({})".format(self.hand)
    def assign_score_to_hand(self):


class Deck:
    def __init__(self, cards):
        self.cards = cards
    def __str__(self):
        return "Deck({})".format(self.cards)
    def draw_from_deck(self):
        current_card = random.choice(self.cards)
        (self.cards).remove(current_card)
        return current_card

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

card_names = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
card_suits = ['Spades', 'Diamonds', 'Clubs', 'Hearts']

def initialize_all_cards_and_deck(card_suits, card_names):
    cards_in_deck = []
    for suit in card_suits:
        for name in card_names:
            cards_in_deck.append(Card(name, suit))
    deck = Deck(cards_in_deck)
    return deck

deck = initialize_all_cards_and_deck(card_suits, card_names)
for card in deck.cards: print(card)
input('')

current_card = draw_from_deck()
user_hand = update_user_hand(current_card)




def update_user_hand(current_user_card):
    user_hand_list.append(current_user_card)
    user_hand = Hand(user_hand_list)
    return user_hand
def update_comp_hand(current_comp_card):
    comp_hand_list.append(current_comp_card)
    comp_hand = Hand(comp_hand_list)
    return comp_hand
def display_scoreboard(user_hand, comp_hand, current_user_card, current_comp_card):
    os.system('clear')
    length_of_deck = str(len(deck.cards))
    user_card_names = [card.name for card in user_hand.hand]
    comp_card_names = [card.name for card in comp_hand.hand]

    user_score = str(sum([card.value for card in user_hand.hand]))
    comp_score = str(sum([card.value for card in comp_hand.hand]))

    user_card_names_printable = '   '.join(user_card_names) + '     <<<   USER '
    user_score_printable = user_score + '        <<<   USER '

    comp_card_names_printable = ' COMP   >>>     ' + '   '.join(comp_card_names)
    comp_score_printable = ' COMP   >>>        ' + comp_score

    print ("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Cards left in deck: {}\n\n\n{:^94}".format(length_of_deck, 'HANDS'))
    print("{:^45}     {:^45}".format(user_card_names_printable, comp_card_names_printable))
    print("\n\n{:^95}".format('SCORES'))
    print("{:^45}     {:^45}".format(user_score_printable, comp_score_printable))
    print ("\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print('\n{:^95}'.format("Your draw:  {} of {}, worth {} points".format(current_user_card.name, current_user_card.suit, current_user_card.value)))
    print('\n{:^95}'.format("Computer's draw:  {} of {}, worth {} points".format(current_comp_card.name, current_comp_card.suit, current_comp_card.value)))
    print ("\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    time.sleep(0.3)

def user_hit_or_stand(user_hand):
    user_score = sum([card.value for card in user_hand.hand])
    if user_score > 21:
        for card in user_hand.hand:
            if card.name == 'Ace':
                print('\n\n{:^95}'.format("Switching user's Ace card value from 11 to 1 to save user's ass"))
                card.value = 1
                user_score = sum([card.value for card in user_hand.hand])
    if user_score > 21:
        print('{:^95}'.format("User has exceeded 21 points and is being discharged from the game"))
        return False
    if user_score <= 21:
        print('{:^95}'.format('enter H to hit again               enter S to stand   '))
        choice = input('{:<46} '.format('                                      > > >  '))
        return choice == 'H'
def comp_hit_or_stand(comp_hand):
    comp_score = sum([card.value for card in comp_hand.hand])
    if comp_score > 21:
        for card in comp_hand.hand:
            if card.name == 'Ace':
                print('{:^95}'.format("\n\nSwitching user's Ace card value from 11 to 1 to save user's ass"))
                card.value = 1
                comp_score = sum([card.value for card in comp_hand.hand])
    if comp_score > 21:
        print('{:^95}'.format("Computer has exceeded 21 points and is being discharged from the game"))
        return False
    if comp_score >= 17: return False
    else: return True

def identify_winner(user_hand, comp_hand):
    user_score = sum([card.value for card in user_hand.hand])
    comp_score = sum([card.value for card in comp_hand.hand])
    if comp_score <= 21 and user_score <= 21:
        user_margin_of_victory = 21 - user_score
        comp_margin_of_victory = 21 - comp_score
        if user_margin_of_victory < comp_margin_of_victory: winner = 'User wins by strategy!'
        if user_margin_of_victory > comp_margin_of_victory: winner = 'Computer wins by strategy!'
    elif comp_score > 21:
        winner = 'User wins because computer went over 21!'
    elif user_score > 21:
        winner = 'Computer wins because user went over 21!'
    return winner



#~~~~~
card_names = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
card_suits = ['Spades', 'Diamonds', 'Clubs', 'Hearts']

user_hand_list = []
comp_hand_list = []
current_user_card = Card('Joker', 'Platinum', 0)
current_comp_card = Card('Joker', 'Platinum', 0)
user_hand = Hand([current_user_card])
comp_hand = Hand([current_comp_card])

deck = initialize_all_cards_and_deck(card_suits, card_names)

os.system('clear')
input('{:^95}\n{:>47}'.format('Press ENTER to begin', ''))
cont = True
while cont:
    display_scoreboard(user_hand, comp_hand, current_user_card, current_comp_card)
    current_user_card = deck.draw_from_deck()
    user_hand = update_user_hand(current_user_card)

    current_comp_card = deck.draw_from_deck()
    comp_hand = update_comp_hand(current_comp_card)
    input('\n\n{:^95}\n{:>47}'.format('Press ENTER to continue', ''))

    display_scoreboard(user_hand, comp_hand, current_user_card, current_comp_card)

    user_cont = user_hit_or_stand(user_hand)
    comp_cont = comp_hit_or_stand(comp_hand)

    while user_cont == True and comp_cont == False:
        display_scoreboard(user_hand, comp_hand, current_user_card, current_comp_card)
        current_user_card = deck.draw_from_deck()
        user_hand = update_user_hand(current_user_card)
        user_cont = user_hit_or_stand(user_hand)

    while user_cont == False and comp_cont == True:
        display_scoreboard(user_hand, comp_hand, current_user_card, current_comp_card)
        current_comp_card = deck.draw_from_deck()
        comp_hand = update_comp_hand(current_comp_card)
        input('{:^95}\n{:>47}'.format('Press ENTER to continue', ''))
        comp_cont = comp_hit_or_stand(comp_hand)

    if user_cont == False and comp_cont == False:
        input('{:^95}\n{:>47}'.format('Press ENTER to reveal winner', ''))
        winner = identify_winner(user_hand, comp_hand)
        print('{:^95}'.format(winner))
        cont = False

input('\n\n{:^95}\n{:>47}'.format('Press ENTER to close application', ''))


























# number of cards left in deck: str(len(deck.cards))
















    #
