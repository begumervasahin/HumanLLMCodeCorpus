import argparse
class class1:
    def fonk1(self, b3, b1):
        self.b1 = b1
        self.b2 = {node: float('inf') for node in b1}
        self.b2[b3] = 0
        self.b3 = b3
        self.fonk2()
        self.fonk3()
    def fonk2(self):
        b4 = len(self.b1)
        for _ in range(b4 - 1):
            for node in self.b1:
                for neighbor, weight in self.b1[node].items():
                    if self.b2[node] == float('inf'):
                        continue
                    b5 = self.b2[node] + weight
                    if b5 < self.b2[neighbor]:
                        self.b2[neighbor] = b5
        print("Shortest b2 from", self.b3 + ":", self.b2)
    def fonk3(self):
        for node in self.b1:
            for neighbor, weight in self.b1[node].items():
                if self.b2[node] + weight < self.b2[neighbor]:
                    print('The b1 has a negative-weight cycle.')
if b6 = = '__main__':
    b7 = argparse.ArgumentParser()
    b7.add_argument('-n', '--node', b8 = str, required=True, help='Starting node')
    b9 = b7.parse_args()
    b1 = {
        'A': {'B': 6, 'C': 7},
        'B': {'C': 8, 'D': 5, 'E': -4},
        'C': {'D': -3, 'E': 9},
        'D': {'B': -2},
        'E': {'A': 2}
    }
    b10 = class1(b9.node, b1)