from maze import Maze
from maze_solver import DFSSolver
import matplotlib.pyplot as plt
import time
import pickle
p_values = [x / 10 for x in range(1, 10)]
maze_dimension = 1000
solvable_counts = {p: 0 for p in p_values}
for p in p_values:
    count = 0
    for _ in range(100):
        maze = Maze(maze_dimension, p)
        solver = DFSSolver(maze)
        start_time = time.time()
        solver.display_solution(display=False)
        solving_time = time.time() - start_time
        if solver.is_solvable:
            solvable_counts[p] += 1
            count += 1
            maze_file_name = f"../mazes/{maze_dimension}x{maze_dimension}_{p}_{count:03}.p"
            with open(maze_file_name, 'wb') as f:
                pickle.dump(maze, f, pickle.HIGHEST_PROTOCOL)
            print(f"Maze ({maze_dimension}, {p}) solved in {solving_time:.2f} seconds.")
        else:
            print(f"Maze ({maze_dimension}, {p}) is not solvable.")
    print(f"For p={p}, {solvable_counts[p]} out of 100 mazes were solvable.")
solvable_counts_list = [solvable_counts[p] for p in p_values]
plt.plot(p_values, solvable_counts_list)
plt.xlabel("Probability (p-value)")
plt.ylabel("Number of Solvable Mazes")
plt.title("Solvability Rate vs. Probability")
plt.savefig("solvability_vs_probability.png")
plt.show()