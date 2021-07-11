
from enum import Enum

class RobotType(Enum):
    RED = 0
    GREEN = 1
    BLUE = 2
    YELLOW = 3
    WHITE = 4

class Robot:
    def __init__(self, type, row=None, col=None):
        self.type = type
        self.row = row
        self.col = col

    def __str__(self):
        if self.type == RobotType.RED:
            return 'R'
        if self.type == RobotType.GREEN:
            return 'G'
        if self.type == RobotType.BLUE:
            return 'B'
        if self.type == RobotType.YELLOW:
            return 'Y'
        if self.type == RobotType.WHITE:
            return 'W'

    def get_position(self):
        return self.row, self.col

    def set_position(self, row, col):
        self.row = row
        self.col = col
