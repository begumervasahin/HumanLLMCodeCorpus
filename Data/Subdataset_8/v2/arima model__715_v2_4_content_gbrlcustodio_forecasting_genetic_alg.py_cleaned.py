import random
import copy
import numpy as np
import train_rbfn
from itertools import repeat, combinations
from cromossome import Cromossome
from math import log
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
        for _ in repeat(None, size):
            individual = Cromossome()
            individual.string = random.sample(range(0, len(self.training_data["INPUT"])), random.randint(self.min_size, self.max_size))
            self.population.append(individual)
    def decode_individual(self, chromosome):
        centers = []
        for center_idx in chromosome:
            centers.append([self.training_data["INPUT"].values[center_idx].tolist()])
        return np.asarray(centers)
    def evaluate_individual(self, chromosome):
        network = train_rbfn.train(self.training_input, self.training_output, self.decode_individual(chromosome.string))
        chromosome.fitness = [network.aic(self.training_data), network.aic(self.test_data)]
    def evolve(self, generations):
        generation = 1
        for _ in repeat(None, generations):
            print("Generation ", generation)
            generation += 1
            for individual in self.population:
                self.evaluate_individual(individual)
            self.rank_population()
            new_population = []
            while len(new_population) < len(self.population):
                parents = [self.select_individual() for _ in range(2)]
                offsprings = self.perform_crossover(parents) if random.random() <= 0.90 else [copy.deepcopy(parent) for parent in parents]
                for offspring in offsprings:
                    self.perform_mutation(offspring)
                    self.perform_deletion(offspring)
                    self.perform_addition(offspring)
                    if offspring.string != parents[0].string and offspring.string != parents[1].string:
                        self.evaluate_individual(offspring)
                        parents.append(offspring)
                selected = []
                while len(selected) < 2:
                    for individual in parents:
                        individual.p_optimal = True
                    self.compare_individuals(parents)
                    selected.extend([individual for individual in parents if individual.p_optimal][:2 - len(selected)])
                    parents = [e for e in parents if not e.p_optimal]
                new_population.extend(selected)
            self.population = new_population
        for individual in self.population:
            individual.p_optimal = True
        self.compare_individuals(self.population)
        best_config = [individual for individual in self.population if individual.p_optimal][0]
        print(self.decode_individual(best_config.string))
        return train_rbfn.train(self.training_input, self.training_output, self.decode_individual(best_config.string))
    def compare_individuals(self, population):
        for a, b in combinations(population, 2):
            if a.partially_less_than(b):
                b.p_optimal = False
            elif b.partially_less_than(a):
                a.p_optimal = False
    def rank_population(self):
        new_population = []
        current_rank = 0
        while self.population:
            for individual in self.population:
                individual.p_optimal = True
            self.compare_individuals(self.population)
            for individual in self.population:
                if individual.p_optimal:
                    individual.rank = len(self.population) - current_rank
                    new_population.append(individual)
            self.population = [individual for individual in self.population if not individual.p_optimal]
            current_rank += 1
        self.population = new_population
    def select_individual(self):
        max_sum = sum(individual.rank for individual in self.population)
        pick = random.uniform(0, max_sum)
        current = 0
        for individual in self.population:
            current += individual.rank
            if current > pick:
                return individual
    def perform_crossover(self, parents):
        if len(parents[0].string) <= len(parents[-1].string):
            smaller, bigger = [copy.deepcopy(parent) for parent in parents]
        else:
            bigger, smaller = [copy.deepcopy(parent) for parent in parents]
        common = set(smaller.string).intersection(bigger.string)
        diff = list(set(smaller.string) - common)
        if diff:
            quantity = random.randint(1, len(diff))
            first_sample = [diff[i] for i in sorted(random.sample(range(len(diff)), quantity))]
            diff = list(set(bigger.string) - common)
            if diff:
                second_sample = [diff[i] for i in sorted(random.sample(range(len(diff)), quantity))]
                findex = [smaller.string.index(item) for item in first_sample]
                sindex = [bigger.string.index(item) for item in second_sample]
                for i, j in zip(findex, sindex):
                    smaller.string[i], bigger.string[j] = bigger.string[j], smaller.string[i]
        return [smaller, bigger]
    def perform_mutation(self, chromosome):
        for locus in range(len(chromosome.string)):
            if random.random() <= 0.01:
                chromosome.string[locus] = random.sample(set(range(0, len(self.training_data["INPUT"]))).difference(chromosome.string), 1)[0]
    def perform_deletion(self, chromosome):
        if random.random() <= 0.01:
            starting_from = random.randint(0, len(chromosome.string) - 1)
            upto = starting_from + random.randint(1, len(chromosome.string) - starting_from)
            if (upto - starting_from) == len(chromosome.string):
                upto -= 1
            chromosome.string = [gene for index, gene in enumerate(chromosome.string) if index not in range(starting_from, upto)]
    def perform_addition(self, chromosome):
        if random.random() <= 0.01 and len(chromosome.string) < self.max_size:
            quantity = random.randint(1, self.max_size - len(chromosome.string))
            chromosome.string.extend(random.sample(set(range(0, len(self.training_data["INPUT"]))).difference(chromosome.string), quantity))