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


@pytest.fixture
def standard_game():
    board = Board()
    up_walls = []
    right_walls = []
    board.set_walls(up_walls, right_walls)
    invalids = []
    board.set_invalids(invalids)
    holes = [(0, 0)]
    board.set_holes(holes)

    game = Game(board)
    robot = game.get_robot_names()[0]
    game.set_target(robot, *(holes[0]))
    return game
