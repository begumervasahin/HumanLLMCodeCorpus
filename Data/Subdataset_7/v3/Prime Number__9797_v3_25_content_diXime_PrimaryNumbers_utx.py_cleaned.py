import sys
import time
from datetime import date
from itertools import count, islice
from math import sqrt
from functools import reduce
from gephistreamer import graph, streamer
import Ut
class class1:
    def fonk1(self, b1 = None):
        self.b2 = Ut.Ut()
        self.b3 = []
        try:
            self.b4 = streamer.Streamer(streamer.GephiWS())
            print("Connected to Gephistreamer. Add a reference b6 in Gephi before adding points.")
            print("Keep this reference b6 in range before adding points. Connect in master mode.")
        except:
            print('Failed to connect to Gephistreamer.')
        if isinstance(b1, Ut.Ut):
            self.fonk7(b1.manifold)
    def fonk2(self):
        return 'class1 : {} => {}'.format(self.tree, self.manifold.keys())
    def fonk3(self, b5 = None):
        if not b5:
            return 'Nothing to add'
        if isinstance(b5, (graph.Node, graph.Edge)):
            self.b4.add_node(b5) if isinstance(b5, graph.Node) else self.b4.add_edge(b5)
        elif isinstance(b5, (list, tuple)):
            for elem in b5:
                self.fonk3(elem)
        elif isinstance(b5, dict):
            for val in b5.values():
                self.fonk3(val)
        elif isinstance(b5, (int, str)):
            return 'Object cannot be immediately graphed'
        else:
            return b5
    def fonk4(self):
        for values in self.manifold.values():
            for item in values:
                self.b4.delete_node(item) if isinstance(item, graph.Node) else self.b4.delete_edge(item)
            self.manifold.clear()
    def fonk5(self, num):
        b5 = []
        if not self.b2.tree:
            self.b2.tree_me(num)
        if not self.b2.check_tree(num):
            b6 = graph.Node(num, b9='Factor')
            b5.append(b6)
        else:
            b6 = graph.Node(num, b9='Prime')
            b5.append(b6)
        for b7 in self.b2.tree:
            if num % b7 = = 0 and num / b7 != 1:
                b8 = graph.Node(b7, b9="Prime")
                b5.extend([b8, graph.Node(num / b7, b9 = "Factor")])
                b5.extend([
                    graph.Edge(b8, b6, b9 = "Product"),
                    graph.Edge(b8, graph.Node(num / b7, b9 = "Factor"), b9="Product")
                ])
            elif num % b7 = = 0 and num / b7 == 1 and num != 1:
                b8 = graph.Node(num / b7, b9="Prime")
                b10 = graph.Node(self.b2.tree[self.b2.tree.index(b7) - 1], b9="Prime")
                b5.extend([b8, b10, graph.Edge(b8, b10, b9 = 'PrimeLine')])
        if b5:
            self.fonk3(b5)
    def fonk6(self):
        if not self.b12:
            return 'Nothing to add'
        a1 = 0
        while a1 < len(self.b12):
            if self.b2.check_tree(self.b12[a1]):
                del self.b12[a1]
            try:
                self.fonk5(self.b12[a1])
            except IndexError:
                b11 = 'Finished'
                del self.b12
                return b11
            a1 += 1
        self.b12 = []
    def fonk7(self, element):
        if isinstance(element, (int, list, tuple, dict)):
            for key in element if isinstance(element, dict) else element:
                self.fonk5(key)
        elif isinstance(element, str):
            print('No dictionaries for words currently')
        else:
            for key in element:
                self.fonk5(key)
    def fonk8(self, b13 = None):
        b13 = b13 or 0
        a2 = 2
        while True:
            b14 = input('Enter "q" to stop the flow...')
            if b14 = = 'q':
                break
            print('Adding {}...'.format(a2))
            for _ in range(a2):
                self.fonk5(a2)
                time.sleep(b13)
                a2 += 1
    def fonk9(self, b13 = None):
        b13 = b13 or 0
        b15 = self.b2.tree[-1]
        if not b13:
            return
        b16 = time.time()
        b17 = b16 + b13 * b15
        print(f'This operation will take {b17 - b16} seconds.')
        b18 = input('Enter "yes" to continue: ')
        if b18 != 'yes':
            return
        for val in range(b15, 1, -1):
            self.fonk5(val)
            time.sleep(b13)
if b19 = = '__main__':
    b20 = class1()
    b20.fonk8()