import pytest
from board import Board
from players import Player


@pytest.fixture
def example_board():
    test_board = Board()
    return test_board


@pytest.fixture
def example_player(example_board):
    return Player(0, 15, example_board.round)


def test_build_train(example_player):
    tiles = example_player.tiles
    assert False


def test_last_tile():
    assert False
