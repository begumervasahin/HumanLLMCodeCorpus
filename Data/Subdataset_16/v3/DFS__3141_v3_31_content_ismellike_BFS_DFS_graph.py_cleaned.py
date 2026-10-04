class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = []
        self.b3 = False
    def fonk2(self, b9):
        self.b2.append(b9)
class class2:
    def fonk3(self, b4):
        self.b4 = b4
        self.b5 = []
    def fonk4(self, node):
        self.b5.append(node)
    def fonk5(self):
        b6 = [f"Head node b1: {self.b4}"]
        for node in self.b5:
            b6.append(f"class1 {node.b1} has b2 {node.b2}")
        return "\n".join(b6)
def fonk6(b11):
    with open(b11, 'r') as file:
        b4 = int(file.readline().strip())
        b7 = class2(b4)
        a1 = -1
        b8 = None
        for line in file:
            parent_index, b9 = map(int, line.strip().split(','))
            if a1 = = parent_index:
                b8.fonk2(b9)
            else:
                if b8 is not None:
                    b7.fonk4(b8)
                a1 = parent_index
                b8 = class1(parent_index)
                b8.fonk2(b9)
        if b8 is not None:
            b7.fonk4(b8)
    return b7
if b10 = = "__main__":
    b11 = 'graph_data.txt'
    b7 = fonk6(b11)
    print(b7)