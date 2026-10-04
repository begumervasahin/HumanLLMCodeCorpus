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
        self.b5 = {}
    def fonk4(self, node):
        self.b5[node.b1] = node
    def fonk5(self):
        b6 = [f"Head node b1: {self.b4}"]
        for node in self.b5.values():
            b6.append(f"class1 {node.b1} has b2 {node.b2}")
        return "\n".join(b6)
def fonk6(b10):
    with open(b10, "r") as file:
        b4 = int(file.readline().strip())
        b7 = class2(b4)
        for line in file:
            parent_index, b8 = map(int, line.strip().split(','))
            if parent_index not in b7.b5:
                b7.fonk4(class1(parent_index))
            b7.b5[parent_index].fonk2(b8)
            if b8 not in b7.b5:
                b7.fonk4(class1(b8))
    return b7
if b9 = = "__main__":
    b10 = 'graph_data.txt'
    b7 = fonk6(b10)
    print(b7)