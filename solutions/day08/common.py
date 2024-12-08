def coords_add(a,b):
    return (a[0]+b[0], a[1]+b[1])

def coords_sub(a,b):
    return (a[0]-b[0], a[1]-b[1])

def valid_antinode(antinode, board):
    return 0 <= antinode[0] <= board.max_x and 0 <= antinode[1] <= board.max_y

def add_antinode_if_valid(antinodes, antinode, board):
    if valid_antinode(antinode, board):
        antinodes.add(antinode)
        return True
    return False
