import random as rd
import numpy as np
import time
class Graph:
    def __init__(self, file_name):
        self.costs = self.load_graph(file_name)
    def load_graph(self, file_name):
        with open(file_name, 'r') as file:
            lines = file.readlines()
            matrix = []
            for line in lines:
                row = list(map(int, line.split()))
                matrix.append(row)
            return np.array(matrix)
def calculate_cost(sol, g):
    res = 0
    for i in range(len(sol) - 1):
        res += g.costs[sol[i], sol[i + 1]]
    return res
def compare_solution(sol1, sol2, g):
    return calculate_cost(sol1, g) - calculate_cost(sol2, g)
def change_solution(sol, g, temp):
    sol2 = exchange(sol)
    delta = compare_solution(sol2, sol, g)
    if delta < 0:
        return sol2
    else:
        a = rd.random()
        if a < np.exp(-delta / temp):
            return sol2
        else:
            return sol
def exchange(sol):
    sol2 = sol.copy()
    possible = list(range(1, len(sol) - 2))
    i = rd.choice(possible)
    possible.remove(i)
    j = rd.choice(possible)
    sol2[i], sol2[j] = sol2[j], sol2[i]
    return sol2
def main():
    N = 17
    g = Graph("N17.data")
    total_cost = 0
    total_time = 0
    for k in range(10):
        s = [i for i in range(1, N)]
        rd.shuffle(s)
        sol = [0] + s + [0]
        T0 = 1000
        start_time = time.time()
        while T0 > 5:
            for i in range(N ** 2):
                sol = change_solution(sol, g, T0)
            T0 *= 0.98
        elapsed_time = time.time() - start_time
        print(sol)
        total_cost += calculate_cost(sol, g)
        total_time += elapsed_time
    print(f"Average cost: {total_cost / 10}")
    print(f"Average time: {total_time / 10:.2f} seconds")
if __name__ == '__main__':
    main()