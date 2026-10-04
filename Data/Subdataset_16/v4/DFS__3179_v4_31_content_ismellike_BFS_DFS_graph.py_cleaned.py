class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = []
        self.b3 = False
    def fonk2(self, b8):
        self.b2.append(b8)
class class2:
    def fonk3(self, b4, b5):
        self.b4 = b4
        self.b5 = b5
    def fonk4(self):
        b6 = [f"Head node b1: {self.b4}"]
        for node in self.b5:
            b6.append(f"class1 {node.b1} has b2 {node.b2}")
        return "\n".join(b6)
def fonk5(b10):
    with open(b10, "r") as file:
        b4 = int(file.readline().strip())
        b5 = []
        a1 = -1
        b7 = None
        for line in file:
            parent_index, b8 = map(int, line.strip().split(','))
            if a1 = = parent_index:
                b7.fonk2(b8)
            else:
                if b7 is not None:
                    b5.append(b7)
                a1 = parent_index
                b7 = class1(parent_index)
                b7.fonk2(b8)
        if b7 is not None:
            b5.append(b7)
    return class2(b4, b5)
if b9 = = "__main__":
    b10 = 'graph_data.txt'
    b11 = fonk5(b10)
    print(b11)