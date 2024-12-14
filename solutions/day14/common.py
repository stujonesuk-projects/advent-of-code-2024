from statistics import stdev
from math import sqrt
from re import match

class Robot:
    robot_id = 0
    by_id = {}
    variance = 0

    def init():
        Robot.robot_id = 0
        Robot.by_id = {}
        Robot.variance = 0

    def move_all():
        x_vals = []
        y_vals = []
        for robot in Robot.by_id.values():
            robot.move()
            x_vals.append(robot.pos_x)
            y_vals.append(robot.pos_y)
        Robot.variance = sqrt(stdev(x_vals) * stdev(y_vals))

    def __init__(self, data, board):
        parsed_data = match('^p=([-0-9]+),([-0-9]+) v=([-0-9]+),([-0-9]+)$', data).groups()
        self.id = Robot.robot_id
        Robot.by_id[self.id] = self
        Robot.robot_id += 1
        self.pos_x = int(parsed_data[0])
        self.pos_y = int(parsed_data[1])
        self.vel_x = int(parsed_data[2])
        self.vel_y = int(parsed_data[3])
        self.move_directions = []
        if self.vel_x > 0:
            self.move_directions.extend([3] * self.vel_x)
        if self.vel_x < 0:
            self.move_directions.extend([7] * -self.vel_x)
        if self.vel_y > 0:
            self.move_directions.extend([5] * self.vel_y)
        if self.vel_y < 0:
            self.move_directions.extend([1] * -self.vel_y)
        self.cell = board.cell_at(self.pos_x, self.pos_y)
        self.cell.metadata['robots'].add(self.id)

    def move(self):
        self.cell.metadata['robots'].remove(self.id)
        for d in self.move_directions:
            self.cell = self.cell.neighbours[d]
        self.cell.metadata['robots'].add(self.id)
        self.pos_x = self.cell.x
        self.pos_y = self.cell.y
