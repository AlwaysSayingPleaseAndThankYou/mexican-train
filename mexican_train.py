"""Central module for mexican_train package."""
from board import Board
from players import Player


def deal_num(num_players):
    """Return number of tile each player gets in starting hand."""
    hand_size = 0
    if num_players in [1, 2, 3, 4]:
        hand_size = 15
    elif num_players in [5, 6]:
        hand_size = 12
    elif num_players in [7, 8]:
        hand_size = 10
    return hand_size


def create_players(num_players, board):
    """Create the number of players for the game and initialize them."""
    players = []
    for i in range(num_players):
        players.append(Player(i, deal_num(num_players), board.round))
    for player in players:
        while i <= player.hand_size:
            player.tiles.append(board.deal_tile())
            i += 1
    return players


def reporter(players, board):
    """Return all the end tiles on the board.

    Needs to only return the value if the train is open.
    Otherwise append null.
    """
    report = []
    for player in players:
        if player.open:
            report.append(player.end)
    report.append(board.mexican_train)
    return report


def main(num_players):
    """Play the game."""
    game_board = Board()
    players = create_players(num_players, game_board)
    # TODO: each player must build their largest possible trains
    # players[0].possible_trains.append([[13, 13], [13, 12], [12, 8]])
    # players[0].possible_trains.append([[13, 13], [13, 7]])
    # print('built')
    # print(players[0].build_train())
    # print('possible - w append')
    # print(players[0].possible_trains)
    # players[0].clean_trains()
    # print('clean')
    # print(players[0].possible_trains)

    # useable_tiles = players[0]._find_useable_tiles(reporter(players, game_board))
    # for player in players:
    #     player.build_train()
    #     print(player.possible_trains)


if __name__ == '__main__':
    main(4)
