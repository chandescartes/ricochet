
class Target:
    def __init__(self, robot_name, row, col):
        self.robot_name = robot_name
        self.row = row
        self.col = col

    def __str__(self):
        return self.robot_name.lower()[0]

    def get_position(self):
        return self.row, self.col

    def set_position(self, row, col):
        self.row = row
        self.col = col
