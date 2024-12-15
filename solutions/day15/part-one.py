from common.board import Board
from collections import deque

def answer(data):
    base_state, directions = '\n'.join(data).split('\n\n')
    directions = deque(map(int,directions.replace('\n','').replace('<','7').replace('>','3').replace('^','1').replace('v','5')))
    board = Board(base_state.split('\n'))
    robot = next(board.all_cells('@'))
    while(len(directions) > 0):
        current_direction = directions.popleft()
        can_move = False
        test_cell = robot.neighbours[current_direction]
        move_cells = deque()
        while(test_cell != None and test_cell.value != '#'):
            move_cells.append(test_cell)
            if test_cell.value == '.':
                can_move = True
                break
            test_cell = test_cell.neighbours[current_direction]
        if can_move:
            robot.value = '.'
            hole_to_fill = move_cells.pop()
            hole_to_fill.value = 'O'
            if len(move_cells) > 0:
                robot = move_cells.popleft()
                robot.value = '@'
            else:
                hole_to_fill.value = '@'
                robot = hole_to_fill
    return sum(map(lambda box: box.y * 100 + box.x, board.all_cells('O')))
