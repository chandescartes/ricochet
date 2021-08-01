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


@pytest.fixture
def standard_game():
    up_walls = [
        (1, 4),
        (1, 14),
        (2, 1),
        (3, 11),
        (4, 6),
        (4, 15),
        (6, 0),
        (7, 3),
        (7, 7),
        (7, 8),
        (7, 10),
        (7, 13),
        (8, 5),
        (9, 7),
        (9, 8),
        (10, 1),
        (10, 13),
        (11, 4),
        (12, 0),
        (12, 9),
        (12, 15),
        (13, 5),
        (13, 14),
        (14, 3),
        (14, 10),
    ]
    right_walls = [
        (0, 1),
        (0, 9),
        (1, 3),
        (1, 13),
        (2, 1),
        (2, 10),
        (3, 6),
        (6, 2),
        (6, 13),
        (7, 6),
        (7, 8),
        (7, 10),
        (8, 5),
        (8, 6),
        (8, 8),
        (9, 1),
        (9, 12),
        (10, 3),
        (11, 9),
        (13, 5),
        (13, 14),
        (14, 2),
        (14, 9),
        (15, 6),
        (15, 11),
    ]
    return Game(
        size=16,
        up_walls=up_walls,
        right_walls=right_walls,
        target_position=(0, 0),
        initial_robot_positions=[],
    )
