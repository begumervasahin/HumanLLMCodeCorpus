
from gephistreamer import graph
from gephistreamer import streamer
import time
import Ut
class class1:
    def fonk1(self, b1 = None):
        self.b2 = Ut.Ut()
        self.b3 = list()
        try:
            self.b4 = streamer.Streamer(streamer.GephiWS())
            print("Connected. Ajoutez un référent dans gephi avant d'ajouter des points. "
                  "Gardez ce référent à portée avant d'ajouter des points. "
                  "Connectez-vous en master.")
        except Exception:
            print('Impossible de se connecter au gephistreamer.')
        if isinstance(b1, Ut.Ut):
            self.fonk7(b1.manifold)
    def fonk2(self):
        return f'class1 : {self.tree} => {list(self.manifold.keys())}'
    def fonk3(self, b5 = None):
        if not b5:
            return 'nothing to add'
        elif isinstance(b5, graph.Node):
            self.b4.add_node(b5)
        elif isinstance(b5, graph.Edge):
            self.b4.add_edge(b5)
        elif isinstance(b5, list):
            for b14 in b5:
                if isinstance(b14, (graph.Edge, graph.Node)):
                    self.fonk3(b14)
        elif isinstance(b5, (int, str)):
            return 'Objet non graphable immédiatement'
        elif isinstance(b5, dict):
            for key in b5:
                self.fonk3(b5[key])
        else:
            return b5
    def fonk4(self):
        for key, values in self.manifold.items():
            for item in values:
                if isinstance(item, graph.Node):
                    self.b4.delete_node(item)
                elif isinstance(item, graph.Edge):
                    self.b4.delete_edge(item)
            del self.manifold[key]
    def fonk5(self, n):
        b6 = list()
        if not self.b2.tree:
            self.b2.treeme(n)
        if not self.b2.checktree(n):
            b7 = graph.Node(n, type='Factor')
            b6.append(b7)
        else:
            b7 = graph.Node(n, type='Prime')
            b6.append(b7)
        for w in range(len(self.b2.tree)):
            if n % self.b2.tree[w] == 0:
                if n
                    b8 = graph.Node(self.b2.tree[w], type="Prime")
                    b6.append(b8)
                    b9 = graph.Node(n
                    self.b3.append(n
                    b6.append(b9)
                    b10 = graph.Edge(b8, b7, type="Product")
                    b6.append(b10)
                    b11 = graph.Edge(b8, b9, type="Product")
                    b6.append(b11)
                else:
                    b8 = graph.Node(n
                    b6.append(b8)
                    b12 = graph.Node(self.b2.tree[w - 1], type="Prime")
                    b6.append(b12)
                    b13 = graph.Edge(b8, b12, type='PrimeLine')
                    b6.append(b13)
        if b6:
            self.fonk3(b6)
    def fonk6(self):
        if not self.b3:
            return 'Rien à ajouter'
        while self.b3:
            b14 = self.b3.pop(0)
            if not self.b2.checktree(b14):
                self.fonk5(b14)
    def fonk7(self, b14):
        if isinstance(b14, int):
            self.fonk5(b14)
        elif isinstance(b14, (list, tuple)):
            for item in b14:
                self.fonk5(item)
        elif isinstance(b14, dict):
            for key in b14:
                self.fonk5(key)
        elif isinstance(b14, str):
            print('Pas de dictionnaire pour les mots actuellement')
        else:
            try:
                for item in b14:
                    self.fonk5(item)
            except Exception:
                print('Objet non reconnu et non utilisable')
    def fonk8(self, b15 = None):
        b15 = b15 or 0
        b16 = ''
        a1 = 2
        while b16 != 'q':
            b16 = input('Entrez q pour arrêter le a1...')
            print(f'Ajout de {a1}...')
            while a1 > 0:
                self.fonk5(a1)
                time.sleep(b15)
                a1 += 1
    def fonk9(self, b15 = None):
        b17 = time.time()
        if b15 and isinstance(b15, int):
            b18 = b17 + b15 * self.b2.tree[-1]
            print(f'Attention, l\'opération prendra {b18 - b17} secondes.')
            b19 = input('Entrez oui pour continuer')
        else:
            b19 = 'oui'
        if b19 = = 'oui':
            b20 = self.b2.tree[-1]
            while b20 >= 2:
                self.fonk5(b20)
                if isinstance(b15, int):
                    time.sleep(b15)
                b20 -= 1