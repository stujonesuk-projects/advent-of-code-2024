from common.board import Board
from collections import deque

def answer(data):
    board = Board(data, parse_as_int=True)
    trailheads = board.all_cells(0)
    answer = 0
    for trailhead in trailheads:
        cells = deque([trailhead])
        visited = set()
        while len(cells) > 0:
            cell = cells.popleft()
            if cell not in visited:
                visited.add(cell)
                if cell.value == 9:
                    answer += 1
                    continue
                neighbours = list(filter(lambda a: a.value == cell.value + 1 and a not in visited, cell.neighbour_cells([1, 3, 5, 7])))
                cells.extend(neighbours)
    return answer