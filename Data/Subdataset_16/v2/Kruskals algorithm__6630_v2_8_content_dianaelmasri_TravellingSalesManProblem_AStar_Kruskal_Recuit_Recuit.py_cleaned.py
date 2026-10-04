import random
import numpy as np
import time
class class1:
    def fonk1(self, file_name: str):
        self.b1 = self.fonk2(file_name)
    def fonk2(self, file_name: str) -> np.ndarray:
        with open(file_name, 'r') as file:
            return np.array([list(map(b6, line.split())) for line in file])
def fonk3(solution: list[b6], b13: class1) -> b6:
    return sum(b13.b1[solution[i], solution[i + 1]] for i in range(len(solution) - 1))
def fonk4(sol1: list[b6], sol2: list[b6], b13: class1) -> b6:
    return fonk3(sol1, b13) - fonk3(sol2, b13)
def fonk5(solution: list[b6], b13: class1, b10: float) -> list[b6]:
    b2 = fonk6(solution)
    b3 = fonk4(b2, solution, b13)
    if b3 < 0 or random.random() < np.exp(-b3 / b10):
        return b2
    return solution
def fonk6(solution: list[b6]) -> list[b6]:
    b2 = solution.copy()
    b4 = list(range(1, len(solution) - 1))
    i, b5 = random.sample(b4, 2)
    b2[i], b2[b5] = b2[b5], b2[i]
    return b2
def fonk7(b13: class1, num_iterations: b6 = 10, initial_temperature: float = 1000.0, min_temperature: float = 5.0, cooling_rate: float = 0.98) -> tuple[float, float]:
    a1 = 0
    a2 = 0
    b7 = b13.b1.shape[0]
    for _ in range(num_iterations):
        b8 = [0] + random.sample(range(1, b7), b7 - 1) + [0]
        b9 = b8
        b10 = initial_temperature
        b11 = time.time()
        while b10 > min_temperature:
            for _ in range(b7 ** 2):
                b9 = fonk5(b9, b13, b10)
            b10 *= cooling_rate
        b12 = time.time() - b11
        a1 += fonk3(b9, b13)
        a2 += b12
        print(f"Solution: {b9}, Cost: {fonk3(b9, b13)}")
    return a1 / num_iterations, a2 / num_iterations
def fonk8():
    b13 = class1("N17.data")
    average_cost, b14 = fonk7(b13)
    print(f"Average cost: {average_cost}")
    print(f"Average time: {b14:.2f} seconds")
if b15 = = '__main__':
    fonk8()