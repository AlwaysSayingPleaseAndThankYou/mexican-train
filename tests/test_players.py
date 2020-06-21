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


@pytest.mark.parametrize("tile, target",[([2, 1], 0),
                                         ([4.11], 5)])
def test_play_tile(example_board, example_player, tile, target):
    len_tiles = len(example_player.tiles)
    example_player.play_tile(example_board, tile, target)
    assert len(example_player.tiles) < len_tiles
    assert example_board.ends[target] == tile[1]
    assert tile not in example_player.workingTrain
