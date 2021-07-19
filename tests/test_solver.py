from components import Game
from solver import encode_robot_positions


def test_encode_robot_positions():
    robot_positions = [(8, 8), (0, 8), (8, 0), (10, 8), (5, 5)]
    result = ((8, 8), (0, 8), (5, 5), (8, 0), (10, 8))
    encoding = encode_robot_positions(robot_positions)
    assert encoding == result

    robot_positions = [(15, 15), (0, 8), (8, 0), (0, 5), (5, 5)]
    result = ((15, 15), (0, 5), (0, 8), (5, 5), (8, 0))
    encoding = encode_robot_positions(robot_positions)
    assert encoding == result
