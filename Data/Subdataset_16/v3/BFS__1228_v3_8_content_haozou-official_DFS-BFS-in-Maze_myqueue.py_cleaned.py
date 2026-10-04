class class1:
    def fonk1(self):
        self.b1 = []
    def fonk2(self, item):
        self.b1.insert(0, item)
    def fonk3(self):
        return self.b1.fonk8()
    def fonk4(self):
        return not self.b1
    def fonk5(self):
        return len(self.b1)
class class2:
    def fonk6(self):
        self.b1 = []
    def fonk7(self, item):
        self.b1.append(item)
    def fonk8(self):
        return self.b1.fonk8()
    def fonk9(self):
        return not self.b1
    def fonk10(self):
        return len(self.b1)
def fonk11(b6, b7, b8):
    b2 = class1()
    b2.fonk2(b7)
    b3 = {b7: None}
    while not b2.fonk9():
        b4 = b2.fonk3()
        if b4 = = b8:
            return fonk13(b3, b7, b8)
        for next_node in b6[b4]:
            if next_node not in b3:
                b2.fonk2(next_node)
                b3[next_node] = b4
    return None
def fonk12(b6, b7, b8):
    b2 = class2()
    b2.fonk7(b7)
    b3 = {b7: None}
    while not b2.fonk9():
        b4 = b2.fonk8()
        if b4 = = b8:
            return fonk13(b3, b7, b8)
        for next_node in b6[b4]:
            if next_node not in b3:
                b2.fonk7(next_node)
                b3[next_node] = b4
    return None
def fonk13(b3, b7, b8):
    b4 = b8
    b5 = []
    while b4 != b7:
        b5.append(b4)
        b4 = b3[b4]
    b5.append(b7)
    b5.reverse()
    return b5
def fonk14():
    b6 = {
        'A': ['B', 'C', 'E'],
        'B': ['A', 'D', 'F'],
        'C': ['A', 'G'],
        'D': ['B'],
        'E': ['A', 'F'],
        'F': ['B', 'E', 'H'],
        'G': ['C', 'H'],
        'H': ['F', 'G']
    }
    b7 = 'A'
    b8 = 'H'
    print(f"BFS Path from {b7} to {b8}:")
    b9 = fonk11(b6, b7, b8)
    print(b9)
    print(f"\nDFS Path from {b7} to {b8}:")
    b10 = fonk12(b6, b7, b8)
    print(b10)
if b11 = = '__main__':
    fonk14()