from common.board import Board
from solutions.day06.common import walk_board

def answer(data):
    board = Board(data)    
    answer = 0
    walk_board(board)
    candidates = list(map(lambda c: (c.x, c.y), board.all_cells('X')))
    for candidate in candidates:
        board.reset()
        board.cell_at(candidate[0],candidate[1]).value = '#'
        if not walk_board(board):
            answer += 1
    return answer
