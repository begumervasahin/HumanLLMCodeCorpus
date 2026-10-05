import sys
from datetime import date
from functools import reduce
from math import sqrt
from itertools import count, islice
import time
from gephistreamer import graph, streamer
import Ut
class Utx:
    def __init__(self, seed=None):
        self.ut = Ut.Ut()
        self.lone = list()
        try:
            self.stream = streamer.Streamer(streamer.GephiWS())
            print("Connected. Ajoutez un referent dans gephi avant d'ajouter des points. Gardez ce référent à portée avant d'ajouter des points. Connectez-vous en master")
        except:
            print('Impossible de se connecter au gephistreamer.')
        if isinstance(seed, Ut.Ut):
            self.sow(seed.manifold)
    def __repr__(self):
        return 'Utx : {} => {}'.format(self.tree, self.manifold.keys())
    def out(self, elements=None):
        if not elements or elements is None:
            return 'nothing to add'
        elif isinstance(elements, graph.Node):
            self.stream.add_node(elements)
        elif isinstance(elements, graph.Edge):
            self.stream.add_edge(elements)
        elif isinstance(elements, list):
            for elem in elements:
                self.out(elem)
        elif isinstance(elements, int) or isinstance(elements, str):
            return 'Objet non graphable immédiatement'
        elif isinstance(elements, dict):
            for key in elements.keys():
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
            if n % self.ut.tree[w] == 0 and n / self.ut.tree[w] != 1:
                premierfac = graph.Node(self.ut.tree[w], type="Prime")
                toout.append(premierfac)
                premierResultat = graph.Node(n / self.ut.tree[w], type="Factor")
                self.lone.append(n / self.ut.tree[w])
                toout.append(premierResultat)
                lienfact = graph.Edge(premierfac, node, type="Product")
                toout.append(lienfact)
                lienfac2 = graph.Edge(premierfac, premierResultat, type="Product")
                toout.append(lienfac2)
            elif n % self.ut.tree[w] == 0 and n / self.ut.tree[w] == 1 and n != 1:
                premierfac = graph.Node(n / self.ut.tree[w], type="Prime")
                toout.append(premierfac)
                premierprecedent = graph.Node(self.ut.tree[w - 1], type="Prime")
                toout.append(premierprecedent)
                arbre = graph.Edge(premierfac, premierprecedent, type='PrimeLine')
                toout.append(arbre)
        if toout:
            self.out(toout)
    def split(self):
        if not self.lone:
            return 'Rien a ajouter'
        key = 0
        while key < len(self.lone):
            if self.ut.checktree(self.lone[key]):
                del self.lone[key]
            try:
                self.connect(self.lone[key])
            except IndexError:
                message = 'Terminé'
                del self.lone
                return message
            key += 1
        self.lone = []
    def sow(self, element):
        if isinstance(element, int):
            self.connect(element)
        elif isinstance(element, (list, tuple)):
            for key in element:
                self.connect(key)
        elif isinstance(element, dict):
            for key in element.keys():
                self.connect(key)
        elif isinstance(element, str):
            print('Pas de dictionnaire pour les mots actuellement')
        else:
            for key in element:
                self.connect(key)
    def flow(self, timer=None):
        if timer is None:
            timer = 0
        t = ''
        flux = 2
        while t != 'q':
            t = input('Entrez q pour arrêter le flux...')
            print('Ajout de {}...'.format(flux))
            for _ in range(flux):
                self.connect(flux)
                time.sleep(timer)
                flux += 1
    def spread(self, timer=None):
        timing = time.time()
        if timer and isinstance(timer, int):
            timeout = timing + timer * self.ut.tree[-1]
            print('Attention, l\'opération prendra {} secondes.'.format(timeout - timing))
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
if __name__ == '__main__':
    utx = Utx()
    utx.flow()