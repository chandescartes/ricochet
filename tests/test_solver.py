from solver import encode_robot_positions


def test_encode_robot_positions(standard_game):
    robots = standard_game.get_robot_names()
    standard_game.set_robot_position(robots[0], 8, 8)
    standard_game.set_robot_position(robots[1], 0, 8)
    standard_game.set_robot_position(robots[2], 8, 0)
    standard_game.set_robot_position(robots[3], 10, 8)
    standard_game.set_robot_position(robots[4], 5, 5)

    result = ((8, 8), (0, 8), (5, 5), (8, 0), (10, 8))
    encoding = encode_robot_positions(standard_game)
    assert encoding == result

    standard_game.set_robot_position(robots[0], 15, 15)
    standard_game.set_robot_position(robots[3], 0, 5)

    result = ((15, 15), (0, 5), (0, 8), (5, 5), (8, 0))
    encoding = encode_robot_positions(standard_game)
    assert encoding == result
