from string import ascii_uppercase, ascii_lowercase
from random import choice, random
TARGET_STRING = "METHINKS IT IS LIKE A WEASEL"
CHARACTER_SET = ascii_uppercase + ascii_lowercase + ' '
class EvolutionaryAlgorithm:
    def __init__(self, target, charset, min_mutate_rate=0.09, max_iterations=100):
        self.target = target
        self.charset = charset
        self.parent = [choice(self.charset) for _ in range(len(self.target))]
        self.min_mutate_rate = min_mutate_rate
        self.max_iterations = max_iterations
        self.perfect_fitness = float(len(self.target))
    def fitness(self, trial):
        return sum(t == h for t, h in zip(trial, self.target))
    def mutate_rate(self):
        return 1 - ((self.perfect_fitness - self.fitness(self.parent)) / self.perfect_fitness * (1 - self.min_mutate_rate))
    def mutate(self, parent, rate):
        return [(ch if random() <= rate else choice(self.charset)) for ch in parent]
    def mate(self, a, b):
        place = choice(range(len(self.target))) if choice(range(10)) < 7 else 0
        return a, b, a[:place] + b[place:], b[:place] + a[place:]
    def evolve(self):
        iterations = 0
        center = len(range(self.max_iterations))
        while self.parent != list(self.target):
            rate = self.mutate_rate()
            iterations += 1
            if iterations % 100 == 0:
                self._display_iteration(iterations)
            copies = [self.mutate(self.parent, rate) for _ in range(self.max_iterations)] + [self.parent]
            parent1 = max(copies[:center], key=self.fitness)
            parent2 = max(copies[center:], key=self.fitness)
            self.parent = max(self.mate(parent1, parent2), key=self.fitness)
        self._display_iteration(iterations)
    def _display_iteration(self, iterations):
        print("(iterations: {}, fitness: {:.2f}%, parent: {})".format(iterations, self.fitness(self.parent) * 100. / self.perfect_fitness, ''.join(self.parent)))
if __name__ == "__main__":
    evolutionary_algorithm = EvolutionaryAlgorithm(TARGET_STRING, CHARACTER_SET)
    evolutionary_algorithm.evolve()