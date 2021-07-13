from components.Robot import Robot
from components.Target import Target


class Game:
    def __init__(self, board, num_robots=5):
        self.board = board
        self.num_robots = num_robots

        self.robots = {}
        for i in range(self.num_robots):
            robot_name = chr(65 + i)
            self.robots[robot_name] = Robot(robot_name)

    def set_target(self, robot, row, col):
        if self.target:
            row, col = self.target.row, self.target.col
            tile = self.board.get_tile(row, col)
            tile.clear_target()

        self.target = Target(robot.name, row, col)
