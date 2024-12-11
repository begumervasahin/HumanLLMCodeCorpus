from maze import Maze
from maze_solver import AStarSolver, DFSSolver, BFSSolver
import matplotlib.pyplot as plt
import time
import pickle
b1 = [x / 10 for x in range(1, 10)]
a1 = 1000
b2 = {p: 0 for p in b1}
for p in b1:
    a2 = 0
    for i in range(100):
        b3 = Maze(a1, p)
        b4 = DFSSolver(b3)
        b5 = time.time()
        b4.display_solution(b6 = False)
        b7 = time.time() - b5
        if b4.is_solvable:
            b2[p] += 1
            a2 += 1
            with open(f"../mazes/{a1}x{a1}_{p}_{a2:03}.p", 'wb') as f:
                pickle.dump(b3, f, pickle.HIGHEST_PROTOCOL)
            print(f"Maze ({b3.a1}, {b3.p}) solved in {b7}b4.")
        else:
            print(f"Maze ({b3.a1}, {b3.p}) not b2..")
    print(f"{p}: {b2[p]}")
b8 = [b2[p] for p in b1]
plt.plot(b1, b8)
plt.xlabel("p-value")
plt.ylabel("P(Solvable)")
plt.savefig("q3.png")
plt.show()