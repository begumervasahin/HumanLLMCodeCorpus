import time
from gephistreamer import graph, streamer
import Ut
class Utx:
    def __init__(self, seed=None):
        self.ut = Ut.Ut()
        self.lone = list()
        self.stream = None
        try:
            self.stream = streamer.Streamer(streamer.GephiWS())
            print("Connected to Gephi. Ensure a referent is added in Gephi before adding points. Connect as master.")
        except Exception:
            print('Unable to connect to Gephi streamer.')
        if isinstance(seed, Ut.Ut):
            self.sow(seed.manifold)
    def __repr__(self):
        return f'Utx : {self.ut.tree} => {list(self.ut.manifold.keys())}'
    def out(self, elements=None):
        if not elements:
            return 'Nothing to add'
        if isinstance(elements, list):
            for element in elements:
                self.out(element)
        elif isinstance(elements, graph.Node):
            self.stream.add_node(elements)
        elif isinstance(elements, graph.Edge):
            self.stream.add_edge(elements)
        elif isinstance(elements, dict):
            for key in elements:
                self.out(elements[key])
        else:
            return 'Element type not supported'
    def clear_nodes(self):
        for key, values in self.ut.manifold.items():
            for item in values:
                if isinstance(item, graph.Node):
                    self.stream.delete_node(item)
                elif isinstance(item, graph.Edge):
                    self.stream.delete_edge(item)
            del self.ut.manifold[key]
    def connect(self, n):
        toout = []
        if not self.ut.tree:
            self.ut.treeme(n)
        if not self.ut.checktree(n):
            node = graph.Node(n, type='Factor')
        else:
            node = graph.Node(n, type='Prime')
        toout.append(node)
        for prime in self.ut.tree:
            if n % prime == 0:
                if n
                    prime_factor = graph.Node(prime, type="Prime")
                    result_node = graph.Node(n
                    self.lone.append(n
                    toout.extend([
                        prime_factor,
                        result_node,
                        graph.Edge(prime_factor, node, type="Product"),
                        graph.Edge(prime_factor, result_node, type="Product")
                    ])
                else:
                    prime_factor = graph.Node(n
                    previous_prime = graph.Node(prime, type="Prime")
                    toout.extend([
                        prime_factor,
                        previous_prime,
                        graph.Edge(prime_factor, previous_prime, type='PrimeLine')
                    ])
        if toout:
            self.out(toout)
    def split(self):
        if not self.lone:
            return 'Nothing to add'
        while self.lone:
            element = self.lone.pop(0)
            if not self.ut.checktree(element):
                self.connect(element)
    def sow(self, element):
        if isinstance(element, int):
            self.connect(element)
        elif isinstance(element, (list, tuple)):
            for item in element:
                self.connect(item)
        elif isinstance(element, dict):
            for key in element:
                self.connect(key)
        else:
            print('Unsupported element type')
    def flow(self, timer=None):
        timer = timer or 0
        flux = 2
        while True:
            t = input('Enter q to stop the flow: ')
            if t == 'q':
                break
            print(f'Adding {flux}...')
            self.connect(flux)
            time.sleep(timer)
            flux += 1
    def spread(self, timer=None):
        timing = time.time()
        if timer and isinstance(timer, int):
            timeout = timing + timer * self.ut.tree[-1]
            print(f'This operation will take {timeout - timing} seconds.')
            follow = input('Enter yes to continue: ').strip().lower()
        else:
            follow = 'yes'
        if follow == 'yes':
            itmax = self.ut.tree[-1]
            while itmax >= 2:
                self.connect(itmax)
                if isinstance(timer, int):
                    time.sleep(timer)
                itmax -= 1
if __name__ == "__main__":
    utx = Utx()
    utx.flow(timer=1)