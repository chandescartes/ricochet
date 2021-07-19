from enum import Enum


class Game:
    def __init__(
        self, size, up_walls, right_walls, target_position, initial_robot_positions
    ):
        self.size = size

        self._create_board()
        self._set_walls(up_walls, right_walls)

        self.target_position = target_position

        # First index is position of the target robot, the rest are other robots' positions.
        self.initial_robot_positions = initial_robot_positions

    def _create_board(self):
        """Creates a board with boundary walls

        self.board[r][c] is a tuple of 4 booleans.
        Whether a wall exists at direction (up, right, down, left)
        """
        self.board = [
            [
                ((r == 0), (c == self.size - 1), (r == self.size - 1), (c == 0))
                for c in range(self.size)
            ]
            for r in range(self.size)
        ]

    def _set_walls(self, up_walls, right_walls):
        """Sets walls on board given a list of up walls and right walls

        For each up wall, set a down wall at the position above it.
        For each right wall, set a left wall at the position to the right of it.
        """
        for r, c in up_walls:
            self.board[r][c][0] = True
            self.board[r - 1][c][2] = True

        for r, c in right_walls:
            self.board[r][c][1] = True
            self.board[r][c + 1][3] = True
