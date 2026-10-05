import random
from collections import defaultdict
DEAD_CELL, LIVE_CELL = '-', '*'
class GameOfLife:
    def __init__(self, cell_count=(3, 3)):
        self.cell_count = cell_count
        self.universe = defaultdict(int)
    def initialize_universe(self, alive_cells):
        for cell in alive_cells:
            self.universe[cell] = 1
    def display_generation(self):
        print("\nGeneration:")
        for row in range(self.cell_count[1]):
            print("  ", ''.join(str(self.universe[(row, col)]) for col in range(self.cell_count[0])).replace(
                '0', DEAD_CELL).replace('1', LIVE_CELL))
    def compute_next_generation(self, cell_table):
        next_generation = defaultdict(int)
        for row in range(self.cell_count[1]):
            for col in range(self.cell_count[0]):
                current_state = self.universe[(row, col)]
                neighbor_sum = sum(self.universe[(r, c)] for r in range(row - 1, row + 2)
                                   for c in range(col - 1, col + 2)) - current_state
                next_state = cell_table[(current_state, neighbor_sum)]
                next_generation[(row, col)] = next_state
        self.universe = next_generation
def main():
    max_generations = 3
    cell_count = (3, 3)
    cell_table = defaultdict(int, {
        (1, 2): 1,
        (1, 3): 1,
        (0, 3): 1,
    })
    game = GameOfLife(cell_count)
    alive_cells = [(random.randint(0, cell_count[0]-1), random.randint(0, cell_count[1]-1)) for _ in range(5)]
    game.initialize_universe(alive_cells)
    for generation in range(max_generations):
        game.display_generation()
        game.compute_next_generation(cell_table)
if __name__ == "__main__":
    main()