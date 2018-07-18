# Creating a 52 Card Deck as a base for the Splendor deck
import random


class CardDeck:

    deck = []

    def __init__(self):
        self.deck = []

    def buildDeck(self):
        for suit in Card.suits:
            for face in Card.faces:
                newcard = Card(face, suit)
                self.deck.append(newcard)
                # print("new card added")
        return self.deck

    def showRandomCard(self):
        randomcard = random.randint(0, 51)
        print("cool")
        print(self.deck[randomcard].face, "of", self.deck[randomcard].suit + "s")
        print("neat")

    def showDeck(self):
        for card in self.deck:
            print(card.face, "of", card.suit + "s")

    def shuffleDeck(self):
        random.shuffle(self.deck)


class Card:

    def __init__(self, face, suit):
        self.face = face
        self.suit = suit

    faces = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')
    suits = ("Spade", "Diamond", "Heart", "Club")


myDeck = CardDeck()
myDeck.buildDeck()
myDeck.showRandomCard()
myDeck.shuffleDeck()
myDeck.showDeck()
