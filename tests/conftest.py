#conftest.py
import pytest
from board import Board
from players import Player


@pytest.fixture
def example_board():
    test_board = Board(4)
    return test_board


@pytest.fixture
def example_player(example_board):
    return Player(0, 15, example_board)


@pytest.fixture
def example_players_4(example_board):
    players_4 = []
    for i in range(4):
        players_4.append(Player(i, 15, example_board))
    return players_4


@pytest.fixture
def example_players_6(example_board):
    players_6 = []
    for i in range(6):
        players_6.append(Player(i, 12, example_board))
    return players_6

# These are all for testing player.take_turn
