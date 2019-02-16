from models import Score
from rules import POKER_HANDS


def play(player_1_hand, player_2_hand):
    player_1_score = evaluate_hand(player_1_hand)
    player_2_score = evaluate_hand(player_2_hand)

    if player_1_score > player_2_score:
        return 1, 0
    elif player_1_score < player_2_score:
        return 0, 1
    else:
        return 0, 0


def evaluate_hand(hand):
    """
    Evaluates a hand of cards against the defined poker hands (form highest to lowest) and returns a score.
    """
    for poker_hand in reversed(POKER_HANDS):
        rank_scores = poker_hand(hand)

        if any(rank_scores):
            return Score(hand, POKER_HANDS.index(poker_hand), rank_scores)

