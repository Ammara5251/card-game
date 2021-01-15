import unittest
from game import Deck

class DeckClassTestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(DeckClassTestCase, self).__init__(*args, **kwargs)
        self.deck = Deck()

    def test_no_of_cards_in_deck(self):
        self.assertEqual(len(self.deck.cards), 52, "Should be 53 cards")

    def test_pop_exception(self):
        with self.assertRaises(Exception):
            for _ in range(53):
                self.deck.drawCard()



if __name__ == '__main__':
    unittest.main()