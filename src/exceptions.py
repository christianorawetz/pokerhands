class InvalidCard(Exception):
    def __init__(self, message):
        super(InvalidCard, self).__init__(message)


class InvalidPokerHand(Exception):
    def __init__(self, message):
        super(InvalidPokerHand, self).__init__(message)
