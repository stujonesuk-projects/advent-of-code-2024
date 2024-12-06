from common.board import Board

def answer(data):
    board = Board(data)
    directions = {
        '^': 1,
        '>': 3,
        'v': 5,
        '<': 7
    }
    symbols = { v: k for k,v in directions.items() }    
    guard = next(board.all_cells('^','>','v','<'))
    while(guard):
        next_guard = guard.neighbours[directions[guard.value]]
        if next_guard is None:
            guard.value = 'X'
            guard = None
            break
        if next_guard.value == '#':
            guard.value = symbols[(directions[guard.value] + 2) % 8]
            continue
        next_guard.value = guard.value
        guard.value = 'X'
        guard = next_guard
            
    return len(list(board.all_cells('X')))
