"""Central module for mexican_train package."""
from board import Board
from players import Player


def deal_num(num_players):
    # Should this be a function of board?
    """Return number of tile each player gets in starting hand."""
    hand_size = 0
    if num_players in [1, 2, 3, 4]:
        hand_size = 15
    elif num_players in [5, 6]:
        hand_size = 12
    elif num_players in [7, 8]:
        hand_size = 10
    return hand_size


def main(num_players):
    """Play the game."""
    game_board = Board(num_players)
    players = []
    for i in range(num_players):
        players.append(Player(i, deal_num(num_players), game_board))
    # TODO: each player must build their largest possible trains


if __name__ == '__main__':
    main(4)
