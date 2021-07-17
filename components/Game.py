from enum import Enum

from components.Board import WallType
from components.Robot import Robot
from components.Target import Target


class DirectionType(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class Game:
    def __init__(self, board, num_robots=5):
        self.board = board
        self.num_robots = num_robots

        self.robots = {}
        for i in range(self.num_robots):
            robot_name = chr(65 + i)
            self.robots[robot_name] = Robot(robot_name)

        self.target = None
        self.target_robot = None

    def get_target_position(self):
        if not self.target:
            return None
        return self.target.get_position()

    def set_target(self, robot_name, row, col):
        self.clear_target()
        self.target = Target(robot_name, row, col)
        self.board.get_tile(row, col).set_target(self.target)
        self.target_robot = self.robots[robot_name]

    def clear_target(self):
        if self.target:
            row, col = self.target.row, self.target.col
            self.board.get_tile(row, col).clear_target()
            self.target = None
            self.target_robot = None

    def get_robot_names(self):
        return list(self.robots.keys())

    def get_robot_position(self, robot_name):
        return self.robots[robot_name].get_position()

    def set_robot_position(self, robot_name, row, col):
        robot = self.robots[robot_name]
        prev_r, prev_c = robot.get_position()
        if prev_r is not None and prev_c is not None:
            self.board.get_tile(prev_r, prev_c).clear_robot()
        self.board.get_tile(row, col).set_robot(robot)
        robot.set_position(row, col)

    def get_position_after_move_up(self, start_r, start_c):
        for r in range(start_r, -1, -1):
            if self.board.get_tile(r, start_c).is_wall(WallType.UP) or (
                r > 0 and self.board.get_tile(r - 1, start_c).is_robot()
            ):
                return r, start_c
        assert f"Reached end of board without hitting a wall! ({r}, {start_c})"

    def get_position_after_move_right(self, start_r, start_c):
        size = self.board.size
        for c in range(start_c, size):
            if self.board.get_tile(start_r, c).is_wall(WallType.RIGHT) or (
                c < size - 1 and self.board.get_tile(start_r, c + 1).is_robot()
            ):
                return start_r, c
        assert f"Reached end of board without hitting a wall! ({start_r}, {c})"

    def get_position_after_move_down(self, start_r, start_c):
        size = self.board.size
        for r in range(start_r, size):
            if self.board.get_tile(r, start_c).is_wall(WallType.DOWN) or (
                r < size - 1 and self.board.get_tile(r + 1, start_c).is_robot()
            ):
                return r, start_c
        assert f"Reached end of board without hitting a wall! ({r}, {start_c})"

    def get_position_after_move_left(self, start_r, start_c):
        for c in range(start_c, -1, -1):
            if self.board.get_tile(start_r, c).is_wall(WallType.LEFT) or (
                c > 0 and self.board.get_tile(start_r, c - 1).is_robot()
            ):
                return start_r, c
        assert f"Reached end of board without hitting a wall! ({start_r}, {c})"

    def move_robot(self, robot_name, direction):
        robot = self.robots[robot_name]
        start_r, start_c = robot.get_position()

        if direction == DirectionType.UP:
            end_r, end_c = self.get_position_after_move_up(start_r, start_c)
        elif direction == DirectionType.RIGHT:
            end_r, end_c = self.get_position_after_move_right(start_r, start_c)
        elif direction == DirectionType.DOWN:
            end_r, end_c = self.get_position_after_move_down(start_r, start_c)
        elif direction == DirectionType.LEFT:
            end_r, end_c = self.get_position_after_move_left(start_r, start_c)

        self.board.get_tile(start_r, start_c).clear_robot()
        self.board.get_tile(end_r, end_c).set_robot(robot)
        robot.set_position(end_r, end_c)
        return end_r, end_c

    def is_game_finished(self):
        if not self.target:
            return False
        target_row, target_col = self.target.get_position()
        robot_row, robot_col = self.target_robot.get_position()
        return target_row == robot_row and target_col == robot_col
