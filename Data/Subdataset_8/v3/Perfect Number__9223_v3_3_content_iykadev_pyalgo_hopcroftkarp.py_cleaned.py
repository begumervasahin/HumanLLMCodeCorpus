import collections
import math
import random
from functools import reduce
from operator import mul
class Graph:
    '''
    Represents a bipartite graph.
    '''
    def __init__(self, n, edges):
        '''
        Initializes the bipartite graph with n nodes on each side and the given set of edges.
        '''
        self.n = n
        self.edges = edges
        self.nodes_left = [x + 1 for x in range(n)]
        self.nodes_right = [y * -1 - 1 for y in range(n)]
        self.neighbors = {}
        for edge in self.edges:
            x, y = edge
            self.neighbors[x] = self.neighbors.get(x, []) + [y]
            self.neighbors[y] = self.neighbors.get(y, []) + [x]
    def random_edge(self):
        '''
        Returns a random edge from the graph.
        '''
        return random.sample(self.edges, 1)[0]
class Matching:
    '''
    Represents a matching of size k between k nodes on the left and k nodes on the right.
    '''
    def __init__(self, k, edges):
        '''
        Initializes the matching with the given set of edges and the maximum size k.
        '''
        self.k = k
        self.edges = edges
        self.update()
    def update(self):
        '''
        Updates the neighbor dictionaries for each node.
        '''
        self.edges_left = {x: y for (x, y) in self.edges}
        self.edges_right = {y: x for (x, y) in self.edges}
    def size(self):
        '''Returns the size of the matching.'''
        return len(self.edges)
    def transition(self, e):
        '''
        Considers transitioning the matching.
        '''
        changed = False
        if self.size() == self.k:
            if e in self.edges:
                self.edges.remove(e)
                changed = True
        else:
            u, v = e
            if (u in self.edges_left) != (v in self.edges_right):
                if u in self.edges_left:
                    self.edges.remove((u, self.edges_left[u]))
                elif v in self.edges_right:
                    self.edges.remove((self.edges_right[v], v))
                self.edges.append(e)
                changed = True
            elif (u not in self.edges_left) and (v not in self.edges_right):
                self.edges.append(e)
                changed = True
        if changed:
            self.update()
            assert self.size() == self.k or self.size() == self.k - 1
        return changed
class HopcroftKarp:
    '''
    Implements the Hopcroft-Karp algorithm for finding a matching of size k in a bipartite graph.
    '''
    INFINITY = -1
    def __init__(self, graph):
        self.graph = graph
    def match(self, k):
        '''Constructs a matching of size k.'''
        self.pair = {}
        self.dist = {}
        self.q = collections.deque()
        for v in self.graph.nodes_left + self.graph.nodes_right:
            self.pair[v] = None
            self.dist[v] = HopcroftKarp.INFINITY
        matching = 0
        while matching < k and self.bfs():
            for v in self.graph.nodes_left:
                if matching >= k:
                    break
                if self.pair[v] is None and self.dfs(v):
                    matching += 1
                    if matching == k:
                        break
        edges = [(u, self.pair[u]) for u in self.pair.keys() if u > 0 and self.pair[u] is not None]
        M = Matching(k, edges)
        return M
    def dfs(self, v):
        '''Performs depth-first search.'''
        if v is not None:
            for u in self.graph.neighbors[v]:
                if self.dist[self.pair[u]] == self.dist[v] + 1 and self.dfs(self.pair[u]):
                    self.pair[u] = v
                    self.pair[v] = u
                    return True
            self.dist[v] = HopcroftKarp.INFINITY
            return False
        return True
    def bfs(self):
        '''Performs breadth-first search.'''
        for v in self.graph.nodes_left:
            if self.pair[v] is None:
                self.dist[v] = 0
                self.q.append(v)
            else:
                self.dist[v] = HopcroftKarp.INFINITY
        self.dist[None] = HopcroftKarp.INFINITY
        while len(self.q) > 0:
            v = self.q.popleft()
            if v is not None:
                for u in self.graph.neighbors[v]:
                    if self.dist[self.pair[u]] == HopcroftKarp.INFINITY:
                        self.dist[self.pair[u]] = self.dist[v] + 1
                        self.q.append(self.pair[u])
        return self.dist[None] != HopcroftKarp.INFINITY
class MarkovChain:
    '''
    Represents a Markov Chain on a set of matchings of size k and k-1.
    '''
    def __init__(self, k, graph, matching):
        self.k = k
        self.graph = graph
        self.matching = matching
    def run(self, num_transitions):
        '''Runs the Markov chain for a given number of steps.'''
        for _ in range(num_transitions):
            e = self.graph.random_edge()
            self.matching.transition(e)
class MonteCarloEstimator:
    '''
    Monte Carlo Estimator to estimate the ratio of matchings of size k and those of size k-1.
    '''
    def __init__(self, graph, k):
        self.graph = graph
        self.k = k
        hc = HopcroftKarp(graph)
        self.matching = hc.match(k)
        self.mc = MarkovChain(k, graph, self.matching)
    def estimate(self, num_transitions, num_samples):
        '''Estimates an r_k value for the given value of k.'''
        num_k = 0
        num_k_minus_1 = 0
        for _ in range(num_samples):
            self.mc.run(num_transitions)
            if self.matching.size() == self.k:
                num_k += 1
            elif self.matching.size() == self.k - 1:
                num_k_minus_1 += 1
        return float(num_k) / num_k_minus_1
class Approximator:
    '''
    Main class for running the randomized approximation algorithm.
    '''
    def __init__(self, graph, num_transitions="n ** 9", num_samples="n ** 5"):
        self.graph = graph
        self.r_values = [len(graph.edges)]
        n = self.graph.n
        self.num_transitions = eval(num_transitions)
        self.num_samples = eval(num_samples)
    def run(self):
        '''
        Runs the approximation algorithm and returns the product of the r values.
        '''
        for k in range(2, self.graph.n + 1):
            mce = MonteCarloEstimator(self.graph, k)
            self.r_values.append(mce.estimate(self.num_transitions, self.num_samples))
        return reduce(mul, self.r_values, 1)
def main():
    '''Basic example.'''
    n = 4
    graph = Graph(n, [(1, -3), (1, -4), (2, -2), (3, -1), (4, -3), (4, -4)])
    approximator = Approximator(graph)
    print(approximator.run())
if __name__ == "__main__":
    main()