import random as rd
import numpy as np
import time
from Graph import Graph
def calculate_cost(solution, graph):
    total_cost = 0
    for i in range(len(solution) - 1):
        total_cost += graph.costs[solution[i], solution[i + 1]]
    return total_cost
def compare_solutions(sol1, sol2, graph):
    return calculate_cost(sol1, graph) - calculate_cost(sol2, graph)
def perturb_solution(solution, graph, temperature):
    new_solution = exchange(solution)
    cost_difference = compare_solutions(new_solution, solution, graph)
    if cost_difference < 0:
        return new_solution
    else:
        acceptance_probability = np.exp(-cost_difference / temperature)
        if rd.random() < acceptance_probability:
            return new_solution
        else:
            return solution
def exchange(solution):
    new_solution = solution.copy()
    indices = list(range(1, len(solution) - 2))
    i, j = rd.sample(indices, 2)
    new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
    return new_solution
def main():
    num_nodes = 17
    graph = Graph("N17.data")
    total_cost = 0
    total_time = 0
    for _ in range(10):
        initial_solution = [i for i in range(1, num_nodes)]
        rd.shuffle(initial_solution)
        solution = [0] + initial_solution + [0]
        temperature = 1000
        start_time = time.time()
        while temperature > 5:
            for _ in range(num_nodes ** 2):
                solution = perturb_solution(solution, graph, temperature)
            temperature *= 0.98
        elapsed_time = time.time() - start_time
        print(solution)
        total_cost += calculate_cost(solution, graph)
        total_time += elapsed_time
    print(f"Average cost: {total_cost / 10}")
    print(f"Average time: {total_time / 10:.2f} seconds")
if __name__ == '__main__':
    main()