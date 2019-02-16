import unittest

from parse import parse_hands
from rules import royal_flush, straight_flush, four_of_a_kind, full_house, flush, straight, three_of_a_kind, two_pairs, \
    one_pair


class TestPokerRules(unittest.TestCase):
    def test_royal_flush(self):
        player_1_hand, player_2_hand = parse_hands("TH JH QH KH AH QC TC 6D 7C KS")

        rank_scores = royal_flush(player_1_hand)

        self.assertEqual([14, 13, 12, 11, 10], rank_scores)

    def test_straight_flush(self):
        player_1_hand, player_2_hand = parse_hands("2H 3H 4H 5H 6H QC TC 6D 7C KS")

        rank_scores = straight_flush(player_1_hand)

        self.assertEqual([6, 5, 4, 3, 2], rank_scores)

    def test_four_of_a_kind(self):
        player_1_hand, player_2_hand = parse_hands("2H 2D 2C 2S 6H QC TC 6D 7C KS")

        rank_scores = four_of_a_kind(player_1_hand)

        self.assertEqual([2, 2, 2, 2], rank_scores)

    def test_full_house(self):
        player_1_hand, player_2_hand = parse_hands("2H 2D 2C 3S 3H QC TC 6D 7C KS")

        rank_scores = full_house(player_1_hand)

        self.assertEqual([2, 2, 2, 3, 3], rank_scores)

    def test_flush(self):
        player_1_hand, player_2_hand = parse_hands("2H 3H JH 6H AH QC TC 6D 7C KS")

        rank_scores = flush(player_1_hand)

        self.assertEqual([14, 11, 6, 3, 2], rank_scores)

    def test_straight(self):
        player_1_hand, player_2_hand = parse_hands("2H 3H 4D 5C 6S QC TC 6D 7C KS")

        rank_scores = straight(player_1_hand)

        self.assertEqual([6, 5, 4, 3, 2], rank_scores)

    def test_three_of_a_kind(self):
        player_1_hand, player_2_hand = parse_hands("6H 2D 2S 2C 6S QC TC 6D 7C KS")

        rank_scores = three_of_a_kind(player_1_hand)

        self.assertEqual([2, 2, 2], rank_scores)

    def test_test_two_pairs(self):
        player_1_hand, player_2_hand = parse_hands("6H 2D 8S 2C 6S QC TC 6D 7C KS")

        rank_scores = two_pairs(player_1_hand)

        self.assertEqual([6, 6, 2, 2], rank_scores)

    def test_one_pair(self):
        player_1_hand, player_2_hand = parse_hands("8H 2D 8S 3C 6S QC TC 6D 7C KS")

        rank_scores = one_pair(player_1_hand)

        self.assertEqual([8, 8], rank_scores)

