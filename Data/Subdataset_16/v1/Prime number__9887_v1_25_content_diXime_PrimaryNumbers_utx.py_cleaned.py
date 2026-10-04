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
            print("Connected. \
            Ajoutez un referent dans gephi avant d'ajouter des points \
            Gardez ce référent à portée avant d'ajouter des points \
            Connectez-vous en master")
        except Exception as e:
            print(f'Impossible de se connecter au gephistreamer: {e}')
        if isinstance(b1, Ut.Ut):
            self.fonk7(b1.manifold)
    def fonk2(self):
        return 'class1 : {} => {}'.format(self.tree, self.manifold.keys())
    def fonk3(self, b5 = None):
        if not b5:
            return 'Nothing to add'
        if isinstance(b5, graph.Node):
            self.b4.add_node(b5)
        elif isinstance(b5, graph.Edge):
            self.b4.add_edge(b5)
        elif isinstance(b5, list):
            for element in b5:
                self.fonk3(element)
        elif isinstance(b5, (int, str)):
            return 'Objet non graphable immédiatement'
        elif isinstance(b5, dict):
            for key in b5:
                self.fonk3(b5[key])
        else:
            return b5
    def fonk4(self):
        for key, values in self.manifold.items():
            for element in values:
                if isinstance(element, graph.Node):
                    self.b4.delete_node(element)
                elif isinstance(element, graph.Edge):
                    self.b4.delete_edge(element)
            del self.manifold[key]
    def fonk5(self, n):
        b6 = list()
        if not self.b2.tree:
            self.b2.treeme(n)
        if not self.b2.checktree(n):
            b7 = graph.Node(n, b10='Factor')
            b6.append(b7)
        else:
            b7 = graph.Node(n, b10='Prime')
            b6.append(b7)
        for w in range(len(self.b2.tree)):
            if n % self.b2.tree[w] == 0:
                if n / self.b2.tree[w] != 1:
                    b8 = graph.Node(self.b2.tree[w], b10="Prime")
                    b6.append(b8)
                    b9 = graph.Node(n / self.b2.tree[w], b10="Factor")
                    self.b3.append(n / self.b2.tree[w])
                    b6.append(b9)
                    b6.append(graph.Edge(b8, b7, b10 = "Product"))
                    b6.append(graph.Edge(b8, b9, b10 = "Product"))
                elif n != 1:
                    b8 = graph.Node(n / self.b2.tree[w], b10="Prime")
                    b6.append(b8)
                    b11 = graph.Node(self.b2.tree[w - 1], b10="Prime")
                    b6.append(b11)
                    b6.append(graph.Edge(b8, b11, b10 = 'PrimeLine'))
        if b6:
            self.fonk3(b6)
    def fonk6(self):
        if not self.b3:
            return 'Rien à ajouter'
        for key in range(len(self.b3)):
            if self.b2.checktree(self.b3[key]):
                del self.b3[key]
            try:
                self.fonk5(self.b3[key])
            except IndexError:
                b12 = 'Terminé'
                del self.b3
                return b12
        self.b3 = list()
    def fonk7(self, element):
        if isinstance(element, int):
            self.fonk5(element)
        elif isinstance(element, (list, tuple)):
            for item in element:
                self.fonk5(item)
        elif isinstance(element, dict):
            for key in element:
                self.fonk5(key)
        elif isinstance(element, str):
            print('Pas de dictionnaire pour les mots actuellement')
        else:
            try:
                for item in element:
                    self.fonk5(item)
            except Exception as e:
                print(f'Objet non reconnu et non utilisable: {e}')
    def fonk8(self, b13 = None):
        if b13 is None:
            b13 = 0
        a1 = 2
        b14 = ''
        while b14 != 'q':
            b14 = input('Entrez q pour arrêter le a1...')
            print(f'Ajout de {a1}...')
            while a1 > 0:
                self.fonk5(a1)
                time.sleep(b13)
                a1 += 1
    def fonk9(self, b13 = None):
        b15 = time.time()
        if b13 is not None and isinstance(b13, int):
            b16 = b15 + b13 * self.b2.tree[-1]
            print(f'Attention, l\'opération prendra {b16 - b15} secondes.')
            b17 = input('Entrez oui pour continuer')
        else:
            b17 = 'oui'
        if b17 = = 'oui':
            b18 = self.b2.tree[-1]
            while b18 >= 2:
                self.fonk5(b18)
                if isinstance(b13, int):
                    time.sleep(b13)
                b18 -= 1