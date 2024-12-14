from common.board import Board
from solutions.day14.common import Robot
from statistics import stdev, mean

def answer(data):
    def init_robot_metadata(cell):
        cell.metadata['robots'] = set()
        return None
    
    Robot.init()
    
    width, height = 101, 103
    
    board = Board(['.' * width] * height)
    board.wrap_edges()
    list(map(init_robot_metadata, board.all_cells('.')))

    new_robot = lambda d: Robot(d, board)
    list(map(new_robot, data))

    variances = {}
    i = 0
    while True:
        i += 1
        Robot.move_all()
        variances[i] = Robot.variance
        if i % 100 == 0:
            sd = stdev(variances.values())
            m = mean(variances.values())
            item = next(filter(lambda v: abs(v[1] - m) / sd > 10, variances.items()), None)
            if item:
                return item[0]