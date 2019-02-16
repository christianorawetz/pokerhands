from models import Card, PokerHand


def parse_hands(input_str):
    cards = input_str.strip().split(' ')

    player_1_cards, player_2_cards = parse_cards(cards[:5]), parse_cards(cards[5:])

    return PokerHand(player_1_cards), PokerHand(player_2_cards)


def parse_cards(cards):
    return [Card(card[0], card[1]) for card in cards]
