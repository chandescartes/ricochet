from collections import defaultdict
from enum import Enum


class WallType(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class Board:
    def __init__(self, size=16):
        self.size = size
        self.invalids = defaultdict(bool)
        self.holes = defaultdict(bool)
        self.board = [
            [
                Tile(
                    r,
                    c,
                    is_wall_up=(r == 0),
                    is_wall_right=(c == self.size - 1),
                    is_wall_down=(r == self.size - 1),
                    is_wall_left=(c == 0),
                )
                for c in range(self.size)
            ]
            for r in range(self.size)
        ]

    def get_tile(self, row, col):
        return self.board[row][col]

    def set_wall(self, row, col, wall_type):
        self.get_tile(row, col).set_wall(wall_type)

    def set_walls(self, up_walls, right_walls):
        for r, c in up_walls:
            self.set_wall(r, c, WallType.UP)
            self.set_wall(r - 1, c, WallType.DOWN)

        for r, c in right_walls:
            self.set_wall(r, c, WallType.RIGHT)
            self.set_wall(r, c + 1, WallType.LEFT)

    def set_invalid(self, row, col):
        self.get_tile(row, col).set_invalid()
        self.invalids[row, col] = True

    def set_invalids(self, invalids):
        for r, c in invalids:
            self.set_invalid(r, c)

    def set_hole(self, row, col):
        self.get_tile(row, col).set_hole()
        self.holes[row, col] = True

    def set_holes(self, holes):
        for r, c in holes:
            self.set_hole(r, c)

    def __str__(self):
        size = self.size
        board_builder = []

        for r in range(size):
            row_builder = []
            down_wall_builder = []

            for c in range(size):
                tile = self.get_tile(r, c)

                tile_string = str(tile)
                right_wall_string = "|" if tile.is_wall(WallType.RIGHT) else " "
                combined_string = f"{tile_string}{right_wall_string}"
                row_builder.append(combined_string)

                down_wall_string = "_" if tile.is_wall(WallType.DOWN) else " "
                down_wall_builder.append(down_wall_string)

            row_string = "".join(row_builder)
            row_string = f"|{row_string}"
            board_builder.append(row_string)

            down_wall_string = " ".join(down_wall_builder)
            down_wall_string = f"|{down_wall_string}|"
            board_builder.append(down_wall_string)

        board_string = "\n".join(board_builder)
        board_string = f' {" ".join("_" * size)} \n{board_string}'
        return board_string


class Tile:
    def __init__(
        self,
        row,
        col,
        is_wall_up=False,
        is_wall_right=False,
        is_wall_down=False,
        is_wall_left=False,
        is_invalid=False,
        is_hole=False,
        robot=None,
        target=None,
    ):
        self.row = row
        self.col = col

        self.is_wall_up = is_wall_up
        self.is_wall_right = is_wall_right
        self.is_wall_down = is_wall_down
        self.is_wall_left = is_wall_left

        self.is_invalid = is_invalid
        self.is_hole = is_hole

        self.robot = robot
        self.target = target

    def __str__(self):
        if self.robot is not None:
            return str(self.robot)
        if self.target is not None:
            return str(self.target)
        return "."

    def is_wall(self, wall_type):
        if wall_type == WallType.UP:
            return self.is_wall_up
        if wall_type == WallType.RIGHT:
            return self.is_wall_right
        if wall_type == WallType.DOWN:
            return self.is_wall_down
        if wall_type == WallType.LEFT:
            return self.is_wall_left

    def set_wall(self, wall_type):
        if wall_type == WallType.UP:
            self.is_wall_up = True
        elif wall_type == WallType.RIGHT:
            self.is_wall_right = True
        elif wall_type == WallType.DOWN:
            self.is_wall_down = True
        elif wall_type == WallType.LEFT:
            self.is_wall_left = True

    def set_invalid(self):
        self.is_invalid = True

    def set_hole(self):
        assert (
            not self.is_invalid and self.is_corner()
        ), f"Cannot set wall at ({self.row}, {self.col})"
        self.is_hole = True

    def is_robot(self):
        return self.robot is not None

    def set_robot(self, robot):
        assert not self.is_invalid, f"Cannot set robot at ({self.row}, {self.col})"
        self.robot = robot

    def clear_robot(self):
        self.robot = None

    def set_target(self, target):
        assert self.is_hole, f"Cannot set target at ({self.row}, {self.col})"
        self.target = target

    def clear_target(self):
        self.target = None

    def is_corner(self):
        return (
            (self.is_wall_up and self.is_wall_right)
            or (self.is_wall_right and self.is_wall_down)
            or (self.is_wall_down and self.is_wall_left)
            or (self.is_wall_left and self.is_wall_up)
        )
