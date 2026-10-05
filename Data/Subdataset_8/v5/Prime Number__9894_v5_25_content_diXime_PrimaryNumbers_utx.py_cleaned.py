import sys
import time
from datetime import date
from math import sqrt
from functools import reduce
from itertools import count, islice
from gephistreamer import graph, streamer
import Ut
class Utx:
    def __init__(self, seed=None):
        self.ut = Ut.Ut()
        self.lone = []
        try:
            self.stream = streamer.Streamer(streamer.GephiWS())
            print("Connected to Gephi streamer. Please add a reference node in Gephi before adding points.")
            print("Keep this reference node accessible before adding points.")
            print("Connect as master.")
        except:
            print('Failed to connect to Gephistreamer.')
        if isinstance(seed, Ut.Ut):
            self.sow(seed.manifold)
    def __repr__(self):
        return 'Utx : {} => {}'.format(self.tree, self.manifold.keys())
    def out(self, elements=None):
        if not elements or elements is None:
            return 'nothing to add'
        elif isinstance(elements, (graph.Node, graph.Edge)):
            self.stream.add_node(elements) if isinstance(elements, graph.Node) else self.stream.add_edge(elements)
        elif isinstance(elements, list):
            for item in elements:
                self.out(item)
        elif isinstance(elements, (int, str, dict)):
            return 'Object not graphable immediately'
        else:
            return elements
    def clearnodes(self):
        for key, values in self.manifold.items():
            for item in values:
                if isinstance(item, (graph.Node, graph.Edge)):
                    self.stream.delete_node(item) if isinstance(item, graph.Node) else self.stream.delete_edge(item)
            del self.manifold[key]
    def connect(self, n):
        to_out = []
        if not self.ut.tree:
            self.ut.treeme(n)
        if not self.ut.checktree(n):
            node = graph.Node(n, type='Factor')
        else:
            node = graph.Node(n, type='Prime')
        to_out.append(node)
        for val in self.ut.tree:
            if n % val == 0 and n
                prime_factor = graph.Node(val, type="Prime")
                product_result = graph.Node(n
                self.lone.append(n
                edge_factor = graph.Edge(prime_factor, node, type="Product")
                edge_factor2 = graph.Edge(prime_factor, product_result, type="Product")
                to_out.extend([prime_factor, product_result, edge_factor, edge_factor2])
            elif n % val == 0 and n
                prime_factor = graph.Node(n
                previous_prime = graph.Node(self.ut.tree[self.ut.tree.index(val) - 1], type="Prime")
                prime_line = graph.Edge(prime_factor, previous_prime, type='PrimeLine')
                to_out.extend([prime_factor, previous_prime, prime_line])
        if to_out:
            self.out(to_out)
    def split(self):
        if not self.lone:
            return 'Nothing to add'
        for i, val in enumerate(self.lone):
            if self.ut.checktree(val):
                del self.lone[i]
            try:
                self.connect(val)
            except IndexError:
                message = 'Terminated'
                del self.lone
                return message
        self.lone = []
    def sow(self, element):
        if isinstance(element, (int, list, tuple)):
            for item in element:
                self.connect(item)
        elif isinstance(element, dict):
            for key in element.keys():
                self.connect(key)
        elif isinstance(element, str):
            print('No dictionaries for words currently')
        else:
            try:
                for item in element:
                    self.connect(item)
            except:
                print('Unrecognized and unusable object')
    def flow(self, timer=0):
        t = str()
        flux = 2
        while t != 'q':
            t = input('Enter q to stop the flow...')
            print(f'Adding {flux}...')
            while flux > 0:
                self.connect(flux)
                time.sleep(timer)
                flux += 1
    def spread(self, timer=None):
        timing = time.time()
        if timer and isinstance(timer, int):
            timeout = timing + timer * self.ut.tree[-1]
            print(f'Attention, the operation will take {timeout - timing} seconds.')
            follow = input('Enter yes to continue')
        else:
            follow = 'yes'
        if follow == 'yes':
            itmax = self.ut.tree[-1]
            while itmax >= 2:
                self.connect(itmax)
                if isinstance(timer, int):
                    time.sleep(timer)
                itmax -= 1
if __name__ == '__main__':
    seed = None
    utx = Utx(seed)
    utx.flow()
