from components import Game
from solver import encode_robot_positions, solve


def test_encode_robot_positions():
    robot_positions = [(8, 8), (0, 8), (8, 0), (10, 8), (5, 5)]
    result = ((8, 8), (0, 8), (5, 5), (8, 0), (10, 8))
    encoding = encode_robot_positions(robot_positions)
    assert encoding == result

    robot_positions = [(15, 15), (0, 8), (8, 0), (0, 5), (5, 5)]
    result = ((15, 15), (0, 5), (0, 8), (5, 5), (8, 0))
    encoding = encode_robot_positions(robot_positions)
    assert encoding == result


def test_solve():
    game = Game(
        size=4,
        up_walls=[],
        right_walls=[],
        target_position=(0, 0),
        initial_robot_positions=[(2, 0), (0, 3)],
    )
    assert solve(game) == 1

    game = Game(
        size=4,
        up_walls=[],
        right_walls=[],
        target_position=(3, 2),
        initial_robot_positions=[(2, 0), (0, 3)],
    )
    assert solve(game) == 3
