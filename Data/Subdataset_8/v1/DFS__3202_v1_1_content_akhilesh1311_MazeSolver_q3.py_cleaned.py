from maze import Maze
from maze_solver import AStarSolver, DFSSolver, BFSSolver
import matplotlib.pyplot as plt
import time
import pickle
pvals = [x / 10 for x in range(1, 10)]
dim = 1000
solvable = {p: 0 for p in pvals}
for p in pvals:
    count = 0
    for i in range(100):
        m = Maze(dim, p)
        s = DFSSolver(m)
        t0 = time.time()
        s.display_solution(display=False)
        td = time.time() - t0
        if s.is_solvable:
            solvable[p] += 1
            count += 1
            with open(f"../mazes/{dim}x{dim}_{p}_{count:03}.p", 'wb') as f:
                pickle.dump(m, f, pickle.HIGHEST_PROTOCOL)
            print(f"Maze ({m.dim}, {m.p}) solved in {td}s.")
        else:
            print(f"Maze ({m.dim}, {m.p}) not solvable..")
    print(f"{p}: {solvable[p]}")
counts = [solvable[p] for p in pvals]
plt.plot(pvals, counts)
plt.xlabel("p-value")
plt.ylabel("P(Solvable)")
plt.savefig("q3.png")
plt.show()