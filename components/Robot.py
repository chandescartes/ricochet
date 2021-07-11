
from enum import Enum

class RobotType(Enum):
    RED = 0
    GREEN = 1
    BLUE = 2
    YELLOW = 3
    WHITE = 4

class Robot:
    def __init__(self, type):
        self.type = type
        self.row = None
        self.col = None

    def __str__(self):
        return f'{self.type}'

    def get_position(self):
        return self.row, self.col

    def set_position(self, row, col):
        self.row = row
        self.col = col
