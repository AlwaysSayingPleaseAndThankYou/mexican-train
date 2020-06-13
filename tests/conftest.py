#conftest.py
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