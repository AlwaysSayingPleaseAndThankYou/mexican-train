import pytest


@pytest.mark.parametrize("tile, index, opens, train_num", [
    ([8, 1], 0, False, 0),
    ([10, 7], 1, False, 1),
    ([12, 1], 2, True, 2)])
def test_play_tile(example_board, example_player, tile, index, opens, train_num):
    """Two player game
    Tile should only be passed if its a valid tile
    Should only test a valid set of tiles"""
    # This should close the train if Player_ID == train_num
    example_board.opens = [True, False, True]
    example_board.ends = [8, 10, 12]
    example_board.play_tile(tile, train_num)
    assert example_board.ends[index] == tile[1]
    assert example_board.opens[train_num] is opens


# 2 player game
@pytest.mark.parametrize("tile, player_id, train", [
    ([4, 7], 0, 0),
    ([6, 10], 0, 1),
    ([12, 3], 0, 2)])
def test_play_tile(example_board, tile, player_id, train):
    example_board.opens = [True, True, True]
    example_board.ends = [6, 4, 12]
    example_board.play_tile(tile, train, player_id)
    if player_id == train:
        assert example_board.opens[train] is False
    else:
        assert example_board.opens[train] is True
    assert example_board.ends[train] == tile[1]


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
    for item in returned:
        assert len(item) == 2
