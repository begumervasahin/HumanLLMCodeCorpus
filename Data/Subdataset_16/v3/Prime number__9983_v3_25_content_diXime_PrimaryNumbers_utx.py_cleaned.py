import time
from gephistreamer import graph, streamer
import Ut
class class1:
    def fonk1(self, b1 = None):
        self.b2 = Ut.Ut()
        self.b3 = []
        try:
            self.b4 = streamer.Streamer(streamer.GephiWS())
            print("Connected. Please add a referent in Gephi before adding points. Keep this referent available before adding points. Connect as master.")
        except Exception as e:
            print(f'Unable to connect to Gephi streamer: {e}')
        if isinstance(b1, Ut.Ut):
            self.fonk7(b1.manifold)
    def fonk2(self):
        return f'class1 : {self.tree} => {self.manifold.keys()}'
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
            return 'Object not immediately graphable'
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
        b6 = []
        if not self.b2.tree:
            self.b2.treeme(n)
        b7 = graph.Node(n, b11='Prime' if self.b2.checktree(n) else 'Factor')
        b6.append(b7)
        for b8 in self.b2.tree:
            if n % b8 = = 0:
                if n / b8 != 1:
                    b9 = graph.Node(b8, b11="Prime")
                    b10 = graph.Node(n / b8, b11="Factor")
                    self.b3.append(n / b8)
                    b6.extend([
                        b9, b10,
                        graph.Edge(b9, b7, b11 = "Product"),
                        graph.Edge(b9, b10, b11 = "Product")
                    ])
                elif n != 1:
                    b12 = graph.Node(n / b8, b11="Prime")
                    b13 = graph.Node(b8 - 1, b11="Prime")
                    b6.extend([
                        b12, b13,
                        graph.Edge(b12, b13, b11 = 'PrimeLine')
                    ])
        if b6:
            self.fonk3(b6)
    def fonk6(self):
        if not self.b3:
            return 'Nothing to add'
        for i in range(len(self.b3)):
            if self.b2.checktree(self.b3[i]):
                del self.b3[i]
            try:
                self.fonk5(self.b3[i])
            except IndexError:
                del self.b3
                return 'Completed'
        self.b3 = []
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
            print('Dictionary for words is currently not supported')
        else:
            try:
                for item in element:
                    self.fonk5(item)
            except Exception as e:
                print(f'Unrecognized and unusable object: {e}')
    def fonk8(self, b14 = None):
        if b14 is None:
            b14 = 0
        a1 = 2
        while True:
            b15 = input('Enter q to stop the flow...').strip()
            if b15.lower() == 'q':
                break
            print(f'Adding {a1}...')
            self.fonk5(a1)
            time.sleep(b14)
            a1 += 1
    def fonk9(self, b14 = None):
        b16 = time.time()
        if b14 is not None and isinstance(b14, int):
            b17 = b16 + b14 * self.b2.tree[-1]
            print(f'Warning: the operation will take {b17 - b16} seconds.')
            b18 = input('Enter yes to continue').strip().lower()
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
    b21.fonk8()