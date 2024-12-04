from common.board import Board

def check_x_mas(cell):
    axis_nw_se = cell.neighbour_values([0,4])
    axis_ne_sw = cell.neighbour_values([2,6])
    return 1 if (axis_nw_se == axis_ne_sw == set(['M','S'])) else 0

def answer(data):
    return sum(map(check_x_mas, Board(data).all_cells('A')))
