import pytest
from brain import Brain


# This assumes a game of size 8
@pytest.fixture
def example_brain():
    tiles = [[12, 9],
             [5, 6],
             [1, 2],
             [8, 8],
             [9, 8],
             [6, 11],
             [3, 9],
             [2, 4],
             [5, 10],
             [9, 10]]
    b = Brain(tiles)
    b.possible_trains = [[[13, 12], [12, 2]],
                         [[13, 12], [12, 10]]]
    return b


# TODO: I bet putting this in a test class means I dont' have to pass them each
# example brain
@pytest.mark.parametrize("tile", [([2, 1]), ([10, 5])])
def test__report_train_ends(example_brain, tile):
    report = example_brain._report_train_ends()
    assert tile in report or [tile[1], tile[0]] in report


@pytest.mark.parametrize("tile", [([1, 2]),
                                  ([2, 4]),
                                  ([9, 10])])
def test_find_useable_tiles(example_brain, tile):
    report = example_brain.find_useable_tiles(example_brain.possible_trains)
    assert tile in report
    assert tile not in example_brain.tiles


@pytest.mark.parametrize("original_train", [([[13, 12], [12, 2]]),
                                            ([[13, 12], [12, 10]])])
def test_build_train(example_brain, original_train):
    report = example_brain.build_train()
    assert any(original_train == train[:2] for train in report)
    assert all(len(train) > len(original_train) for train in report)


def test_clean_trains():
    assert False
