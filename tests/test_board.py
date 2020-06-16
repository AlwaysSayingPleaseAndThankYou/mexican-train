import pytest


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


@pytest.mark.parametrize("ends, opens", ([
    ([10, 4, 12], [True, False, True]),
    ([8, 7, 11], [True, False, True])
]))
def test_report_playables(example_board, ends, opens):
    # 2 player game
    example_board.ends = ends
    example_board.opens = opens
    returned = example_board.report_playables()
    assert len(returned) == example_board.opens.count(True)
    assert ends[1] not in returned
