import numpy as np
import pandas as pd
class GeneticAlgorithm:
    def __init__(self, csv_file="my_numbers.csv"):
        self.number_of_generations = 10000
        self.population_size = 50
        self.tournament_size = 2
        self.mutation_rate = 0.1
        self.sigma = 1
        self.degree = 4
        self.X_array = np.arange(1, 101)
        data = pd.read_csv(csv_file)
        self.Y_array = data["Y"].values
    def set_parameters(self, mutation_rate, sigma):
        self.mutation_rate = mutation_rate
        self.sigma = sigma
    def create_initial_population(self):
        return np.random.uniform(low=0, high=1, size=(self.population_size, self.degree))
    def calculate_fitness(self, population):
        fitness = np.zeros(len(population))
        for i in range(population.shape[0]):
            y_pred = (
                population[i][0] * np.power(self.X_array, 3) +
                population[i][1] * np.power(self.X_array, 2) +
                population[i][2] * self.X_array +
                population[i][3]
            )
            error = np.sum(np.power(y_pred - self.Y_array, 2)) / len(y_pred)
            fitness[i] = 1 / (1 + error)
        return fitness
    def select_parents(self, population, fitness):
        selected_parents = np.zeros((10, self.degree))
        for i in range(10):
            random_indices = np.random.choice(len(population), size=self.tournament_size, replace=False)
            tournament_fitness = fitness[random_indices]
            best_index = random_indices[np.argmax(tournament_fitness)]
            selected_parents[i] = population[best_index]
        return selected_parents
    def perform_crossover_and_mutation(self, parents):
        children = []
        for i in range(len(parents)):
            for j in range(i + 1, len(parents)):
                parent1 = parents[i]
                parent2 = parents[j]
                selected_indices = np.random.choice(self.degree, self.degree, replace=False)
                child = [parent1[selected_indices[0]], parent1[selected_indices[1]],
                         parent2[selected_indices[2]], parent2[selected_indices[3]]]
                for k in range(self.degree):
                    if np.random.rand() <= self.mutation_rate:
                        child[k] += np.random.normal(0, self.sigma)
                children.append(child)
        return np.asarray(children)
if __name__ == "__main__":
    ga = GeneticAlgorithm()
    ga.set_parameters(0.2, 0.5)
    population = ga.create_initial_population()
    print("Initial Population:\n", population)
    fitness = ga.calculate_fitness(population)
    print("Fitness Scores:\n", fitness)
    parents = ga.select_parents(population, fitness)
    print("Selected Parents:\n", parents)
    children = ga.perform_crossover_and_mutation(parents)
    print("Children:\n", children)