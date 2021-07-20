import pytest

from components import Direction, Game


@pytest.fixture
def game():
    return Game(
        size=16,
        up_walls=[(3, 8), (13, 8)],
        right_walls=[(8, 2), (8, 12)],
        target_position=(0, 0),
        initial_robot_positions=[],
    )


def test_move_up(game):
    position = game.move_robot(Direction.UP, 8, 8, [])
    assert position == (3, 8)

    position = game.move_robot(Direction.UP, 8, 8, [(5, 8)])
    assert position == (6, 8)

    position = game.move_robot(
        Direction.UP, 8, 8, [(0, 8), (4, 4), (3, 8), (5, 8), (10, 8)]
    )
    assert position == (6, 8)


def test_move_right(game):
    position = game.move_robot(Direction.RIGHT, 8, 8, [])
    assert position == (8, 12)

    position = game.move_robot(Direction.RIGHT, 8, 8, [(8, 12)])
    assert position == (8, 11)

    position = game.move_robot(
        Direction.RIGHT, 8, 8, [(8, 14), (4, 4), (8, 3), (8, 11), (8, 10)]
    )
    assert position == (8, 9)


def test_move_down(game):
    position = game.move_robot(Direction.DOWN, 8, 8, [])
    assert position == (12, 8)

    position = game.move_robot(Direction.DOWN, 8, 8, [(9, 8)])
    assert position == (8, 8)

    position = game.move_robot(
        Direction.DOWN, 8, 8, [(13, 8), (4, 4), (3, 8), (11, 8), (10, 8)]
    )
    assert position == (9, 8)


def test_move_left(game):
    position = game.move_robot(Direction.LEFT, 8, 8, [])
    assert position == (8, 3)

    position = game.move_robot(Direction.LEFT, 8, 8, [(8, 5)])
    assert position == (8, 6)

    position = game.move_robot(
        Direction.LEFT, 8, 8, [(8, 3), (4, 4), (8, 11), (8, 5), (8, 4)]
    )
    assert position == (8, 6)
