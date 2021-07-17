from contextlib import nullcontext as does_not_raise

import pytest

from components.Board import Board
from components.Game import DirectionType, Game


def test_board_set_hole(small_board):
    with does_not_raise():
        small_board.set_hole(0, 0)
        small_board.set_hole(2, 2)

    with pytest.raises(AssertionError):
        small_board.set_hole(1, 1)

    with pytest.raises(AssertionError):
        small_board.set_hole(2, 3)


def test_invalids(small_board_with_holes):
    small_board_with_holes.set_invalid(3, 3)

    with pytest.raises(AssertionError):
        small_board_with_holes.set_hole(3, 3)

    game = Game(small_board_with_holes, num_robots=1)
    robot = game.get_robot_names()[0]

    with pytest.raises(AssertionError):
        game.set_target(robot, 3, 3)

    with pytest.raises(AssertionError):
        game.set_robot_position(robot, 3, 3)


def test_game_set_target(small_game):
    robot, _ = small_game.get_robot_names()

    with does_not_raise():
        small_game.set_target(robot, 0, 0)
        small_game.set_target(robot, 0, 3)

    assert small_game.get_target_position() == (0, 3)

    with pytest.raises(AssertionError):
        small_game.set_target(robot, 3, 3)

    with pytest.raises(AssertionError):
        small_game.set_target(robot, 1, 1)


def test_game_move_robot(small_game):
    robot_a, robot_b = small_game.get_robot_names()

    small_game.set_robot_position(robot_a, 2, 1)
    r, c = small_game.move_robot(robot_a, DirectionType.UP)
    assert r == 0 and c == 1

    small_game.set_robot_position(robot_a, 2, 1)
    r, c = small_game.move_robot(robot_a, DirectionType.RIGHT)
    assert r == 2 and c == 1

    small_game.set_robot_position(robot_a, 2, 1)
    r, c = small_game.move_robot(robot_a, DirectionType.DOWN)
    assert r == 3 and c == 1

    small_game.set_robot_position(robot_a, 2, 1)
    r, c = small_game.move_robot(robot_a, DirectionType.LEFT)
    assert r == 2 and c == 0

    small_game.set_robot_position(robot_b, 0, 1)
    small_game.set_robot_position(robot_a, 1, 1)
    r, c = small_game.move_robot(robot_a, DirectionType.UP)
    assert r == 1 and c == 1

    small_game.set_robot_position(robot_b, 1, 3)
    small_game.set_robot_position(robot_a, 1, 1)
    r, c = small_game.move_robot(robot_a, DirectionType.RIGHT)
    assert r == 1 and c == 2

    small_game.set_robot_position(robot_b, 3, 1)
    small_game.set_robot_position(robot_a, 1, 1)
    r, c = small_game.move_robot(robot_a, DirectionType.DOWN)
    assert r == 2 and c == 1

    small_game.set_robot_position(robot_b, 1, 0)
    small_game.set_robot_position(robot_a, 1, 1)
    r, c = small_game.move_robot(robot_a, DirectionType.LEFT)
    assert r == 1 and c == 1


def test_game_is_game_finished(small_game):
    robot, _ = small_game.get_robot_names()
    small_game.set_target(robot, 0, 0)

    small_game.set_robot_position(robot, 0, 1)
    assert not small_game.is_game_finished()

    small_game.set_robot_position(robot, 0, 0)
    assert small_game.is_game_finished()
