import pytest

from components import Game


@pytest.fixture
def mini_game():
    return Game(
        size=4,
        up_walls=[],
        right_walls=[],
        target_position=(0, 0),
        initial_robot_positions=[(2, 0), (0, 3)],
    )


@pytest.fixture
def standard_game_few_walls():
    return Game(
        size=16,
        up_walls=[(3, 8), (13, 8)],
        right_walls=[(8, 2), (8, 12)],
        target_position=(0, 0),
        initial_robot_positions=[],
    )
