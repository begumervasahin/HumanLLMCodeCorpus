from string import ascii_uppercase, ascii_lowercase
from random import choice, random
target = "METHINKS IT IS LIKE A WEASEL"
charset = ascii_uppercase + ascii_lowercase + ' '
parent = [choice(charset) for _ in range(len(target))]
min_mutate_rate = 0.09
iteration_range = range(100)
perfect_fitness = float(len(target))
def fitness(trial):
    return sum(t == h for t, h in zip(trial, target))
def mutate_rate():
    return 1 - ((perfect_fitness - fitness(parent)) / perfect_fitness * (1 - min_mutate_rate))
def mutate(parent, rate):
    return [(ch if random() <= rate else choice(charset)) for ch in parent]
def display_iteration():
    print("(iterations: {}, fitness: {:.2f}%, parent: {})".format(iterations, fitness(parent) * 100. / perfect_fitness, ''.join(parent)))
def mate(a, b):
    place = 0
    if choice(range(10)) < 7:
        place = choice(range(len(target)))
    else:
        return a, b
    return a, b, a[:place] + b[place:], b[:place] + a[place:]
iterations = 0
center = len(iteration_range)
while parent != list(target):
    rate = mutate_rate()
    iterations += 1
    if iterations % 100 == 0:
        display_iteration()
    copies = [mutate(parent, rate) for _ in iteration_range] + [parent]
    parent1 = max(copies[:center], key=fitness)
    parent2 = max(copies[center:], key=fitness)
    parent = max(mate(parent1, parent2), key=fitness)
display_iteration()