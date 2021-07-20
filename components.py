from enum import Enum


class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class Game:
    def __init__(
        self, size, up_walls, right_walls, target_position, initial_robot_positions
    ):
        self.size = size

        self._create_board()
        self._set_walls(up_walls, right_walls)
        self._precompute_movement_board()

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
                [(r == 0), (c == self.size - 1), (r == self.size - 1), (c == 0)]
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

    def _precompute_move_up(self, row, col):
        for r in range(row, -1, -1):
            if self.board[r][col][0]:
                return r
        assert f"Infinite move up from ({row}, {col})!"

    def _precompute_move_right(self, row, col):
        for c in range(col, self.size):
            if self.board[row][c][1]:
                return c
        assert f"Infinite move right from ({row}, {col})!"

    def _precompute_move_down(self, row, col):
        for r in range(row, self.size):
            if self.board[r][col][2]:
                return r
        assert f"Infinite move down from ({row}, {col})!"

    def _precompute_move_left(self, row, col):
        for c in range(col, -1, -1):
            if self.board[row][c][3]:
                return c
        assert f"Infinite move left from ({row}, {col})!"

    def _precompute_movement_board(self):
        """Precompute where robots will end up after move, assuming no robots present

        To optimize move computation.
        """
        self.movement_board = [
            [
                (
                    self._precompute_move_up(r, c),
                    self._precompute_move_right(r, c),
                    self._precompute_move_down(r, c),
                    self._precompute_move_left(r, c),
                )
                for c in range(self.size)
            ]
            for r in range(self.size)
        ]

    def _move_robot_up(self, row, col, other_robot_positions):
        final_row = self.movement_board[row][col][0]
        for r, c in other_robot_positions:
            if c == col and final_row <= r < row:
                final_row = r + 1
        return final_row, col

    def _move_robot_right(self, row, col, other_robot_positions):
        final_col = self.movement_board[row][col][1]
        for r, c in other_robot_positions:
            if r == row and col < c <= final_col:
                final_col = c - 1
        return row, final_col

    def _move_robot_down(self, row, col, other_robot_positions):
        final_row = self.movement_board[row][col][2]
        for r, c in other_robot_positions:
            if c == col and row < r <= final_row:
                final_row = r - 1
        return final_row, col

    def _move_robot_left(self, row, col, other_robot_positions):
        final_col = self.movement_board[row][col][3]
        for r, c in other_robot_positions:
            if r == row and final_col <= c < col:
                final_col = c + 1
        return row, final_col

    def move_robot(self, direction, row, col, other_robot_positions):
        if direction == Direction.UP:
            return self._move_robot_up(row, col, other_robot_positions)

        if direction == Direction.RIGHT:
            return self._move_robot_right(row, col, other_robot_positions)

        if direction == Direction.DOWN:
            return self._move_robot_down(row, col, other_robot_positions)

        if direction == Direction.LEFT:
            return self._move_robot_left(row, col, other_robot_positions)

        raise AssertionError(f"Invalid direction {direction} 🚫")
