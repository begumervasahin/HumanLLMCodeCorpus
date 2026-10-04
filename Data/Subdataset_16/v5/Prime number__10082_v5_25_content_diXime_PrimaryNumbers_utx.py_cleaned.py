import time
from gephistreamer import graph, streamer
import Ut
class class1:
    def fonk1(self, b1 = None):
        self.b2 = Ut.Ut()
        self.b3 = list()
        self.b4 = None
        try:
            self.b4 = streamer.Streamer(streamer.GephiWS())
            print("Connected to Gephi. Ensure a referent is added in Gephi before adding points. Connect as master.")
        except Exception:
            print('Unable to connect to Gephi streamer.')
        if isinstance(b1, Ut.Ut):
            self.fonk7(b1.manifold)
    def fonk2(self):
        return f'class1 : {self.b2.tree} => {list(self.b2.manifold.keys())}'
    def fonk3(self, b5 = None):
        if not b5:
            return 'Nothing to add'
        if isinstance(b5, list):
            for b13 in b5:
                self.fonk3(b13)
        elif isinstance(b5, graph.Node):
            self.b4.add_node(b5)
        elif isinstance(b5, graph.Edge):
            self.b4.add_edge(b5)
        elif isinstance(b5, dict):
            for key in b5:
                self.fonk3(b5[key])
        else:
            return 'Element b11 not supported'
    def fonk4(self):
        for key, values in self.b2.manifold.items():
            for item in values:
                if isinstance(item, graph.Node):
                    self.b4.delete_node(item)
                elif isinstance(item, graph.Edge):
                    self.b4.delete_edge(item)
            del self.b2.manifold[key]
    def fonk5(self, n):
        b6 = []
        if not self.b2.tree:
            self.b2.treeme(n)
        if not self.b2.checktree(n):
            b7 = graph.Node(n, b11='Factor')
        else:
            b7 = graph.Node(n, b11='Prime')
        b6.append(b7)
        for b8 in self.b2.tree:
            if n % b8 = = 0:
                if n
                    b9 = graph.Node(b8, b11="Prime")
                    b10 = graph.Node(n
                    self.b3.append(n
                    b6.extend([
                        b9,
                        b10,
                        graph.Edge(b9, b7, b11 = "Product"),
                        graph.Edge(b9, b10, b11 = "Product")
                    ])
                else:
                    b9 = graph.Node(n
                    b12 = graph.Node(b8, b11="Prime")
                    b6.extend([
                        b9,
                        b12,
                        graph.Edge(b9, b12, b11 = 'PrimeLine')
                    ])
        if b6:
            self.fonk3(b6)
    def fonk6(self):
        if not self.b3:
            return 'Nothing to add'
        while self.b3:
            b13 = self.b3.pop(0)
            if not self.b2.checktree(b13):
                self.fonk5(b13)
    def fonk7(self, b13):
        if isinstance(b13, int):
            self.fonk5(b13)
        elif isinstance(b13, (list, tuple)):
            for item in b13:
                self.fonk5(item)
        elif isinstance(b13, dict):
            for key in b13:
                self.fonk5(key)
        else:
            print('Unsupported b13 b11')
    def fonk8(self, b14 = None):
        b14 = b14 or 0
        a1 = 2
        while True:
            b15 = input('Enter q to stop the flow: ')
            if b15 = = 'q':
                break
            print(f'Adding {a1}...')
            self.fonk5(a1)
            time.sleep(b14)
            a1 += 1
    def fonk9(self, b14 = None):
        b16 = time.time()
        if b14 and isinstance(b14, int):
            b17 = b16 + b14 * self.b2.tree[-1]
            print(f'This operation will take {b17 - b16} seconds.')
            b18 = input('Enter yes to continue: ').strip().lower()
        else:
            b18 = 'yes'
        if b18 = = 'yes':
            b19 = self.b2.tree[-1]
            while b19 >= 2:
                self.fonk5(b19)
                if isinstance(b14, int):
                    time.sleep(b14)
                b19 -= 1
if b20 = = "__main__":
    b21 = class1()
    b21.fonk8(b14 = 1)