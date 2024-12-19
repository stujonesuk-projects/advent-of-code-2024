from common.board import Board
from os import environ
from collections import deque
from sys import maxsize

def answer(data):
    size = 7 if environ['IS_SAMPLE'] == 'True' else 71
    max_cnt = 12 if environ['IS_SAMPLE'] == 'True' else 1024
    board = Board(['.' * size] * size)
    for cell in board.all_cells('.'):
        cell.metadata['distance'] = maxsize
    cnt = 0
    for item in data:
        cnt += 1
        x,y = map(int,item.split(','))
        board.cell_at(x,y).value = '#'
        if cnt == max_cnt:
            break
    
    cell = board.cell_at(0,0)
    cell.metadata['distance'] = 0
    target = board.cell_at(size - 1, size - 1)
    to_process = deque([(cell,0)])
    while len(to_process) > 0:
        test, distance = to_process.popleft()
        for neighbour in test.neighbour_cells([1,3,5,7]):
            if neighbour.value == '.' and neighbour.metadata['distance'] > distance + 1:
                neighbour.metadata['distance'] = distance + 1
                to_process.append((neighbour, distance + 1))
    return target.metadata['distance']