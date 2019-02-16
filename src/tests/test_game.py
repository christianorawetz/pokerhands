import unittest

from game import play
from parse import parse_hands


class TestPokerGame(unittest.TestCase):
    def test_player_1_wins_royal_flush(self):
        player_1_hand, player_2_hand = parse_hands("TH JH QH KH AH QC TC 6D 7C KS")

        player_1_result, player_2_result = play(player_1_hand, player_2_hand)

        self.assertEqual(1, player_1_result)
        self.assertEqual(0, player_2_result)

    def test_player_2_wins_royal_flush(self):
        player_1_hand, player_2_hand = parse_hands("QC TC 6D 7C KS TH JH QH KH AH")

        player_1_result, player_2_result = play(player_1_hand, player_2_hand)

        self.assertEqual(0, player_1_result)
        self.assertEqual(1, player_2_result)

    def test_high_card_player_1(self):
        player_1_hand, player_2_hand = parse_hands("9S TS JS QS KS 8H 9H TH JH QH")

        player_1_result, player_2_result = play(player_1_hand, player_2_hand)

        self.assertEqual(1, player_1_result)
        self.assertEqual(0, player_2_result)

    def test_high_card_player_2(self):
        player_1_hand, player_2_hand = parse_hands("8H 9H TH JH QH 9S TS JS QS KS")

        player_1_result, player_2_result = play(player_1_hand, player_2_hand)

        self.assertEqual(0, player_1_result)
        self.assertEqual(1, player_2_result)

    def test_draw(self):
        player_1_hand, player_2_hand = parse_hands("9S TS JS QS KS 9H TH JH QH KH")

        player_1_result, player_2_result = play(player_1_hand, player_2_hand)

        self.assertEqual(0, player_1_result)
        self.assertEqual(0, player_2_result)

    def test_player_2_wins_pair_of_eights(self):
        player_1_hand, player_2_hand = parse_hands("5H 5C 6S 7S KD 2C 3S 8S 8D TD")

        player_1_result, player_2_result = play(player_1_hand, player_2_hand)

        self.assertEqual(0, player_1_result)
        self.assertEqual(1, player_2_result)

    def test_player_1_wins_highest_card_ace(self):
        player_1_hand, player_2_hand = parse_hands("5D 8C 9S JS AC 2C 5C 7D 8S QH")

        player_1_result, player_2_result = play(player_1_hand, player_2_hand)

        self.assertEqual(1, player_1_result)
        self.assertEqual(0, player_2_result)

    def test_player_2_wins_flush(self):
        player_1_hand, player_2_hand = parse_hands("2D 9C AS AH AC 3D 6D 7D TD QD")

        player_1_result, player_2_result = play(player_1_hand, player_2_hand)

        self.assertEqual(0, player_1_result)
        self.assertEqual(1, player_2_result)

    def test_player_2_wins_highest_card_jack(self):
        player_1_hand, player_2_hand = parse_hands("6D 7C 5D 5H 3S 5C JC 2H 5S 3D")

        player_1_result, player_2_result = play(player_1_hand, player_2_hand)

        self.assertEqual(0, player_1_result)
        self.assertEqual(1, player_2_result)

    def test_player_1_wins_highest_card_nine(self):
        player_1_hand, player_2_hand = parse_hands("4D 6S 9H QH QC 3D 6D 7H QD QS")

        player_1_result, player_2_result = play(player_1_hand, player_2_hand)

        self.assertEqual(1, player_1_result)
        self.assertEqual(0, player_2_result)

    def test_player_1_wins_full_house(self):
        player_1_hand, player_2_hand = parse_hands("2H 2D 4C 4D 4S 3C 3D 3S 9S 9D")

        player_1_result, player_2_result = play(player_1_hand, player_2_hand)

        self.assertEqual(1, player_1_result)
        self.assertEqual(0, player_2_result)
