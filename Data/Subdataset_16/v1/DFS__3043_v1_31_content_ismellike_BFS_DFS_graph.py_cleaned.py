class class1:
    def fonk1(self, b2):
        self.b1 = []
        self.b2 = b2
        self.b3 = False
    def fonk2(self, b2):
        self.b1.append(b2)
class class2:
    def fonk3(self, b4, b5):
        self.b4 = b4
        self.b5 = b5
def fonk4(path):
    b5 = []
    with open(path, "r") as file:
        b4 = int(file.readline().strip())
        a1 = -1
        b6 = None
        for line in file:
            split1, b7 = map(int, line.strip().split(','))
            if a1 = = split1:
                b6.fonk2(b7)
            else:
                if a1 != -1:
                    b5.append(b6)
                a1 = split1
                b6 = class1(split1)
                b6.fonk2(b7)
        if b6:
            b5.append(b6)
    return class2(b4, b5)
if b8 = = "__main__":
    b9 = 'graph_data.txt'
    b10 = fonk4(b9)
    print(f"Head node: {b10.b4}")
    for node in b10.b5:
        print(f"class1 {node.b2} has b1 {node.b1}")