import random
import copy
import numpy as np
import matplotlib.pyplot as plt
import Ind
def crossover(parents):
    child = Ind.Ind()
    r1, r2 = random.sample(range(4), 2)
    child.cof[r1] = parents[0].cof[r1]
    child.cof[r2] = parents[0].cof[r2]
    remaining_indices = [i for i in range(4) if i not in (r1, r2)]
    child.cof[remaining_indices[0]] = parents[1].cof[remaining_indices[0]]
    child.cof[remaining_indices[1]] = parents[1].cof[remaining_indices[1]]
    return child
def mutation(individual, mutation_rate, sigma):
    if random.random() <= mutation_rate:
        noise = np.random.normal(0, sigma, 4)
        individual.cof += noise
    return individual
def generate_next_population(population, mutation_rate, sigma, ys, xs):
    parents_pairs = [(copy.deepcopy(random.choice(population)), copy.deepcopy(random.choice(population))) for _ in range(len(population))]
    offspring = [crossover(pair) for pair in parents_pairs]
    offspring = [mutation(ind, mutation_rate, sigma) for ind in offspring]
    for ind in offspring:
        ind.fit_ness(ys, xs)
    combined_population = population + offspring
    combined_population.sort(key=lambda ind: ind.fitness, reverse=True)
    return combined_population[:50]
def main(generations, population_size, tournament_size, mutation_rate, sigma):
    with open('input.csv', 'r') as f:
        ys = [float(f.readline().strip()) for _ in range(100)]
    xs = [round(x * 0.1, 1) for x in range(100)]
    population = [Ind.Ind() for _ in range(population_size)]
    for ind in population:
        ind.fit_ness(ys, xs)
    best_fitness, mean_fitness, worst_fitness, generations_count = [], [], [], []
    for gen_num in range(generations):
        population = generate_next_population(population, mutation_rate, sigma, ys, xs)
        generations_count.append(gen_num)
        best_fitness.append(population[0].fitness)
        mean_fitness.append((population[0].fitness + population[-1].fitness) / 2)
        worst_fitness.append(population[-1].fitness)
        print(f'Generation {gen_num + 1} - Best Fitness: {population[0].fitness}')
    x = np.linspace(0, 10, 100)
    best_cof = population[0].cof
    y = best_cof[3] * x**3 + best_cof[2] * x**2 + best_cof[1] * x + best_cof[0]
    plt.plot(xs, ys, 'co', x, y, '-g', label='Best Fit')
    plt.show()
    plt.plot(generations_count, best_fitness, 'g^', label='Best')
    plt.plot(generations_count, mean_fitness, 'co', label='Mean')
    plt.plot(generations_count, worst_fitness, 'rs', label='Worst')
    plt.legend()
    plt.show()
if __name__ == "__main__":
    main(generations=5000, population_size=50, tournament_size=2, mutation_rate=0.1, sigma=0.1)