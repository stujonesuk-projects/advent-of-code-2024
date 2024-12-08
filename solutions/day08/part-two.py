from common.board import Board
from itertools import combinations
from solutions.day08.common import coords_add, coords_sub, add_antinode_if_valid

def answer(data):
    board = Board(data)
    antenna_types = board.values.difference(set('.'))
    antinodes = set()
    for antenna in antenna_types:
        for antenna_pair in combinations(map(lambda cell: cell.coords(), board.all_cells(antenna)), 2):
            dist = coords_sub(antenna_pair[1], antenna_pair[0])
            directions = [
                (antenna_pair[1], lambda x: coords_add(x, dist)),
                (antenna_pair[0], lambda x: coords_sub(x, dist)),
            ]
            for antinode, operator in directions:
                while(add_antinode_if_valid(antinodes, antinode, board)):
                    antinode = operator(antinode)
    return len(antinodes)
