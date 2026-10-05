from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import copy
from individual import Individual
import random
class EvolutiveKNN:
    def __init__(self, training_examples, training_labels, test_size=0.33):
        self._create_test_set(training_examples, training_labels, test_size)
    def train(self, population_size=50, mutation_rate=0.02, max_generations=50, max_accuracy=1.0, max_k=None, max_weight=10, elitism_rate=0.02, tournament_size=0.25):
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.max_generations = max_generations
        self.max_accuracy = max_accuracy
        self.max_k = max_k
        self.max_weight = max_weight
        self.elitism_rate = elitism_rate
        self.elitism_real_value = int(self.elitism_rate * self.population_size)
        self.tournament_size = tournament_size
        self.global_best = Individual(1, [1])
        self.hall_of_fame = []
        self.best_of_each_generation = []
        self._train()
    def _train(self):
        population = self._initialize_population()
        generations = 0
        self._calculate_fitness_of_population(population, generations)
        while not self._should_stop(generations):
            generations += 1
            population = self._create_new_population(population)
            self._calculate_fitness_of_population(population, generations)
    def _should_stop(self, generations):
        return generations >= self.max_generations or self.global_best.fitness >= self.max_accuracy
    def _create_new_population(self, old_population):
        sorted_old_population = sorted(old_population, key=lambda individual: individual.fitness, reverse=True)
        elite = self._get_elite(sorted_old_population)
        non_elite = self._get_non_elite(sorted_old_population)
        new_population = elite
        while len(new_population) < self.population_size:
            new_population.append(self._generate_child(non_elite))
        return new_population
    def _generate_child(self, population):
        parent1 = self._tournament_selection(population)
        parent2 = self._tournament_selection(population)
        kid = self._crossover(parent1, parent2)
        return kid
    def _tournament_selection(self, population):
        num_selected = int(len(population) * self.tournament_size)
        selected = random.sample(range(len(population)), num_selected)
        return max(selected, key=lambda idx: population[idx].fitness)
    def _crossover(self, parent1, parent2):
        k1, k2 = parent1.k, parent2.k
        k = random.choice([k1, k2])
        weights = parent1.weights[:k] + parent2.weights[k:]
        if random.uniform(0, 1) < self.mutation_rate:
            weights = self._mutate_weights(weights)
        return Individual(k, weights)
    def _mutate_weights(self, weights):
        mutated_weights = weights[:]
        idx = random.randint(0, len(weights) - 1)
        mutated_weights[idx] = random.randint(0, self.max_weight)
        return mutated_weights
    def _get_elite(self, population):
        return population[:self.elitism_real_value]
    def _get_non_elite(self, population):
        return population[self.elitism_real_value:]
    def _initialize_population(self):
        max_k = self.max_k if self.max_k is not None else len(self.training_labels)
        population = []
        for _ in range(self.population_size):
            k = random.randint(1, max_k)
            weights = [random.choice(range(self.max_weight)) for _ in range(k)]
            population.append(Individual(k, weights))
        return population
    def _calculate_fitness_of_population(self, population, generation):
        population_best = Individual(1, [1])
        for individual in population:
            self._calculate_fitness_of_individual(individual)
            if individual.fitness > population_best.fitness:
                population_best = copy.deepcopy(individual)
        self.best_of_each_generation.append(population_best)
        if population_best.fitness > self.global_best.fitness:
            self._update_global_best(population_best, generation)
    def _update_global_best(self, individual, generation):
        self.hall_of_fame.append({'individual': individual, 'generation': generation})
        self.global_best = individual
    def _calculate_fitness_of_individual(self, individual):
        def _weights(distances):
            return individual.weights
        knn = KNeighborsClassifier(n_neighbors=individual.k, weights=_weights)
        knn.fit(self.training_examples, self.training_labels)
        individual.fitness = knn.score(self.test_examples, self.test_labels)
    def _create_test_set(self, training_examples, training_labels, test_size):
        test_indices = random.sample(range(len(training_labels)), test_size)
        self.test_examples = training_examples[test_indices]
        self.test_labels = training_labels[test_indices]
        self.training_examples = np.delete(training_examples, test_indices, axis=0)
        self.training_labels = np.delete(training_labels, test_indices)
if __name__ == '__main__':
    training_examples = np.random.rand(100, 5)
    training_labels = np.random.randint(0, 2, size=100)
    evol_knn = EvolutiveKNN(training_examples, training_labels)
    evol_knn.train()