import argparse
class class1:
    def fonk1(self, b3, b1):
        self.b1 = b1
        self.b2 = {}
        self.b2[b3] = 0
        self.b3 = b3
        self.b4 = list(b1.keys())
        self.b4.remove(b3)
        self.b4.insert(0, b3)
        self.fonk2()
        self.fonk3()
    def fonk2(self):
        for _ in range(len(self.b1) - 1):
            for node in self.b4:
                for neighbor, weight in self.b1[node].items():
                    if self.b2[node] == float('inf'):
                        break
                    elif self.b2[neighbor] == float('inf'):
                        self.b2[neighbor] = weight + self.b2[node]
                    elif weight + self.b2[node] < self.b2[neighbor]:
                        self.b2[neighbor] = weight + self.b2[node]
        print(self.b2)
    def fonk3(self):
        for node in self.b4:
            for neighbor, weight in self.b1[node].items():
                if weight + self.b2[node] < self.b2[neighbor]:
                    print('The Graph has a negative-weight cycle')
if b5 = = '__main__':
    b6 = argparse.ArgumentParser()
    b6.add_argument('-n', '--node', b7 = str, required=True, help='Starting node')
    b8 = b6.parse_args()
    b1 = {
        'A': {'B': 6, 'C': 7},
        'B': {'C': 8, 'D': 5, 'E': -4},
        'C': {'D': -3, 'E': 9},
        'D': {'B': -2},
        'E': {'A': 2}
    }
    class1(b8.node, b1)