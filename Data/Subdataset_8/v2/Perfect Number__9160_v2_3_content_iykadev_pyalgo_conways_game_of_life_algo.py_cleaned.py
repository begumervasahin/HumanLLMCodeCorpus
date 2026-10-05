import random
from collections import defaultdict
print_dead, print_live = '-', '*'
max_generations = 3
cell_count = (3, 3)
cell_table = defaultdict(int, {
    (1, 2): 1,
    (1, 3): 1,
    (0, 3): 1,
})
universe = defaultdict(int)
universe[(1, 0)], universe[(1, 1)], universe[(1, 2)] = 1, 1, 1
for generation in range(max_generations):
    print("\nGeneration %3i:" % (generation,))
    for row in range(cell_count[1]):
        print("  ", ''.join(str(universe[(row, col)]) for col in range(cell_count[0])).replace(
            '0', print_dead).replace('1', print_live))
    next_generation = defaultdict(int)
    for row in range(cell_count[1]):
        for col in range(cell_count[0]):
            next_generation[(row, col)] = cell_table[
                (universe[(row, col)],
                 -universe[(row, col)] + sum(universe[(r, c)]
                                             for r in range(row - 1, row + 2)
                                             for c in range(col - 1, col + 2))
                 )]
    universe = next_generation