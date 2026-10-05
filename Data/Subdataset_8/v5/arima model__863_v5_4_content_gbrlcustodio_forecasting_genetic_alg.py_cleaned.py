import random
import copy
import numpy as np
from itertools import combinations
from cromossome import Cromossome
from train_rbfn import train
class GeneticAlgorithm:
    def __init__(self, training_data, test_data):
        self.training_data = training_data
        self.test_data = test_data
        self.population = []
        self.min_size = 2
        self.max_size = len(training_data["INPUT"]) - 1
        self.training_input = np.asarray([[x.tolist()] for x in training_data["INPUT"].values])
        self.training_output = np.asarray([[x.tolist()] for x in training_data["OUTPUT"].values])
    def initialize_population(self, size):
        for _ in range(size):
            individual = Cromossome()
            individual.string = random.sample(range(0, len(self.training_data["INPUT"])), random.randint(self.min_size, self.max_size))
            self.population.append(individual)
    def decode_centers(self, chromosome):
        centers = []
        for center_index in chromosome:
            centers.append([self.training_data["INPUT"].values[center_index].tolist()])
        return np.asarray(centers)
    def evaluate_fitness(self, chromosome):
        network = train(self.training_input, self.training_output, self.decode_centers(chromosome.string))
        chromosome.fitness = [network.aic(self.training_data), network.aic(self.test_data)]
    def evolve(self, generations):
        for generation in range(1, generations + 1):
            print("Generation", generation)
            self.evaluate_population_fitness()
            self.rank_population()
            new_population = []
            while len(new_population) < len(self.population):
                parents = [self.select_individual() for _ in range(2)]
                offspring = self.perform_crossover(parents) if random.random() <= 0.90 else [copy.deepcopy(parent) for parent in parents]
                for child in offspring:
                    self.perform_mutation(child)
                    self.perform_deletion(child)
                    self.perform_addition(child)
                    if child.string != parents[0].string and child.string != parents[1].string:
                        self.evaluate_fitness(child)
                        parents.append(child)
                selected = []
                while len(selected) < 2:
                    for individual in parents:
                        individual.is_optimal = True
                    self.compare_fitness(parents)
                    selected.extend([individual for individual in parents if individual.is_optimal][:2 - len(selected)])
                    parents = [e for e in parents if not e.is_optimal]
                new_population.extend(selected)
            self.population = new_population
        self.mark_optimal_individuals()
        best_individual = [individual for individual in self.population if individual.is_optimal][0]
        print("Best configuration:", self.decode_centers(best_individual.string))
        return train(self.training_input, self.training_output, self.decode_centers(best_individual.string))
    def evaluate_population_fitness(self):
        for individual in self.population:
            self.evaluate_fitness(individual)
    def rank_population(self):
        self.population.sort(key=lambda x: x.fitness[0], reverse=True)
        for i, individual in enumerate(self.population):
            individual.rank = i + 1
    def select_individual(self):
        total_rank = sum(individual.rank for individual in self.population)
        pick = random.uniform(0, total_rank)
        current_sum = 0
        for individual in self.population:
            current_sum += individual.rank
            if current_sum > pick:
                return individual
    def perform_crossover(self, parents):
        smaller_parent, larger_parent = min(parents, key=lambda x: len(x.string)), max(parents, key=lambda x: len(x.string))
        common_genes = set(smaller_parent.string).intersection(larger_parent.string)
        differing_genes = list(set(smaller_parent.string) - common_genes)
        if differing_genes:
            num_genes = random.randint(1, len(differing_genes))
            first_sample = [gene for gene in random.sample(differing_genes, num_genes)]
            differing_genes = list(set(larger_parent.string) - common_genes)
            if differing_genes:
                second_sample = [gene for gene in random.sample(differing_genes, num_genes)]
                for gene1, gene2 in zip(first_sample, second_sample):
                    index1 = smaller_parent.string.index(gene1)
                    index2 = larger_parent.string.index(gene2)
                    smaller_parent.string[index1], larger_parent.string[index2] = larger_parent.string[index2], smaller_parent.string[index1]
        return [copy.deepcopy(smaller_parent), copy.deepcopy(larger_parent)]
    def perform_mutation(self, chromosome):
        for locus in range(len(chromosome.string)):
            if random.random() <= 0.01:
                available_genes = set(range(len(self.training_data["INPUT"]))) - set(chromosome.string)
                new_gene = random.sample(available_genes, 1)[0]
                chromosome.string[locus] = new_gene
    def perform_deletion(self, chromosome):
        if random.random() <= 0.01:
            start_index = random.randint(0, len(chromosome.string) - 1)
            end_index = start_index + random.randint(1, len(chromosome.string) - start_index)
            if (end_index - start_index) == len(chromosome.string):
                end_index -= 1
            chromosome.string = [gene for index, gene in enumerate(chromosome.string) if index not in range(start_index, end_index)]
    def perform_addition(self, chromosome):
        if random.random() <= 0.01 and len(chromosome.string) < self.max_size:
            num_genes_to_add = random.randint(1, self.max_size - len(chromosome.string))
            available_genes = set(range(len(self.training_data["INPUT"]))) - set(chromosome.string)
            new_genes = random.sample(available_genes, num_genes_to_add)
            chromosome.string.extend(new_genes)
    def compare_fitness(self, population):
        for ind1, ind2 in combinations(population, 2):
            if ind1.partially_less_than(ind2):
                ind2.is_optimal = False
            elif ind2.partially_less_than(ind1):
                ind1.is_optimal = False
    def mark_optimal_individuals(self):
        for individual in self.population:
            individual.is_optimal = True
        self.compare_fitness(self.population)