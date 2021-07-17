from contextlib import nullcontext as does_not_raise

import pytest

from components.Board import Board
from components.Game import DirectionType, Game


def test_board_set_hole():
    board = Board(size=4)
    board.set_walls([(2, 2)], [(2, 1)])

    with does_not_raise():
        board.set_hole(0, 0)
        board.set_hole(0, 3)
        board.set_hole(2, 2)

    with pytest.raises(AssertionError):
        board.set_hole(0, 1)
    with pytest.raises(AssertionError):
        board.set_hole(2, 3)


def test_game_move_robot():
    board = Board(size=4)
    board.set_walls([(3, 0)], [])

    game = Game(board, num_robots=2)
    robot_a, robot_b = game.get_robot_names()

    game.set_robot_position(robot_a, 0, 0)
    r, c = game.move_robot(robot_a, DirectionType.UP)
    assert r == 0 and c == 0

    game.set_robot_position(robot_a, 0, 0)
    r, c = game.move_robot(robot_a, DirectionType.DOWN)
    assert r == 2 and c == 0

    game.set_robot_position(robot_a, 0, 0)
    r, c = game.move_robot(robot_a, DirectionType.RIGHT)
    assert r == 0 and c == 3

    game.set_robot_position(robot_b, 0, 2)
    game.set_robot_position(robot_a, 0, 0)
    r, c = game.move_robot(robot_a, DirectionType.RIGHT)
    assert r == 0 and c == 1


def test_game_is_game_completed():
    board = Board(size=4)
    board.set_hole(0, 0)

    game = Game(board, num_robots=1)
    robot_a = game.get_robot_names()[0]
    game.set_target(robot_a, 0, 0)

    game.set_robot_position(robot_a, 0, 1)
    assert not game.is_game_completed()

    game.set_robot_position(robot_a, 0, 0)
    assert game.is_game_completed()
