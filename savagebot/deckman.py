"""
author: Alex Sutay
file: deckman.py
"""

from dataclasses import dataclass
import random

@dataclass
class Card:
    """Class for building a card"""
    number: int
    suit: str
    path: str


def read_deck(filename):
    """
    reads the file given by filename and
    returns a list of the cards in order.
    """
    with open(filename) as cardfile:
        cards = cardfile.readlines()
    for i in range(0,len(cards)):
        cards[i] = make_card(cards[i])
    return cards


def make_card(cardstr):
    """
    This returns a "card" class item given 
    a string (cardstr) in the format:
    "number suit path"
    """
    cardstr = cardstr.strip()
    cardstr = cardstr.split(' ')
    return Card(int(cardstr[0]), cardstr[1], cardstr[2])


def write_deck(deck, filename):
    """
    given deck as a list containing card class items
    this function writes out to the given filename
    in the format "number suit path"
    """
    writestr = ''
    for card in deck:
        writestr += str(card.number) + ' ' + card.suit + ' ' + card.path + '\n'
    with open(filename, 'w') as cardfile:
        cardfile.write(writestr[:-1])


def new_deck(filename):
    """
    This function makes a new deck, shuffles it, and 
    writes it out to filename
    """
    deck = []
    for suit in ["Spades", "Hearts", "Clubs", "Diamonds"]:
        for num in range(1,14):
            path = 'cards/' + str(num) + suit[0] + '.png'
            deck.append(Card(num, suit, path))
    deck.append(Card(0, "Joker", 'cards/joker.png'))
    deck.append(Card(0, "Joker", 'cards/joker.png'))
    random.shuffle(deck)
    write_deck(deck, filename)


def draw_card(filename):
    """
    This function removes the bottom card from the file 
    filename and returns a Card class item of that card
    """
    deck = read_deck(filename)
    new_card = deck[-1]
    deck = deck[:-1]
    write_deck(deck, filename)
    return new_card
