import random

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[0]*width for _ in range(height)]

    def clear(self):
        self.grid = [[0]*self.width for _ in range(self.height)]

    def random_fill(self):
        for y in range(self.height):
            for x in range(self.width):
                self.grid[y][x] = random.choice([0, 1])

    def get_live_cells(self):
        return [(x, y) for y in range(self.height) for x in range(self.width) if self.grid[y][x] == 1]

    def set_live_cells(self, cells):
        self.clear()
        for x, y in cells:
            if 0 <= x < self.width and 0 <= y < self.height:
                self.grid[y][x] = 1

    def count_neighbors(self, x, y):
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),          (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]
        count = 0
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.width and 0 <= ny < self.height:
                count += self.grid[ny][nx]
        return count

    def next_generation(self):
        new_grid = [[0]*self.width for _ in range(self.height)]
        for y in range(self.height):
            for x in range(self.width):
                neighbors = self.count_neighbors(x, y)
                if self.grid[y][x] == 1:
                    if neighbors in [2, 3]:
                        new_grid[y][x] = 1
                else:
                    if neighbors == 3:
                        new_grid[y][x] = 1
        self.grid = new_grid
