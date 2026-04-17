import random

class Grid:
    def __init__(self, width, height, randomize=True):
        self.width = width
        self.height = height
        self.cells = [
            [random.choice([0, 1]) if randomize else 0 for _ in range(width)]
            for _ in range(height)
        ]

    def get(self, x, y):
        if 0 <= x < self.height and 0 <= y < self.width:
            return self.cells[x][y]
        return 0

    def set(self, x, y, value):
        self.cells[x][y] = value

    def copy(self):
        new_grid = Grid(self.width, self.height, randomize=False)
        new_grid.cells = [row[:] for row in self.cells]
        return new_grid