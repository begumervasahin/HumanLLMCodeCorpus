class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = []
        self.b3 = False
    def fonk2(self, b8):
        self.b2.append(b8)
class class2:
    def fonk3(self, b4):
        self.b4 = b4
        self.b5 = []
    def fonk4(self, node):
        self.b5.append(node)
def fonk5(b10):
    with open(b10, 'r') as file:
        b4 = int(file.readline().strip())
        b6 = class2(b4)
        a1 = -1
        b7 = None
        for line in file:
            parent_index, b8 = map(int, line.strip().split(','))
            if a1 = = parent_index:
                b7.fonk2(b8)
            else:
                if b7 is not None:
                    b6.fonk4(b7)
                a1 = parent_index
                b7 = class1(parent_index)
                b7.fonk2(b8)
        if b7 is not None:
            b6.fonk4(b7)
    return b6
if b9 = = "__main__":
    b10 = 'graph_data.txt'
    b6 = fonk5(b10)
    print(f"Head node b1: {b6.b4}")
    for node in b6.b5:
        print(f"class1 {node.b1} has b2 {node.b2}")