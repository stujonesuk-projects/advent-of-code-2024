from collections import defaultdict

directions = {
    0: (-1,-1),
    1: (0,-1),
    2: (1,-1),
    3: (1,0),
    4: (1,1),
    5: (0,1),
    6: (-1,1),
    7: (-1,0)
}

class Cell:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value
        self.initial_value = value
        self.neighbours = { i:None for i in range(8) }
        self.value_history = []
        self.metadata = defaultdict(None)
    
    def connect_neighbours(self, cells):
        for k in self.neighbours.keys():
            direction = directions[k]
            self.neighbours[k] = cells.get(self.y + direction[1], {}).get(self.x + direction[0], None)
    
    def neighbour_values(self, direction_list):
        values = set()
        for direction in direction_list:
            if self.neighbours[direction] is not None:
                values.add(self.neighbours[direction].value)
        return values
    
    def neighbour_cells(self, direction_list):
        cells = set()
        for direction in direction_list:
            if self.neighbours[direction] is not None:
                cells.add(self.neighbours[direction])
        return cells

    def neighbour_cells_generator(self, direction_list):
        for direction in direction_list:
            if self.neighbours[direction] is not None:
                yield self.neighbours[direction] 

    def neighbour_cells_in_list(self, direction_list, cell_list):
        cells = set()
        for direction in direction_list:
            if self.neighbours[direction] is not None:
                if self.neighbours[direction] in cell_list:
                    cells.add(self.neighbours[direction])
        return cells

    def change_value(self, new_value):
        self.value_history.append(self.value)
        self.value = new_value

    def coords(self):
        return (self.x, self.y)

class Board:
    def __init__(self, data, parse_as_int = False):
        self.cells = {}
        self.values = set()
        self.max_y = 0
        self.max_x = 0
        for y, line in enumerate(data):
            if y > self.max_y:
                self.max_y = y
            self.cells[y] = {}
            for x, value in enumerate(line):
                if parse_as_int:
                    value = int(value)
                if x > self.max_x:
                    self.max_x = x
                self.values.add(value)
                cell = Cell(x,y,value)
                self.cells[y][x] = cell
        for v in self.cells.values():
            for cell in v.values():
                cell.connect_neighbours(self.cells)
        self.edges = {
            "top": set((x, 0) for x in range(self.max_x + 1)),
            "right": set((self.max_x, y) for y in range(self.max_y + 1)),
            "bottom": set((x, self.max_y) for x in range(self.max_x + 1)),
            "left": set((0, y) for y in range(self.max_y + 1)),
        }

    def start_coords(self, direction):
        if direction == 0:
            return set.union(self.edges["bottom"], self.edges["right"])
        if direction == 1:
            return self.edges["bottom"]
        if direction == 2:
            return set.union(self.edges["bottom"], self.edges["left"])
        if direction == 3:
            return self.edges["left"]
        if direction == 4:
            return set.union(self.edges["top"], self.edges["left"])
        if direction == 5:
            return self.edges["top"]
        if direction == 6:
            return set.union(self.edges["top"], self.edges["right"])
        if direction == 7:
            return self.edges["right"]

    def cell_at(self, x, y):
        if x < 0 or x > self.max_x:
            return None
        if y < 0 or y > self.max_y:
            return None
        return self.cells[y][x]

    def walk(self):
        values = []
        for direction in directions.keys():
            coords = self.start_coords(direction)
            for coord in coords:
                cell = self.cells[coord[1]][coord[0]]
                value = cell.value
                while((cell := cell.neighbours[direction]) != None):
                    value += cell.value
                values.append(value)
        return values
    
    def all_cells(self, *values):
        for a in self.cells.values():
            for b in a.values():
                if values == [] or b.value in values:
                    yield b

    def reset(self):
        for a in self.cells.values():
            for b in a.values():
                b.value = b.initial_value
                b.value_history = []

    def wrap_edges(self):
        for x in range(self.max_x + 1):
            self.cell_at(x, 0).neighbours[1] = self.cell_at(x, self.max_y)
            self.cell_at(x, self.max_y).neighbours[5] = self.cell_at(x, 0)

        for y in range(self.max_y + 1):
            self.cell_at(0, y).neighbours[7] = self.cell_at(self.max_x, y)
            self.cell_at(self.max_x, y).neighbours[3] = self.cell_at(0, y)
