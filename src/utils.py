def sort_cards(cards):
    return sorted(cards, key=lambda card: card.rank_value)


def get_rank_values(cards):
    return [card.rank_value for card in cards]


def same_suit(cards):
    return len(set([card.suit for card in cards])) == 1


def same_rank(cards):
    ranks = [card.rank for card in cards]

    return len(set(ranks)) == 1


def all_consecutive(rank_values):
    rank_values = sorted(rank_values)

    return all(rank_values[i] == rank_values[i+1] - 1 for i in range(0, len(rank_values) - 1))





