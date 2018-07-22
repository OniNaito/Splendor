# Creating the Splendor Deck
import random


class CardDeck:

    deck = []

    def __init__(self):
        self.deck = []

    def buildDeck(self, level):
        for lvl in Card.levels:
            if level == lvl:
                for color in Card.colors:
                    for c in range(Card.levels[level]):
                        newcard = Card()
                        newcard.color = color
                        newcard.genCosts(2)
                        newcard.points = 0
                        newcard.level = level

                        self.deck.append(newcard)
        return self.deck



    def showCard(self, card):
        print(card.level, "level card of color", card.color, "worth", card.points, "points costing", card.cost)

    def showRandomCard(self):
        print(len(self.deck))
        randomcard = random.randint(0, len(self.deck) - 1)
        card = self.deck[randomcard]
        self.showCard(card)

    def showDeck(self):
        for card in self.deck:
            self.showCard(card)

    def shuffleDeck(self):
        random.shuffle(self.deck)

    def dealCard(self):
        card = self.deck[0]
        self.showCard(card)
        self.deck.remove(card)


class Card:

    colors = ('Diamond', 'Sapphire', 'Emerald', 'Ruby', 'Onyx')
    levels = {"Green": 8, "Yellow": 6, "Blue": 4}
    costTypes = {'4costShift1': 'Whatever I am, set cost to 4 of the next color in the list'}

    def __init__(self): # , color, cost, points=0, level="Green"):
        self.color = 'Diamond'
        self.cost = []
        self.points = 0
        self.level = 'Green'

        for color in Card.colors:
            cost = [color, 0]
            self.cost.append(cost)

    def genCosts(self, shift, costPool = 4):
        for color in Card.colors:
            if self.color == color:
                for cost in self.cost:
                    if cost[0] == color:
                        currindex = Card.colors.index(color)
                newIndex = currindex + shift
                if newIndex >= len(self.cost):
                    newIndex -= len(self.cost)
                self.cost[newIndex] = [Card.colors[newIndex], 4]



allDecks = []
for level in Card.levels:
    x = CardDeck()
    x.buildDeck(level)
    allDecks.append(x)
# myDeck.showRandomCard()

for deck in allDecks:
    deck.showDeck()

    #     shuffleDeck()
    # for card in range(4):
    #     CardDeck.dealCard(deck)
