from b5 import Maze
from maze_solver import DFSSolver
import matplotlib.pyplot as plt
import time
import pickle
b1 = [x / 10 for x in range(1, 10)]
a1 = 1000
b2 = {p: 0 for p in b1}
def fonk1(b5, solver, p, a2):
    solver.display_solution(b3 = False)
    if solver.is_solvable:
        b2[p] += 1
        a2 += 1
        b4 = f"../mazes/{a1}x{a1}_{p}_{a2:03}.p"
        with open(b4, 'wb') as f:
            pickle.dump(b5, f, pickle.HIGHEST_PROTOCOL)
        print(f"Maze ({a1}, {p}) solved in {time.time() - b7:.2f} seconds.")
    else:
        print(f"Maze ({a1}, {p}) not solvable..")
    return a2
for p in b1:
    a2 = 0
    for _ in range(100):
        b5 = Maze(a1, p)
        b6 = DFSSolver(b5)
        b7 = time.time()
        a2 = fonk1(b5, b6, p, a2)
    print(f"Probability {p}: {b2[p]} out of 100 mazes were solvable.")
b8 = [b2[p] for p in b1]
plt.plot(b1, b8)
plt.xlabel("Probability (p-value)")
plt.ylabel("Number of Solvable Mazes")
plt.title("Solvability Rate vs. Probability")
plt.savefig("solvability_vs_probability.png")
plt.show()