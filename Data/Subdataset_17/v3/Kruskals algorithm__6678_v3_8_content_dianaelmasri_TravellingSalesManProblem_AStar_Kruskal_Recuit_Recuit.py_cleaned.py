import random
import numpy as np
import time
class Graph:
    def __init__(self, file_name: str):
        self.costs = self._load_graph(file_name)
    def _load_graph(self, file_name: str) -> np.ndarray:
        with open(file_name, 'r') as file:
            return np.array([list(map(int, line.split())) for line in file])
def calculate_cost(solution: list[int], graph: Graph) -> int:
    return sum(graph.costs[solution[i], solution[i + 1]] for i in range(len(solution) - 1))
def compare_solutions(sol1: list[int], sol2: list[int], graph: Graph) -> int:
    return calculate_cost(sol1, graph) - calculate_cost(sol2, graph)
def perform_annealing_step(solution: list[int], graph: Graph, temperature: float) -> list[int]:
    new_solution = _exchange_elements(solution)
    cost_diff = compare_solutions(new_solution, solution, graph)
    if cost_diff < 0 or random.random() < np.exp(-cost_diff / temperature):
        return new_solution
    return solution
def _exchange_elements(solution: list[int]) -> list[int]:
    new_solution = solution.copy()
    indices = list(range(1, len(solution) - 1))
    i, j = random.sample(indices, 2)
    new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
    return new_solution
def simulated_annealing(graph: Graph, num_iterations: int = 10, initial_temperature: float = 1000.0, min_temperature: float = 5.0, cooling_rate: float = 0.98) -> tuple[float, float]:
    total_cost = 0
    total_time = 0
    num_nodes = graph.costs.shape[0]
    for _ in range(num_iterations):
        initial_solution = _generate_initial_solution(num_nodes)
        current_solution = initial_solution
        temperature = initial_temperature
        start_time = time.time()
        while temperature > min_temperature:
            for _ in range(num_nodes ** 2):
                current_solution = perform_annealing_step(current_solution, graph, temperature)
            temperature *= cooling_rate
        elapsed_time = time.time() - start_time
        total_cost += calculate_cost(current_solution, graph)
        total_time += elapsed_time
        print(f"Solution: {current_solution}, Cost: {calculate_cost(current_solution, graph)}")
    return total_cost / num_iterations, total_time / num_iterations
def _generate_initial_solution(num_nodes: int) -> list[int]:
    return [0] + random.sample(range(1, num_nodes), num_nodes - 1) + [0]
def main():
    graph = Graph("N17.data")
    average_cost, average_time = simulated_annealing(graph)
    print(f"Average cost: {average_cost}")
    print(f"Average time: {average_time:.2f} seconds")
if __name__ == '__main__':
    main()