
from components.Robot import RobotType

class Target:
    def __init__(self, type, row, col):
        self.type = type
        self.row = row
        self.col = col

    def __str__(self):
        if self.type == RobotType.RED:
            return 'r'
        if self.type == RobotType.GREEN:
            return 'g'
        if self.type == RobotType.BLUE:
            return 'b'
        if self.type == RobotType.YELLOW:
            return 'y'
        if self.type == RobotType.WHITE:
            return 'w'

    def get_position(self):
        return self.row, self.col

    def set_position(self, row, col):
        self.row = row
        self.col = col
