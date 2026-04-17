from Core.grid import Grid
from Core.rules import Rules

class Engine:
    def __init__(self, width=40, height=25, rule=Rules.conway):
        self.grid = Grid(width, height)
        self.rule = rule
        self.generation = 0

    def count_neighbors(self, x, y):
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),          (0, 1),
            (1, -1),  (1, 0), (1, 1)
        ]

        count = 0
        for dx, dy in directions:
            count += self.grid.get(x + dx, y + dy)

        return count
    def insert_pattern(self, pattern, x, y):
        """
        Inject a pattern into the grid at position (x, y)
        """
        for dx, dy in pattern:
            self.grid.set(x + dx, y + dy, 1)
    def step(self):
        """
        CORE ITERATION ENGINE
        This is where the simulation evolves
        """
        new_grid = self.grid.copy()

        for i in range(self.grid.height):
            for j in range(self.grid.width):
                neighbors = self.count_neighbors(i, j)
                current = self.grid.get(i, j)

                new_state = self.rule(current, neighbors)
                new_grid.set(i, j, new_state)

        self.grid = new_grid
        self.generation += 1