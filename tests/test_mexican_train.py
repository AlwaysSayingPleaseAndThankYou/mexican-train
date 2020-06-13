import pytest
from mexican_train import create_players


@pytest.mark.parametrize("player", [0, 1])
def test_create_players(example_board, player):
    players = create_players(2, example_board)
    assert len(players) == 2
    assert players[player].hand_size == 15
    assert len(players[player].tiles) == players[player].hand_size + 1
    assert players[player].open is False
    assert players[player].train == [[13, 13], [13, example_board.round]]
