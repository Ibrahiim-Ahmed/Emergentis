class Metrics:
    @staticmethod
    def population(grid):
        return sum(sum(row) for row in grid.cells)