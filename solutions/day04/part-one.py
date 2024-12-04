from common.board import Board

def answer(data):
    return sum(map(lambda x: x.count('XMAS'), Board(data).walk()))
