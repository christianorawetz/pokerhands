from exceptions import InvalidCard, InvalidPokerHand
import rules


class Card:
    def __init__(self, rank, suit):
        if rank not in rules.CARD_RANK_VALUES or suit not in rules.CARD_SUITS:
            raise InvalidCard('{0}{1} is not a valid card'.format(suit, rank))

        self.rank_value = rules.CARD_RANK_VALUES[rank]
        self.rank = rank
        self.suit = suit

    def __hash__(self):
        return hash(self.__repr__())

    def __eq__(self, other):
        if isinstance(other, Card):
            return self.rank == other.rank and self.suit == other.suit
        else:
            return False

    def __repr__(self):
        return "{0}{1}".format(self.rank, self.suit)


class PokerHand:
    def __init__(self, cards):
        if cards is None or len(set(cards)) != 5:
            raise InvalidPokerHand('A poker hand must consist of 5 cards')

        self.cards = cards

    def get_rank_values(self):
        return [card.rank_value for card in self.cards]


class Score:
    def __init__(self, hand, poker_hand_rank, rank_scores):
        self.hand = hand
        self.poker_hand_rank = poker_hand_rank
        self.rank_scores = rank_scores

    def ranks_tied(self, other):
        return self.poker_hand_rank == other.poker_hand_rank

    def __gt__(self, other):
        if self.poker_hand_rank > other.poker_hand_rank:
            return True
        elif self.ranks_tied(other):
            if self.rank_scores > other.rank_scores:
                return True

            if self.rank_scores == other.rank_scores:
                return rules.high_card(self.hand) > rules.high_card(other.hand)

        return False

    def __lt__(self, other):
        if self.poker_hand_rank < other.poker_hand_rank:
            return True
        elif self.ranks_tied(other):
            if self.rank_scores < other.rank_scores:
                return True

            if self.rank_scores == other.rank_scores:
                return rules.high_card(self.hand) < rules.high_card(other.hand)

        return False




