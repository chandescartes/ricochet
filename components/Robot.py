
from enum import Enum

class Robot:
    def __init__(self, name, row=None, col=None):
        self.name = name.upper()
        self.row = row
        self.col = col

    def __str__(self):
        return self.name[0]

    def get_position(self):
        return self.row, self.col

    def set_position(self, row, col):
        self.row = row
        self.col = col
