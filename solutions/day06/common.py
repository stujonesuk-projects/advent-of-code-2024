directions = {
    '^': 1,
    '>': 3,
    'v': 5,
    '<': 7
}
symbols = { v: k for k,v in directions.items() }

def walk_board(board):
    guard = next(board.all_cells('^','>','v','<'), None)
    if not guard:
        return True
    while(guard):
        if guard.value in guard.value_history:
            guard.change_value('X')
            guard = None                
            return False 
        next_guard = guard.neighbours[directions[guard.value]]
        if next_guard is None:
            guard.change_value('X')
            guard = None
            return True
        if next_guard.value == '#':
            guard.change_value(symbols[(directions[guard.value] + 2) % 8])
            continue
        next_guard.change_value(guard.value)
        guard.change_value('X')
        guard = next_guard
