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
    
    def change_value(self, new_value):
        self.value_history.append(self.value)
        self.value = new_value

class Board:
    def __init__(self, data):
        self.cells = {}
        self.max_y = 0
        self.max_x = 0
        for y, line in enumerate(data):
            if y > self.max_y:
                self.max_y = y
            self.cells[y] = {}
            for x, value in enumerate(line):
                if x > self.max_x:
                    self.max_x = x
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
