import pytest
from board import Board


@pytest.mark.parametrize("tile, index, opens", [
    ([8, 1], 0, False),
    ([10, 7], 1, True)])
def test_play_tile(example_board, example_player, tile, index, opens):
    # Two player game
    # Example Player is player 0
    example_board.opens = [True, False, True]
    example_board.ends = [8, 10, 12]
    # Tile should be sanitized by other functions
    # Should only test a valid set of tiles
    example_board.play_tile(tile)
    assert example_board.ends[index] == tile[1]
    assert example_board.opens[0] is opens


def test_report_playables(example_board):
    assert False
