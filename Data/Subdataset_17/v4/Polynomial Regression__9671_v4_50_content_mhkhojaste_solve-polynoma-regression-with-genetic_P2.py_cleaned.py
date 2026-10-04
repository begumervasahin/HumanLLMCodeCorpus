import numpy as np
import pandas as pd
class GeneticAlgorithm:
    def __init__(self):
        self.num_generations = 10000
        self.population_size = 50
        self.tournament_size = 2
        self.mutation_rate = 0.1
        self.sigma = 1
        self.X_array = np.arange(1, 101)
        data = pd.read_csv("my_numbers.csv")
        self.Y_array = data["Y"].values
        self.degree = 4
    def set_attributes(self, mutation_rate, sigma):
        self.mutation_rate = mutation_rate
        self.sigma = sigma
    def create_initial_population(self):
        return np.random.uniform(low=0, high=1, size=(self.population_size, self.degree))
    def calculate_fitness(self, population):
        fitness = np.zeros(len(population))
        for i in range(population.shape[0]):
            predicted_y = (
                population[i][0] * np.power(self.X_array, 3) +
                population[i][1] * np.power(self.X_array, 2) +
                population[i][2] * self.X_array +
                population[i][3]
            )
            fitness[i] = 1 / (1 + np.sum(np.power(predicted_y - self.Y_array, 2)) / len(predicted_y))
        return fitness
    def select_parents(self, population, fitness):
        selected_parents = np.zeros((10, self.degree))
        for i in range(10):
            indices = np.random.choice(len(population), self.tournament_size, replace=False)
            tournament_fitness = fitness[indices]
            winner_index = indices[np.argmax(tournament_fitness)]
            selected_parents[i] = population[winner_index]
        return selected_parents
    def crossover(self, parents):
        children = []
        num_parents = len(parents)
        for i in range(num_parents):
            for j in range(i + 1, num_parents):
                parent1 = parents[i]
                parent2 = parents[j]
                child = np.zeros(self.degree)
                selected_genes = np.random.choice(self.degree, self.degree
                child[selected_genes] = parent1[selected_genes]
                child[~selected_genes] = parent2[~selected_genes]
                child = self.mutate(child)
                children.append(child)
        return np.asarray(children)
    def mutate(self, child):
        for gene_index in range(len(child)):
            if np.random.rand() <= self.mutation_rate:
                child[gene_index] += np.random.normal(0, self.sigma)
        return child