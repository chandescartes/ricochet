from functools import reduce


def solve(game):
    pass


def encode_robot_positions(robot_positions):
    """Return a hashable encoding given robot positions

    The first position is the target robot's position, which should be distinguished.
    The positions of other robots are sorted to produce the same encoding.
    """
    target_position = robot_positions[0]
    other_positions = robot_positions[1:]
    return (target_position, *sorted(other_positions))
