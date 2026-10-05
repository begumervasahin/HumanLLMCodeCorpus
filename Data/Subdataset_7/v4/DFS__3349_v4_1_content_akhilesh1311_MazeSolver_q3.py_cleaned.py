from b3 import Maze
from maze_solver import DFSSolver
import matplotlib.pyplot as plt
import time
import pickle
b1 = [x / 10 for x in range(1, 10)]
a1 = 1000
b2 = {p: 0 for p in b1}
for p in b1:
    a2 = 0
    for _ in range(100):
        b3 = Maze(a1, p)
        b4 = DFSSolver(b3)
        b5 = time.time()
        b4.display_solution(b6 = False)
        b7 = time.time() - b5
        if b4.is_solvable:
            b2[p] += 1
            a2 += 1
            b8 = f"../mazes/{a1}x{a1}_{p}_{a2:03}.p"
            with open(b8, 'wb') as f:
                pickle.dump(b3, f, pickle.HIGHEST_PROTOCOL)
            print(f"Maze ({a1}, {p}) solved in {b7:.2f} seconds.")
        else:
            print(f"Maze ({a1}, {p}) not solvable..")
    print(f"Probability {p}: {b2[p]} out of 100 mazes were solvable.")
b9 = [b2[p] for p in b1]
plt.plot(b1, b9)
plt.xlabel("Probability (p-value)")
plt.ylabel("Number of Solvable Mazes")
plt.title("Solvability Rate vs. Probability")
plt.savefig("solvability_vs_probability.png")
plt.show()