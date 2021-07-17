import pytest

from components.Board import Board
from components.Game import Game


@pytest.fixture
def small_board():
    board = Board(size=4)
    up_walls = [(2, 2)]
    right_walls = [(2, 1)]
    board.set_walls(up_walls, right_walls)
    return board


@pytest.fixture
def small_board_with_holes(small_board):
    holes = [(0, 0), (0, 3), (2, 2)]
    small_board.set_holes(holes)
    return small_board


@pytest.fixture
def small_game(small_board_with_holes):
    game = Game(small_board_with_holes, num_robots=2)
    return game
