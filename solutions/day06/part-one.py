from common.board import Board
from solutions.day06.common import walk_board

def answer(data):
    board = Board(data)
    walk_board(board)
    return len(list(board.all_cells('X')))
