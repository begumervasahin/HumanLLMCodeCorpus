import numpy as np
import pandas as pd
class Algorithm:
    def __init__(self):
        self.numberOfGenerations = 10000
        self.populationSize = 50
        self.tornumentSize = 2
        self.mutationRate = 0.1
        self.sigma = 1
        self.X_array = np.arange(1, 101)
        data = pd.read_csv("my_numbers.csv")
        self.Y_array = data["Y"].values
        self.degree = 4
    def set_att(self, mutation_rate, sigma):
        self.mutationRate = mutation_rate
        self.sigma = sigma
    def create_first_population(self):
        return np.random.uniform(low=0, high=1, size=(self.populationSize, self.degree))
    def calculate_fitness(self, population):
        fitness = np.zeros(len(population))
        for i in range(population.shape[0]):
            my_y = (
                population[i][0] * np.power(self.X_array, 3) +
                population[i][1] * np.power(self.X_array, 2) +
                population[i][2] * self.X_array +
                population[i][3]
            )
            error = np.sum(np.power(np.subtract(my_y, self.Y_array), 2)) / len(my_y)
            fitness[i] = 1 / (1 + error)
        return fitness
    def choose_parents(self, population, fitness):
        selected_parents = np.zeros((10, self.degree))
        for i in range(10):
            random_indices = np.random.choice(len(population), size=self.tornumentSize, replace=False)
            tournament_fitness = fitness[random_indices]
            best_index = random_indices[np.argmax(tournament_fitness)]
            selected_parents[i] = population[best_index]
        return selected_parents
    def crossover(self, parents):
        children = []
        for i in range(len(parents)):
            for j in range(i + 1, len(parents)):
                parent1 = parents[i]
                parent2 = parents[j]
                selected = np.random.choice(self.degree, self.degree, replace=False)
                child = [parent1[selected[0]], parent1[selected[1]], parent2[selected[2]], parent2[selected[3]]]
                for k in range(self.degree):
                    if np.random.rand() <= self.mutationRate:
                        child[k] += np.random.normal(0, self.sigma)
                children.append(child)
        return np.asarray(children)
if __name__ == "__main__":
    alg = Algorithm()
    alg.set_att(0.2, 0.5)
    population = alg.create_first_population()
    print("Initial Population:\n", population)
    fitness = alg.calculate_fitness(population)
    print("Fitness Scores:\n", fitness)
    parents = alg.choose_parents(population, fitness)
    print("Selected Parents:\n", parents)
    children = alg.crossover(parents)
    print("Children:\n", children)