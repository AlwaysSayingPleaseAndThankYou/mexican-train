from players import Player


def test__create_player(example_board):
    player = Player(0, 15, example_board)
    assert player.hand_size == 15
    assert len(player.tiles) == player.hand_size + 1
    assert player.open is False
    # check tiles have been taken from board
    for tile in player.tiles:
        assert tile not in example_board.boneyard


def test_take_turn():
    assert False
