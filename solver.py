from collections import deque

from components import Direction


def solve(game):
    target_position = game.target_position
    initial_robot_positions = game.initial_robot_positions
    initial_encoding = encode_robot_positions(initial_robot_positions)

    queue = deque([(initial_robot_positions, initial_encoding, 0)])
    seen = {initial_encoding: None}

    while queue:
        robot_positions, encoding, num_moves = queue.popleft()

        if num_moves > 20:
            # Sanity check
            raise AssertionError("Failed to solve 🤯")

        target_robot_position = robot_positions[0]
        if target_robot_position == target_position:
            return num_moves

        for i, (row, col) in enumerate(robot_positions):
            other_robot_positions = robot_positions[:i] + robot_positions[i + 1 :]

            for d in Direction:
                new_position = game.move_robot(d, row, col, other_robot_positions)
                new_robot_positions = (
                    robot_positions[:i] + [new_position] + robot_positions[i + 1 :]
                )
                new_encoding = encode_robot_positions(new_robot_positions)

                if new_encoding not in seen:
                    queue.append((new_robot_positions, new_encoding, num_moves + 1))
                    seen[new_encoding] = encoding

    raise AssertionError("We somehow exhausted the queue before finding a solution 🤔")


def encode_robot_positions(robot_positions):
    """Return a hashable encoding given robot positions

    The first position is the target robot's position, which should be distinguished.
    The positions of other robots are sorted to produce the same encoding.
    """
    target_position = robot_positions[0]
    other_positions = robot_positions[1:]
    return (target_position, *sorted(other_positions))
