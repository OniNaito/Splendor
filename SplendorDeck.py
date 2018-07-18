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
                        newcard = Card(color, {'Diamond': random.randint(0, 8), 'Cobalt': random.randint(0, 8),
                                               'Emerald': random.randint(0, 8), 'Sapphire': random.randint(0, 8),
                                               'Ruby': random.randint(0, 8)}, level=level)
                        self.deck.append(newcard)
        return self.deck

    def showCard(self, card):
        print(card.level, "level card of color", card.color, "worth", card.points, "points costing",
              (', '.join(': '.join(str(b) for b in a) for a in card.cost.items())))

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

    def __init__(self, color, cost, points=0, level="Green"):
        self.color = color
        self.cost = cost
        self.points = points
        self.level = level
    colors = ('Diamond', 'Cobalt', 'Emerald', 'Sapphire', 'Ruby')
    levels = {"Green": 8, "Yellow": 6, "Blue": 4}
    costs = {'Diamond': random.randint(0, 8), 'Cobalt': random.randint(0, 8), 'Emerald': random.randint(0, 8),
             'Sapphire': random.randint(0, 8), 'Ruby': random.randint(0, 8)}


allDecks = []
for level in Card.levels:
    x = CardDeck()
    x.buildDeck(level)
    allDecks.append(x)
# myDeck.showRandomCard()

for deck in allDecks:
    deck.shuffleDeck()
    for card in range(4):
        CardDeck.dealCard(deck)
