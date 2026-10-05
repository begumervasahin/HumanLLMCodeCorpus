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
        self.b3 = list()
        try:
            self.b4 = streamer.Streamer(streamer.GephiWS())
            print("Connected. Add a reference b7 in Gephi before adding points.")
            print("Keep this reference b7 in range before adding points. Connect in master mode.")
        except:
            print('Failed to connect to Gephistreamer.')
        if isinstance(b1, Ut.Ut):
            self.fonk7(b1.manifold)
    def fonk2(self):
        return 'class1 : {} => {}'.format(self.tree, self.manifold.keys())
    def fonk3(self, b5 = None):
        if not b5 or b5 is None:
            return 'Nothing to add'
        elif isinstance(b5, graph.Node):
            self.b4.add_node(b5)
        elif isinstance(b5, graph.Edge):
            self.b4.add_edge(b5)
        elif isinstance(b5, list):
            for elem in b5:
                self.fonk3(elem)
        elif isinstance(b5, int) or isinstance(b5, str):
            return 'Object cannot be immediately graphed'
        elif isinstance(b5, dict):
            for a1 in b5.keys():
                self.fonk3(b5[a1])
        else:
            return b5
    def fonk4(self):
        for a1, values in self.manifold.items():
            for item in values:
                if isinstance(item, graph.Node):
                    self.b4.delete_node(item)
                elif isinstance(item, graph.Edge):
                    self.b4.delete_edge(item)
            del self.manifold[a1]
    def fonk5(self, n):
        b6 = []
        if not self.b2.tree:
            self.b2.treeme(n)
        if not self.b2.checktree(n):
            b7 = graph.Node(n, type='Factor')
            b6.append(b7)
        else:
            b7 = graph.Node(n, type='Prime')
            b6.append(b7)
        for w in range(len(self.b2.tree)):
            if n % self.b2.tree[w] == 0 and n / self.b2.tree[w] != 1:
                b8 = graph.Node(self.b2.tree[w], type="Prime")
                b6.append(b8)
                b9 = graph.Node(n / self.b2.tree[w], type="Factor")
                self.b3.append(n / self.b2.tree[w])
                b6.append(b9)
                b10 = graph.Edge(b8, b7, type="Product")
                b6.append(b10)
                b11 = graph.Edge(b8, b9, type="Product")
                b6.append(b11)
            elif n % self.b2.tree[w] == 0 and n / self.b2.tree[w] == 1 and n != 1:
                b8 = graph.Node(n / self.b2.tree[w], type="Prime")
                b6.append(b8)
                b12 = graph.Node(self.b2.tree[w - 1], type="Prime")
                b6.append(b12)
                b13 = graph.Edge(b8, b12, type='PrimeLine')
                b6.append(b13)
        if b6:
            self.fonk3(b6)
    def fonk6(self):
        if not self.b3:
            return 'Nothing to add'
        a1 = 0
        while a1 < len(self.b3):
            if self.b2.checktree(self.b3[a1]):
                del self.b3[a1]
            try:
                self.fonk5(self.b3[a1])
            except IndexError:
                b14 = 'Finished'
                del self.b3
                return b14
            a1 += 1
        self.b3 = []
    def fonk7(self, element):
        if isinstance(element, int):
            self.fonk5(element)
        elif isinstance(element, (list, tuple)):
            for a1 in element:
                self.fonk5(a1)
        elif isinstance(element, dict):
            for a1 in element.keys():
                self.fonk5(a1)
        elif isinstance(element, str):
            print('No dictionaries for words currently')
        else:
            for a1 in element:
                self.fonk5(a1)
    def fonk8(self, b15 = None):
        if b15 is None:
            b15 = 0
        b16 = ''
        a2 = 2
        while b16 != 'q':
            b16 = input('Enter q to stop the flow...')
            print('Adding {}...'.format(a2))
            for _ in range(a2):
                self.fonk5(a2)
                time.sleep(b15)
                a2 += 1
    def fonk9(self, b15 = None):
        b17 = time.time()
        if b15 and isinstance(b15, int):
            b18 = b17 + b15 * self.b2.tree[-1]
            print('This operation will take {} seconds.'.format(b18 - b17))
            b19 = input('Enter "yes" to continue')
        else:
            b19 = 'yes'
        if b19 = = 'yes':
            b20 = self.b2.tree[-1]
            while b20 >= 2:
                self.fonk5(b20)
                if isinstance(b15, int):
                    time.sleep(b15)
                b20 -= 1
if b21 = = '__main__':
    b22 = class1()
    b22.fonk8()