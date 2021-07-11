
from enum import Enum

class WallType(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class Board:
    def __init__(self, size=16):
        self.size = size
        self.initialize_board()

    def initialize_board(self):
        self.create_board()
        self.set_walls()

    def get_tile(self, row, col):
        return self.board[row][col]

    def create_board(self):
        self.board = [
            [
                Tile(
                    r, c, 
                    is_wall_up=(r == 0),
                    is_wall_right=(c == self.size - 1),
                    is_wall_down=(r == self.size - 1),
                    is_wall_left=(c == 0),
                ) for c in range(self.size)
            ] for r in range(self.size)
        ]

    def set_walls(self):
        up_walls = [(2, 1), (2, 6), (2, 9), (2, 14), (5, 6), (5, 10), (5, 15), (6, 0), (6, 12), (7, 7), (7, 8), (9, 7), (9, 8), (10, 4), (10, 6), (10, 15), (11, 0), (11, 13), (11, 8), (12, 7), (13, 1), (14, 9), (14, 14), (15, 3)]
        right_walls = [(0, 4), (0, 10), (1, 6), (1, 8), (2, 0), (2, 14), (4, 10), (5, 6), (6, 2), (6, 11), (7, 6), (7, 8), (8, 6), (8, 8), (9, 3), (10, 5), (10, 8), (11, 12), (12, 7), (13, 1), (13, 8), (14, 3), (14, 14), (15, 4), (15, 11)]

        for r, c in up_walls:
            tile = self.get_tile(r, c)
            tile.create_wall(WallType.UP)

            tile = self.get_tile(r - 1, c)
            tile.create_wall(WallType.DOWN)

        for r, c in right_walls:
            tile = self.get_tile(r, c)
            tile.create_wall(WallType.RIGHT)

            tile = self.get_tile(r, c + 1)
            tile.create_wall(WallType.LEFT)
     
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
                combined_string = f'{tile_string}{right_wall_string}'
                row_builder.append(combined_string)
                
                down_wall_string = "_" if tile.is_wall(WallType.DOWN) else " "
                down_wall_builder.append(down_wall_string)

            row_string = "".join(row_builder)
            row_string = f'|{row_string}'
            board_builder.append(row_string)

            down_wall_string = " ".join(down_wall_builder)
            down_wall_string = f'|{down_wall_string}|'
            board_builder.append(down_wall_string)

        board_string = "\n".join(board_builder)
        board_string = f' {" ".join("_" * size)} \n{board_string}'
        return board_string
        
class Tile:
    def __init__(
        self, row, col,
        robot=None, target=None, 
        is_wall_up=False, is_wall_right=False, is_wall_down=False, is_wall_left=False
    ):
        self.row = row
        self.col = col

        self.robot = robot
        self.target = target

        self.is_wall_up = is_wall_up
        self.is_wall_right = is_wall_right
        self.is_wall_down = is_wall_down
        self.is_wall_left = is_wall_left

    def __str__(self):
        if not self.robot is None:
            return str(self.robot)
        if not self.target is None:
            return str(self.target)
        return '.'

    def is_wall(self, wall_type):
        if wall_type == WallType.UP:
            return self.is_wall_up
        if wall_type == WallType.RIGHT:
            return self.is_wall_right
        if wall_type == WallType.DOWN:
            return self.is_wall_down
        if wall_type == WallType.LEFT:
            return self.is_wall_left

    def create_wall(self, wall_type):
        if wall_type == WallType.UP:
            self.is_wall_up = True
        elif wall_type == WallType.RIGHT:
            self.is_wall_right = True
        elif wall_type == WallType.DOWN:
            self.is_wall_down = True
        elif wall_type == WallType.LEFT:
            self.is_wall_left = True
    
    def remove_wall(self, wall_type):
        if wall_type == WallType.UP:
            self.is_wall_up = False
        elif wall_type == WallType.RIGHT:
            self.is_wall_right = False
        elif wall_type == WallType.DOWN:
            self.is_wall_down = False
        elif wall_type == WallType.LEFT:
            self.is_wall_left = False
    
    def remove_walls(self):
        self.is_wall_up = False
        self.is_wall_right = False
        self.is_wall_down = False
        self.is_wall_left = False
