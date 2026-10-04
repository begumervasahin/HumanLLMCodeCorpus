from gephistreamer import graph, streamer
import time
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
        if not self.ut.checktree(n):
            node = graph.Node(n, type='Factor')
            toout.append(node)
        else:
            node = graph.Node(n, type='Prime')
            toout.append(node)
        for w in range(len(self.ut.tree)):
            if n % self.ut.tree[w] == 0:
                if n / self.ut.tree[w] != 1:
                    premierfac = graph.Node(self.ut.tree[w], type="Prime")
                    toout.append(premierfac)
                    premierResultat = graph.Node(n / self.ut.tree[w], type="Factor")
                    self.lone.append(n / self.ut.tree[w])
                    toout.append(premierResultat)
                    toout.append(graph.Edge(premierfac, node, type="Product"))
                    toout.append(graph.Edge(premierfac, premierResultat, type="Product"))
                elif n != 1:
                    premierfac = graph.Node(n / self.ut.tree[w], type="Prime")
                    toout.append(premierfac)
                    premierprecedent = graph.Node(self.ut.tree[w - 1], type="Prime")
                    toout.append(premierprecedent)
                    toout.append(graph.Edge(premierfac, premierprecedent, type='PrimeLine'))
        if toout:
            self.out(toout)
    def split(self):
        if not self.lone:
            return 'Nothing to add'
        for key in range(len(self.lone)):
            if self.ut.checktree(self.lone[key]):
                del self.lone[key]
            try:
                self.connect(self.lone[key])
            except IndexError:
                message = 'Completed'
                del self.lone
                return message
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
        t = ''
        while t != 'q':
            t = input('Enter q to stop the flow...')
            print(f'Adding {flux}...')
            while flux > 0:
                self.connect(flux)
                time.sleep(timer)
                flux += 1
    def spread(self, timer=None):
        timing = time.time()
        if timer is not None and isinstance(timer, int):
            timeout = timing + timer * self.ut.tree[-1]
            print(f'Warning: the operation will take {timeout - timing} seconds.')
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