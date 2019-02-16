from game import play
from parse import parse_hands


def main(file_path):
    player_1_score, player_2_score = 0, 0

    with open(file_path, 'r') as input_file:
        for line in input_file:
            player_1_hand, player_2_hand = parse_hands(line)
            player_1_result, player_2_result = play(player_1_hand, player_2_hand)

            player_1_score += player_1_result
            player_2_score += player_2_result

    print("Player 1 won {0} games".format(player_1_score))
    print("Player 2 won {0} games".format(player_2_score))


if __name__ == "__main__":
    main("data/p054_poker.txt")
