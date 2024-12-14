from common.board import Board
from itertools import product
from os import environ
from solutions.day14.common import Robot

def answer(data):
    def init_robot_metadata(cell):
        cell.metadata['robots'] = set()
        return None
    
    Robot.init()

    if environ['IS_SAMPLE'] != 'False':
        width, height = 11, 7
    else:
        width, height = 101, 103
    
    board = Board(['.' * width] * height)
    board.wrap_edges()
    list(map(init_robot_metadata, board.all_cells('.')))

    new_robot = lambda d: Robot(d, board)
    list(map(new_robot, data))

    for _ in range(100):
        Robot.move_all()

    top_left = sum(map(lambda i: len(board.cell_at(i[0], i[1]).metadata['robots']), product(range(width // 2), range(height // 2))))
    top_right = sum(map(lambda i: len(board.cell_at(i[0], i[1]).metadata['robots']), product(range(width // 2 + 1, width), range(height // 2))))
    bottom_left = sum(map(lambda i: len(board.cell_at(i[0], i[1]).metadata['robots']), product(range(width // 2), range(height // 2 + 1, height))))
    bottom_right = sum(map(lambda i: len(board.cell_at(i[0], i[1]).metadata['robots']), product(range(width // 2 + 1, width), range(height // 2 + 1, height))))

    return top_left * top_right * bottom_left * bottom_right