import pytest
from players import Player
from mexican_train import deal_num


def test__create_player(example_board):
    player = Player(0, 15, example_board)
    assert player.hand_size == 15
    assert len(player.tiles) == player.hand_size + 1
    assert player.open is False
    # check tiles have been taken from board
    for tile in player.tiles:
        assert tile not in example_board.boneyard


@pytest.mark.parametrize("num_players, round", [(4, 7),
                                                (6, 3),
                                                (2, 10)])
def test_create_many_players(example_board, num_players, round):
    players = []
    for i in range(num_players):
        players.append(Player(i, deal_num(num_players), example_board))
    assert len(players) == num_players


@pytest.mark.parametrize("double, len_possible, num_tiles,", [(False, 2, 16),
                                                              (True, 2, 16)])
def test_take_turn(example_player, example_board, double, len_possible, num_tiles):
    example_board.double = double
    example_player.possible_trains = example_player.possible_trains[:len_possible]
    example_player.tiles = example_player.tiles[:num_tiles]
    if example_board.double:
        example_player.take_turn(example_board)
        assert example_board.double is False or len(example_player.tiles) == num_tiles + 1
    elif