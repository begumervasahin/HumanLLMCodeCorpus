from maze import Maze
from maze_solver import AStarSolver, DFSSolver, BFSSolver
import matplotlib.pyplot as plt
import time
import pickle
b1 = [x/10 for x in range(1,10)]
a1 = 1000
b2 = {p:0 for p in b1}
b3 = []
for p in b1:
    a2 = 0
    b3 = []
    b4 = []
    for i in range(0, 100):
        b5 = Maze(a1, p)
        b6 = DFSSolver(b5)
        b7 = time.time()
        b6.display_solution(b8 = False)
        b9 = time.time() - b7
        if b6.b10 = = True:
            b2[p] += 1
            a2 += 1
            with open(f"../mazes/{a1}x{a1}_{p}_{a2:03}.p",'wb') as f:
                pickle.dump(b5, f, pickle.HIGHEST_PROTOCOL)
            print(f"maze({b5.a1},{b5.p}) solved in {b9}b6.")
        else:
            print(f"maze({b5.a1},{b5.p}) not b2..")
    print(f"{p}: {b2[p]}")
b11 = [b2[p] for p in b1]
plt.plot(b1, b11)
plt.xlabel("p-value")
plt.ylabel("P(Solvable)")
plt.savefig("q3.png")
plt.show()