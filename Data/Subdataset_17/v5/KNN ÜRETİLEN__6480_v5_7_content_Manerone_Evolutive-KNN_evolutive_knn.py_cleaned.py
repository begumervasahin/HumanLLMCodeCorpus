from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import copy
import random
from individual import Individual
class EvolutiveKNN:
    def __init__(self, training_examples, training_labels, ts_size=0.33):
        test_size = int(ts_size * len(training_labels))
        self._create_test(np.array(training_examples), np.array(training_labels), test_size)
    def train(self, population_size=50, mutation_rate=0.02, max_generations=50, max_accuracy=1.0, max_k=None, max_weight=10, elitism_rate=0.02, tournament_size=0.25):
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.max_generations = max_generations
        self.max_accuracy = max_accuracy
        self.max_k = max_k if max_k is not None else len(self.training_labels)
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
        self._evaluate_population(population, generations)
        while not self._should_stop(generations):
            generations += 1
            population = self._create_new_population(population)
            self._evaluate_population(population, generations)
    def _should_stop(self, generations):
        return generations >= self.max_generations or self.global_best.fitness >= self.max_accuracy
    def _create_new_population(self, old_population):
        sorted_old_population = sorted(old_population, key=lambda individual: individual.fitness, reverse=True)
        elite = self._get_elite(sorted_old_population)
        non_elite = self._get_non_elite(sorted_old_population)
        new_population = elite[:]
        while len(new_population) < self.population_size:
            new_population.append(self._generate_child(non_elite))
        return new_population
    def _generate_child(self, population):
        parent1 = self._select_parent(population)
        parent2 = self._select_parent(population)
        child = self._crossover(parent1, parent2)
        return child
    def _select_parent(self, population):
        tournament_size = int(len(population) * self.tournament_size)
        selected = random.sample(population, tournament_size)
        best = max(selected, key=lambda individual: individual.fitness)
        return best
    def _crossover(self, parent1, parent2):
        k = random.choice([parent1.k, parent2.k])
        collaboration1 = int(np.floor(k * (parent1.k / float(parent1.k + parent2.k))))
        collaboration2 = k - collaboration1
        weights_p1 = random.sample(parent1.weights, collaboration1)
        weights_p2 = random.sample(parent2.weights, collaboration2)
        weights = weights_p1 + weights_p2
        if random.uniform(0, 1) < self.mutation_rate:
            weights = self._mutate_weights(weights)
        return Individual(k, weights)
    def _mutate_weights(self, weights):
        index = random.randint(0, len(weights) - 1)
        weights[index] = random.randint(1, self.max_weight)
        return weights
    def _get_elite(self, population):
        return population[:self.elitism_real_value]
    def _get_non_elite(self, population):
        return population[self.elitism_real_value:]
    def _initialize_population(self):
        population = []
        for _ in range(self.population_size):
            k = random.randint(1, self.max_k)
            weights = [random.randint(1, self.max_weight) for _ in range(k)]
            population.append(Individual(k, weights))
        return population
    def _evaluate_population(self, population, generation):
        population_best = Individual(1, [1])
        for individual in population:
            self._evaluate_individual(individual)
            if population_best.fitness < individual.fitness:
                population_best = copy.deepcopy(individual)
        self.best_of_each_generation.append(population_best)
        if self.global_best.fitness < population_best.fitness:
            self._update_global_best(population_best, generation)
    def _update_global_best(self, individual, generation):
        self.hall_of_fame.append({'individual': individual, 'generation': generation})
        self.global_best = individual
    def _evaluate_individual(self, individual):
        def _element_weights(distances):
            return individual.weights
        kneigh = KNeighborsClassifier(n_neighbors=individual.k, weights=_element_weights)
        kneigh.fit(self.training_examples, self.training_labels)
        individual.fitness = kneigh.score(self.test_examples, self.test_labels)
    def _create_test(self, tr_examples, tr_labels, test_size):
        test_indexes = random.sample(range(len(tr_labels)), test_size)
        self.test_examples = tr_examples[test_indexes]
        self.test_labels = tr_labels[test_indexes]
        self.training_examples = np.array([tr_examples[i] for i in range(len(tr_labels)) if i not in test_indexes])
        self.training_labels = np.array([tr_labels[i] for i in range(len(tr_labels)) if i not in test_indexes])
if __name__ == '__main__':
    N = 1000
    split_idxs = cv_with_shuffling(N)