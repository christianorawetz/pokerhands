import unittest

from exceptions import InvalidCard, InvalidPokerHand
from models import Card, PokerHand
from parse import parse_hands


class TestCardMethods(unittest.TestCase):

    def test_valid_suit(self):
        card = Card('Q', 'H')

        self.assertIsNotNone(card)

    def test_invalid_suit(self):
        with self.assertRaises(InvalidCard):
            Card('Q', 'X')

    def test_invalid_rank(self):
        with self.assertRaises(InvalidCard):
            Card('1', 'H')

    def test_get_value(self):
        ace_card = Card('A', 'H')
        two_card = Card('2', 'H')

        self.assertEqual(ace_card.rank_value, 14)
        self.assertEqual(two_card.rank_value, 2)


class TestPokerHandMethods(unittest.TestCase):

    def test_invalid_hand_no_cards(self):
        with self.assertRaises(InvalidPokerHand):
            PokerHand(None)

    def test_invalid_hand_too_many_cards(self):
        cards = [Card('6', 'S'), Card('6', 'H'), Card('6', 'D'), Card('K', 'C'), Card('K', 'H'), Card('A', 'S')]

        with self.assertRaises(InvalidPokerHand):
            PokerHand(cards)

    def test_invalid_hand_too_few_cards(self):
        cards = [Card('6', 'S'), Card('6', 'H'), Card('6', 'D'), Card('K', 'C')]

        with self.assertRaises(InvalidPokerHand):
            PokerHand(cards)

    def test_invalid_hand_duplicate_card(self):
        cards = [Card('6', 'S'), Card('6', 'S'), Card('6', 'D'), Card('K', 'C'), Card('K', 'H')]

        with self.assertRaises(InvalidPokerHand):
            PokerHand(cards)


class TestPokerHandParser(unittest.TestCase):

    def test_valid_input(self):
        player_1_hand, player_2_hand = parse_hands("KH 4H AS JS QS QC TC 6D 7C KS")

        self.assertIn(Card('K', 'H'), player_1_hand.cards)
        self.assertIn(Card('4', 'H'), player_1_hand.cards)
        self.assertIn(Card('A', 'S'), player_1_hand.cards)
        self.assertIn(Card('J', 'S'), player_1_hand.cards)
        self.assertIn(Card('Q', 'S'), player_1_hand.cards)

        self.assertIn(Card('Q', 'C'), player_2_hand.cards)
        self.assertIn(Card('T', 'C'), player_2_hand.cards)
        self.assertIn(Card('6', 'D'), player_2_hand.cards)
        self.assertIn(Card('7', 'C'), player_2_hand.cards)
        self.assertIn(Card('K', 'S'), player_2_hand.cards)

    def test_invalid_input(self):
        with self.assertRaises(InvalidPokerHand):
            parse_hands("KH 4H AS JS QS QC TC 6D 7C KS 2H")

