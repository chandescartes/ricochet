
from enum import Enum

class WallType(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class Board:
    def __init__(self, board_size=16, num_robots=5):
        self.board_size = board_size
        self.num_robots = num_robots

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
                    is_wall_right=(c == self.board_size - 1),
                    is_wall_down=(r == self.board_size - 1),
                    is_wall_left=(c == 0),
                ) for c in range(self.board_size)
            ] for r in range(self.board_size)
        ]

    def set_walls(self):
        up_walls = [(2, 1), (2, 6), (2, 9), (2, 14), (5, 7), (5, 11), (5, 15), (6, 0), (6, 12), (7, 7), (7, 8), (9, 7), (9, 8), (10, 4), (10, 6), (10, 15), (11, 0), (11, 13), (11, 8), (12, 7), (13, 1), (14, 9), (14, 14), (15, 3)]
        right_walls = [(0, 4), (0, 10), (1, 6), (1, 8), (2, 0), (2, 14), (4, 10), (5, 6), (6, 2), (6, 11), (7, 6), (7, 8), (8, 6), (8, 8), (9, 5), (9, 8), (10, 12), (11, 7), (12, 1), (12, 8), (13, 3), (13, 14), (15, 4), (15, 11)]

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
