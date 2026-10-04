import numpy as np
import random
from copy import deepcopy
class Tree(list):
    def __init__(self, content):
        super().__init__(content)
        self.fitness = None
        self.errors = None
    @property
    def height(self):
        stack = [0]
        max_depth = 0
        for node in self:
            depth = stack.pop()
            max_depth = max(max_depth, depth)
            stack.extend([depth + 1] * node[2])
        return max_depth
    def subtree(self, begin):
        end = begin + 1
        total = self[begin][2]
        while total > 0:
            total += self[end][2] - 1
            end += 1
        return end
    def __str__(self):
        stack = []
        for name, func, arity, const in self[::-1]:
            stack.append(f"{name}({','.join([stack.pop() for _ in range(arity)])})" if arity != 0 else name)
        return stack[0]
    def run(self, X):
        ones = np.ones(len(X))
        x = X.flatten()
        stack = []
        for name, func, arity, const in self[::-1]:
            if name == "x":
                func_ret = x
            elif arity == 0:
                func_ret = ones * const
            else:
                func_ret = func(*[stack.pop() for _ in range(arity)])
            stack.append(func_ret)
        return stack[0]
    def to_tex(self):
        trans_dict = {
            "add": lambda a, b: f"({a}+{b})",
            "sub": lambda a, b: f"({a}-{b})",
            "mul": lambda a, b: f"{a}{b}",
            "div": lambda a, b: f"\\frac{{{a}}}{{{b}}}",
            "sin": lambda a: f"\\sin({a})",
            "cos": lambda a: f"\\cos({a})",
            "tan": lambda a: f"\\tan({a})",
            "log": lambda a: f"\\log({a})",
            "exp": lambda a: f"\\exp({a})",
            "sqrt": lambda a: f"\\sqrt{{{a}}}",
            "-1": lambda: "-1",
            "0": lambda: "0",
            "1": lambda: "1",
            "0.5": lambda: "0.5",
            "pi": lambda: "\\pi",
            "e": lambda: "e",
            "x": lambda: "x",
        }
        stack = []
        for name, func, arity, const in self[::-1]:
            trans_func = trans_dict[name]
            stack.append(trans_func(*[stack.pop() for _ in range(arity)]))
        return stack[0]
    def to_sympy(self):
        trans_dict = {
            "add": lambda a, b: f"({a}+{b})",
            "sub": lambda a, b: f"({a}-{b})",
            "mul": lambda a, b: f"{a}*{b}",
            "div": lambda a, b: f"{a}/{b}",
            "sin": lambda a: f"sin({a})",
            "cos": lambda a: f"cos({a})",
            "tan": lambda a: f"tan({a})",
            "log": lambda a: f"log({a})",
            "exp": lambda a: f"exp({a})",
            "sqrt": lambda a: f"{a}**(1/2)",
            "-1": lambda: "-1",
            "0": lambda: "0",
            "1": lambda: "1",
            "0.5": lambda: "0.5",
            "pi": lambda: "pi",
            "e": lambda: "e",
            "x": lambda: "x",
        }
        stack = []
        for name, func, arity, const in self[::-1]:
            trans_func = trans_dict[name]
            stack.append(trans_func(*[stack.pop() for _ in range(arity)]))
        return stack[0]
def create_tree(node_set, leaf_set, height=5):
    items = []
    stack = [0]
    while stack:
        depth = stack.pop()
        node = random.choice(leaf_set if depth == height else node_set)
        stack.extend([depth + 1] * node[2])
        items.append(node)
    return Tree(items)
def swap_tree(treeA, treeB, limit):
    if len(treeA) == 1 or len(treeB) == 1:
        return treeA, treeB
    for _ in range(100):
        s_A = random.randrange(1, len(treeA))
        s_B = random.randrange(1, len(treeB))
        e_A = treeA.subtree(s_A)
        e_B = treeB.subtree(s_B)
        treeA[s_A:e_A], treeB[s_B:e_B] = treeB[s_B:e_B], treeA[s_A:e_A]
        if treeA.height <= limit and treeB.height <= limit:
            break
        treeA[s_A:e_A], treeB[s_B:e_B] = treeB[s_B:e_B], treeA[s_A:e_A]
    return treeA, treeB
def point_mutation(tree, node_set, leaf_set, mutation_prob):
    for i, node in enumerate(tree):
        if random.random() < mutation_prob:
            name, func, arity, const = node
            tree[i] = random.choice(leaf_set if arity == 0 else [n for n in node_set if n[2] == arity])
    return tree
def make_node_set():
    node_set = [
        ("add", np.add, 2, None),
        ("sub", np.subtract, 2, None),
        ("mul", np.multiply, 2, None),
        ("div", np.divide, 2, None),
        ("sin", np.sin, 1, None),
        ("cos", np.cos, 1, None),
        ("tan", np.tan, 1, None),
        ("log", np.log, 1, None),
        ("exp", np.exp, 1, None),
        ("sqrt", np.sqrt, 1, None)
    ]
    leaf_set = [
        ("pi", None, 0, np.pi),
        ("e", None, 0, np.e),
        ("x", None, 0, None)
    ]
    return node_set, leaf_set
def initial_population(size, node_set, leaf_set):
    return [create_tree(node_set, leaf_set) for _ in range(size)]
def evaluate_population(population, X, y):
    for tree in population:
        if tree.fitness is None:
            _y = tree.run(X)
            errors = np.abs(y - _y)
            fitness = np.mean(errors)
            tree.fitness = fitness if np.isfinite(fitness) else None
            tree.errors = errors if np.isfinite(fitness) else None
    return population
def select_population(population, elite, batch_size=8, tour_size=64):
    population = [tree for tree in population if tree.fitness is not None]
    best = min(population, key=lambda tree: tree.fitness)
    elite = deepcopy(best) if elite is None or best.fitness < elite.fitness else elite
    next_population = []
    T = np.arange(len(population[0].errors))
    np.random.shuffle(T)
    t_start = 0
    for _ in range(len(population) - 1):
        best_tree = None
        best_ave = 0
        subpop = random.sample(population, tour_size) if len(population) > tour_size else population
        t_end = min(t_start + batch_size, len(T))
        for tree in subpop:
            ave = np.mean([tree.errors[t] for t in T[t_start:t_end]])
            if best_tree is None or ave < best_ave:
                best_tree = tree
                best_ave = ave
        next_population.append(deepcopy(best_tree))
        t_start = t_end if t_end < len(T) else 0
    next_population.append(deepcopy(elite))
    return next_population, elite
def perform_crossover(population, crossover_prob, height_limit):
    for i in range(0, len(population), 2):
        if random.random() < crossover_prob:
            population[i], population[i+1] = swap_tree(population[i], population[i+1], height_limit)
            population[i].fitness = None
            population[i+1].fitness = None
    return population
def perform_mutation(population, mutation_prob, node_set, leaf_set):
    for i in range(len(population)):
        population[i] = point_mutation(population[i], node_set, leaf_set, mutation_prob)
        population[i].fitness = None
    return population