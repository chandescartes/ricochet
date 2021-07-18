from functools import reduce


def solve(game):
    pass


def encode_robot_positions(game):
    target_position = game.target_robot.get_position()
    other_positions = (
        game.get_robot_position(robot_name)
        for robot_name in game.get_robot_names()
        if robot_name != game.target_robot.name
    )
    other_positions = sorted(other_positions)
    return (target_position, *other_positions)
