from common.board import Board
from collections import deque

class Box:
    cells = {}

    def __init__(self, left_cell):
        self.left_cell = left_cell
        self.right_cell = left_cell.neighbours[3]
        Box.cells[self.left_cell] = self
        Box.cells[self.right_cell] = self

    def move(self, direction):
        if direction in [1,5]:
            next = [self.left_cell.neighbours[direction], self.right_cell.neighbours[direction]]
            if next[0].value in ['[',']']:
                Box.cells[next[0]].move(direction)
            if next[1].value == '[':
                Box.cells[next[1]].move(direction)
            next[0].value = '['
            next[1].value = ']'
            self.left_cell.value = '.'
            self.right_cell.value = '.'
            del Box.cells[self.left_cell]
            del Box.cells[self.right_cell]
            self.left_cell = next[0]
            self.right_cell = next[1]
            Box.cells[self.left_cell] = self
            Box.cells[self.right_cell] = self
        elif direction == 3:
            next = self.right_cell.neighbours[3]
            if next.value == '[':
                Box.cells[next].move(3)
            self.left_cell.value = '.'
            self.right_cell.value = '['
            next.value = ']'
            del Box.cells[self.left_cell]
            self.left_cell = self.right_cell
            self.right_cell = next
            Box.cells[self.right_cell] = self
        elif direction == 7:
            next = self.left_cell.neighbours[7]
            if next.value == ']':
                Box.cells[next].move(7)
            self.right_cell.value = '.'
            self.left_cell.value = ']'
            next.value = '['
            del Box.cells[self.right_cell]
            self.right_cell = self.left_cell
            self.left_cell = next
            Box.cells[self.left_cell] = self

    def can_move(self, direction):
        if direction == 7:
            next = self.left_cell.neighbours[7]
            if next is None:
                return False
            if next.value == '#':
                return False
            if next.value == ']':
                return Box.cells[next].can_move(7)
            return True
        if direction == 3:
            next = self.right_cell.neighbours[3]
            if next is None:
                return False
            if next.value == '#':
                return False
            if next.value == '[':
                return Box.cells[next].can_move(3)
            return True
        if direction in [1,5]:
            next = [self.left_cell.neighbours[direction], self.right_cell.neighbours[direction]]
            if any(filter(lambda n: n is None, next)):
                return False
            if any(filter(lambda n: n.value == '#', next)):
                return False
            if any(filter(lambda n: n.value in ['[',']'], next)):
                return all(map(lambda n: n not in Box.cells or Box.cells[n].can_move(direction), next))
            return True
        raise ValueError()

def answer(data):
    base_state, directions = '\n'.join(data).split('\n\n')
    directions = deque(map(int,directions.replace('\n','').replace('<','7').replace('>','3').replace('^','1').replace('v','5')))
    base_state = base_state.split('\n')
    base_state = map(lambda r: r.replace('#','##').replace('O','[]').replace('.','..').replace('@','@.'), base_state)
    board = Board(base_state)
    list(map(Box,board.all_cells('[')))
    robot = next(board.all_cells('@'))
    while(len(directions) > 0):
        current_direction = directions.popleft()
        test_cell = robot.neighbours[current_direction]
        if test_cell is None:
            continue
        if test_cell.value == '#':
            continue
        if test_cell.value == '.':
            robot.value = '.'
            test_cell.value = '@'
            robot = test_cell
            continue
        test_box = Box.cells[test_cell]
        if test_box.can_move(current_direction):
            test_box.move(current_direction)
            test_cell.value = '@'
            robot.value = '.'
            robot = test_cell
            continue
        
    return sum(map(lambda box: box.y * 100 + box.x, board.all_cells('[')))
