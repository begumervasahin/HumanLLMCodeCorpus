
from gephistreamer import graph
from gephistreamer import streamer
import time
import Ut
class Utx:
    def __init__(self, seed=None):
        self.ut = Ut.Ut()
        self.lone = list()
        try:
            self.stream = streamer.Streamer(streamer.GephiWS())
            print("Connected. Ajoutez un référent dans gephi avant d'ajouter des points. "
                  "Gardez ce référent à portée avant d'ajouter des points. "
                  "Connectez-vous en master.")
        except Exception:
            print('Impossible de se connecter au gephistreamer.')
        if isinstance(seed, Ut.Ut):
            self.sow(seed.manifold)
    def __repr__(self):
        return f'Utx : {self.tree} => {list(self.manifold.keys())}'
    def out(self, elements=None):
        if not elements:
            return 'nothing to add'
        elif isinstance(elements, graph.Node):
            self.stream.add_node(elements)
        elif isinstance(elements, graph.Edge):
            self.stream.add_edge(elements)
        elif isinstance(elements, list):
            for element in elements:
                if isinstance(element, (graph.Edge, graph.Node)):
                    self.out(element)
        elif isinstance(elements, (int, str)):
            return 'Objet non graphable immédiatement'
        elif isinstance(elements, dict):
            for key in elements:
                self.out(elements[key])
        else:
            return elements
    def clearnodes(self):
        for key, values in self.manifold.items():
            for item in values:
                if isinstance(item, graph.Node):
                    self.stream.delete_node(item)
                elif isinstance(item, graph.Edge):
                    self.stream.delete_edge(item)
            del self.manifold[key]
    def connect(self, n):
        toout = list()
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
                if n
                    prime_factor = graph.Node(self.ut.tree[w], type="Prime")
                    toout.append(prime_factor)
                    result_node = graph.Node(n
                    self.lone.append(n
                    toout.append(result_node)
                    edge1 = graph.Edge(prime_factor, node, type="Product")
                    toout.append(edge1)
                    edge2 = graph.Edge(prime_factor, result_node, type="Product")
                    toout.append(edge2)
                else:
                    prime_factor = graph.Node(n
                    toout.append(prime_factor)
                    previous_prime = graph.Node(self.ut.tree[w - 1], type="Prime")
                    toout.append(previous_prime)
                    prime_edge = graph.Edge(prime_factor, previous_prime, type='PrimeLine')
                    toout.append(prime_edge)
        if toout:
            self.out(toout)
    def split(self):
        if not self.lone:
            return 'Rien à ajouter'
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
        elif isinstance(element, str):
            print('Pas de dictionnaire pour les mots actuellement')
        else:
            try:
                for item in element:
                    self.connect(item)
            except Exception:
                print('Objet non reconnu et non utilisable')
    def flow(self, timer=None):
        timer = timer or 0
        t = ''
        flux = 2
        while t != 'q':
            t = input('Entrez q pour arrêter le flux...')
            print(f'Ajout de {flux}...')
            while flux > 0:
                self.connect(flux)
                time.sleep(timer)
                flux += 1
    def spread(self, timer=None):
        timing = time.time()
        if timer and isinstance(timer, int):
            timeout = timing + timer * self.ut.tree[-1]
            print(f'Attention, l\'opération prendra {timeout - timing} secondes.')
            follow = input('Entrez oui pour continuer')
        else:
            follow = 'oui'
        if follow == 'oui':
            itmax = self.ut.tree[-1]
            while itmax >= 2:
                self.connect(itmax)
                if isinstance(timer, int):
                    time.sleep(timer)
                itmax -= 1