import sys
import time
from datetime import date
from math import sqrt
from functools import reduce
from itertools import count, islice
from gephistreamer import graph, streamer
import Ut
class class1:
    def fonk1(self, b1 = None):
        self.b2 = Ut.Ut()
        self.b3 = list()
        try:
            self.b4 = streamer.Streamer(streamer.GephiWS())
            print("Connected. Add a reference b8 in Gephi before adding points.")
            print("Keep this reference b8 accessible before adding points.")
            print("Connect as master.")
        except:
            print('Failed to connect to Gephistreamer.')
        if isinstance(b1, Ut.Ut):
            self.fonk7(b1.manifold)
    def fonk2(self):
        return 'class1 : {} => {}'.format(self.tree, self.manifold.keys())
    def fonk3(self, b5 = None):
        if not b5 or b5 is None:
            return 'nothing to add'
        elif isinstance(b5, graph.Node):
            self.b4.add_node(b5)
        elif isinstance(b5, graph.Edge):
            self.b4.add_edge(b5)
        elif isinstance(b5, list):
            for item in b5:
                self.fonk3(item)
        elif isinstance(b5, (int, str)):
            return 'Object not graphable immediately'
        elif isinstance(b5, dict):
            for value in b5.values():
                self.fonk3(value)
        else:
            return b5
    def fonk4(self):
        for a3, values in self.manifold.items():
            b6 = self.manifold[a3]
            a1 = 0
            while a1 < len(b6):
                if isinstance(b6[a1], graph.Node):
                    self.b4.delete_node(b6[a1])
                elif isinstance(b6[a1], graph.Edge):
                    self.b4.delete_edge(b6[a1])
                a1 += 1
            del self.manifold[a3]
    def fonk5(self, n):
        b7 = list()
        if not self.b2.tree:
            self.b2.treeme(n)
        if not self.b2.checktree(n):
            b8 = graph.Node(n, type='Factor')
            b7.append(b8)
        else:
            b8 = graph.Node(n, type='Prime')
            b7.append(b8)
        a2 = 0
        while a2 < len(self.b2.tree):
            if n % self.b2.tree[a2] == 0 and n / self.b2.tree[a2] != 1:
                b9 = graph.Node(self.b2.tree[a2], type="Prime")
                b7.append(b9)
                b10 = graph.Node(n / self.b2.tree[a2], type="Factor")
                self.b3.append(n / self.b2.tree[a2])
                b7.append(b10)
                b11 = graph.Edge(b9, b8, type="Product")
                b7.append(b11)
                b12 = graph.Edge(b9, b10, type="Product")
                b7.append(b12)
            elif n % self.b2.tree[a2] == 0 and n / self.b2.tree[a2] == 1 and n != 1:
                b9 = graph.Node(n / self.b2.tree[a2], type="Prime")
                b7.append(b9)
                b13 = graph.Node(self.b2.tree[a2 - 1], type="Prime")
                b7.append(b13)
                b14 = graph.Edge(b9, b13, type='PrimeLine')
                b7.append(b14)
            a2 += 1
        if b7:
            self.fonk3(b7)
    def fonk6(self):
        if not self.b3:
            return 'Nothing to add'
        a3 = 0
        while a3 < len(self.b3):
            if self.b2.checktree(self.b3[a3]):
                del self.b3[a3]
            try:
                self.fonk5(self.b3[a3])
            except IndexError:
                b15 = 'Terminated'
                del self.b3
                return b15
            a3 += 1
        self.b3 = list()
    def fonk7(self, element):
        if isinstance(element, int):
            self.fonk5(element)
        elif isinstance(element, (list, tuple)):
            for item in element:
                self.fonk5(item)
        elif isinstance(element, dict):
            for a3 in element.keys():
                self.fonk5(a3)
        elif isinstance(element, str):
            print('No dictionaries for words currently')
        else:
            try:
                for item in element:
                    self.fonk5(item)
            except:
                print('Unrecognized and unusable object')
    def fonk8(self, b16 = None):
        if b16 is None:
            b16 = 0
        b17 = str()
        a4 = 2
        while b17 != 'q':
            b17 = raw_input('Enter q to stop the flow...')
            print('Adding {}...'.format(a4))
            while a4 > 0:
                self.fonk5(a4)
                time.sleep(b16)
                a4 += 1
    def fonk9(self, b16 = None):
        b18 = time.time()
        if b16 and isinstance(b16, int):
            b19 = b18 + b16 * self.b2.tree[-1]
            print('Attention, the operation will take {} seconds.'.format(b19 - b18))
            b20 = raw_input('Enter yes to continue')
        else:
            b20 = 'yes'
        if b20 = = 'yes':
            b21 = self.b2.tree[-1]
            while b21 >= 2:
                self.fonk5(b21)
                if isinstance(b16, int):
                    time.sleep(b16)
                b21 -= 1