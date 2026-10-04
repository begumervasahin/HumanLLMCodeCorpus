import time
from gephistreamer import graph, streamer
import Ut
class Utx:
    def __init__(self, seed=None):
        self.ut = Ut.Ut()
        self.lone = []
        try:
            self.stream = streamer.Streamer(streamer.GephiWS())
            print("Connected. Please add a referent in Gephi before adding points. Keep this referent available before adding points. Connect as master.")
        except Exception as e:
            print(f'Unable to connect to Gephi streamer: {e}')
        if isinstance(seed, Ut.Ut):
            self.sow(seed.manifold)
    def __repr__(self):
        return f'Utx : {self.tree} => {self.manifold.keys()}'
    def out(self, elements=None):
        if not elements:
            return 'Nothing to add'
        if isinstance(elements, graph.Node):
            self.stream.add_node(elements)
        elif isinstance(elements, graph.Edge):
            self.stream.add_edge(elements)
        elif isinstance(elements, list):
            for element in elements:
                self.out(element)
        elif isinstance(elements, (int, str)):
            return 'Object not immediately graphable'
        elif isinstance(elements, dict):
            for key in elements:
                self.out(elements[key])
        else:
            return elements
    def clearnodes(self):
        for key, values in self.manifold.items():
            for element in values:
                if isinstance(element, graph.Node):
                    self.stream.delete_node(element)
                elif isinstance(element, graph.Edge):
                    self.stream.delete_edge(element)
            del self.manifold[key]
    def connect(self, n):
        toout = []
        if not self.ut.tree:
            self.ut.treeme(n)
        node = graph.Node(n, type='Prime' if self.ut.checktree(n) else 'Factor')
        toout.append(node)
        for prime in self.ut.tree:
            if n % prime == 0:
                if n / prime != 1:
                    factor_node = graph.Node(prime, type="Prime")
                    result_node = graph.Node(n / prime, type="Factor")
                    self.lone.append(n / prime)
                    toout.extend([
                        factor_node, result_node,
                        graph.Edge(factor_node, node, type="Product"),
                        graph.Edge(factor_node, result_node, type="Product")
                    ])
                elif n != 1:
                    prime_node = graph.Node(n / prime, type="Prime")
                    previous_prime_node = graph.Node(prime - 1, type="Prime")
                    toout.extend([
                        prime_node, previous_prime_node,
                        graph.Edge(prime_node, previous_prime_node, type='PrimeLine')
                    ])
        if toout:
            self.out(toout)
    def split(self):
        if not self.lone:
            return 'Nothing to add'
        for i in range(len(self.lone)):
            if self.ut.checktree(self.lone[i]):
                del self.lone[i]
            try:
                self.connect(self.lone[i])
            except IndexError:
                del self.lone
                return 'Completed'
        self.lone = []
    def sow(self, element):
        if isinstance(element, int):
            self.connect(element)
        elif isinstance(element, (list, tuple)):
            for item in element:
                self.connect(item)
        elif isinstance(element, dict):
            for key in element:
                self.connect(key)
        elif isinstance(element, str):
            print('Dictionary for words is currently not supported')
        else:
            try:
                for item in element:
                    self.connect(item)
            except Exception as e:
                print(f'Unrecognized and unusable object: {e}')
    def flow(self, timer=None):
        if timer is None:
            timer = 0
        flux = 2
        while True:
            t = input('Enter q to stop the flow...').strip()
            if t.lower() == 'q':
                break
            print(f'Adding {flux}...')
            self.connect(flux)
            time.sleep(timer)
            flux += 1
    def spread(self, timer=None):
        timing = time.time()
        if timer is not None and isinstance(timer, int):
            timeout = timing + timer * self.ut.tree[-1]
            print(f'Warning: the operation will take {timeout - timing} seconds.')
            follow = input('Enter yes to continue').strip().lower()
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
    utx.flow()