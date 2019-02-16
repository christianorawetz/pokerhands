import collections

from utils import same_suit, sort_cards, all_consecutive, get_rank_values

CARD_RANK_VALUES = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
}

CARD_SUITS = ('H', 'D', 'C', 'S')


def royal_flush(hand):
    ranks = sorted([card.rank_value for card in hand.cards], reverse=True)

    return ranks if same_suit(hand.cards) and ranks == [14, 13, 12, 11, 10] else []


def straight_flush(hand):
    ranks = sorted(hand.get_rank_values(), reverse=True)

    return ranks if same_suit(hand.cards) and all_consecutive(ranks) else []


def four_of_a_kind(hand):
    counter = collections.Counter(hand.get_rank_values())

    return 4 * [rank for rank, count in counter.most_common(1) if count == 4]


def full_house(hand):
    counter = collections.Counter(hand.get_rank_values())

    three_of_kind = 3 * [rank for rank, count in counter.most_common(2) if count == 3]
    two_of_kind = 2 * [rank for rank, count in counter.most_common(2) if count == 2]

    return three_of_kind + two_of_kind if any(three_of_kind) and any(two_of_kind) else []


def flush(hand):
    return sorted(hand.get_rank_values(), reverse=True) if same_suit(hand.cards) else []


def straight(hand):
    ranks = sorted(hand.get_rank_values(), reverse=True)

    return ranks if all_consecutive(ranks) else []


def three_of_a_kind(hand):
    counter = collections.Counter(hand.get_rank_values())

    return 3 * [rank for rank, count in counter.most_common(1) if count == 3]


def two_pairs(hand):
    counter = collections.Counter(hand.get_rank_values())

    pairs = [rank for rank, count in counter.most_common(2) if count == 2]

    return sorted(2 * pairs, reverse=True) if len(pairs) == 2 else []


def one_pair(hand):
    counter = collections.Counter(hand.get_rank_values())

    return 2 * [rank for rank, count in counter.most_common(1) if count == 2]


def high_card(hand):
    return sorted(hand.get_rank_values(), reverse=True)


POKER_HANDS = [
    high_card,
    one_pair,
    two_pairs,
    three_of_a_kind,
    straight,
    flush,
    full_house,
    four_of_a_kind,
    straight_flush,
    royal_flush
]

