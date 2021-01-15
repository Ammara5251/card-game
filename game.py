from random import shuffle

class Card(object):
    """
    Args:
        Suit & Value of card.
    """
    suits = {
        "Spades": 1,
        "Diamonds": 2,
        "Hearts": 3,
        "Clubs": 4,
    }

    values = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "JACK": 11,
        "QUEEN": 12,
        "KING": 13,
        "ACE": 1,
    }

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        """
        String representation of card.
        """
        return f"{self.value} of {self.suit}"


class Deck(object):
    def __init__(self):
        self.cards = []
        self.sorted = []
        self.build()


    def build(self):
        for s in Card.suits.keys():
            for v in Card.values.keys():
                self.cards.append(Card(s, v))

    def __str__(self):
        """
        String representation of Deck list.
        """
        return str(self.cards)

    def shuffle(self):
        """
        Shuffle the deck of cards.
        """
        shuffle(self.cards)

    def drawCard(self):
        """
        Draw the card from deck.
        
        Returns:
            The drawn card from deck.
        Raises:
            Exception: If there is no card left in the deck.
        """
        try:
            return self.cards.pop()
        except IndexError:
            raise Exception("The Deck is Empty") from None

    def sort(self):
        """
        Sort the deck of cards.
        """
        for s in Card.suits.keys():
            for v in Card.values.keys():
                self.sorted.append(Card(s, v))


class Player(object):
    """
    Player Class

    Args: Name of Player
    """
    def __init__(self, name="Anonymous"):
        self._name = name
        self.hand = []
        self.score = 0

    @property
    def name(self):
        """Name of Player"""
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def draw(self, deck):
        """
        Draw a card from top of deck.
        """
        self.hand.append(deck.drawCard())
        return self

    def showHand(self):
        """
        Show Hand of player.
        """
        for card in self.hand:
            print(card)

    def cal(self):
        """
        Calculate total score of player.

        Returns:
            Total score of the player.
        """
        for card in self.hand:
            self.score += Card.suits.get(card.suit) * Card.values.get(card.value)
        return self.score

    @staticmethod
    def determine_winner(obj, obj1):
        """Determine Winner based on Score"""
        if obj.cal() > obj1.cal():
            print(f"\n{obj.name} is Winner")
        elif obj.cal() < obj1.cal():
            print(f"\n{obj1.name} is Winner")
        else:
            print("\nThere is a Tie")

if __name__ == '__main__':
    deck = Deck()
    deck.sort()

    deck.shuffle()

    player1 = Player("Player 1")
    player2 = Player("Player 2")

    for _ in range(3):
        player1.draw(deck)
        player2.draw(deck)

    print(f"\n{player1.name}'s Hand-----\n")
    player1.showHand()
    print(f"Score: {player1.cal()}")
    print(f"\n{player2.name}'s Hand-----\n")
    player2.showHand()
    print(f"Score: {player2.cal()}")

    Player.determine_winner(player1, player2)
