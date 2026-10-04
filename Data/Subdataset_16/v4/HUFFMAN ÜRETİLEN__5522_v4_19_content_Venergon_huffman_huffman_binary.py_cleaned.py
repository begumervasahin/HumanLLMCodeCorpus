class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
        self.b3 = ""
    def fonk2(self):
        return f"({self.b1})"
    def fonk3(self):
        return self.b2
    def fonk4(self):
        return self.b1
    def fonk5(self, b3):
        self.b3 = b3
    def fonk6(self):
        return self.b3
class class2:
    def fonk7(self, b4, b5):
        self.b4 = b4
        self.b5 = b5
        self.b2 = b4.fonk9() + b5.fonk9()
        self.b3 = ""
    def fonk8(self):
        return f"({self.b4},{self.b5})"
    def fonk9(self):
        return self.b2
    def fonk10(self):
        return self.b4.fonk10() + self.b5.fonk10()
    def fonk11(self, b3):
        self.b3 = b3
    def fonk12(self):
        return self.b3
def fonk13(node, b7):
    b3 = node.fonk12()
    b4, b5 = node.b4, node.b5
    b4.fonk11(b3 + "1")
    b5.fonk11(b3 + "0")
    if isinstance(b4, class2):
        fonk13(b4, b7)
    else:
        b7.append(b4)
    if isinstance(b5, class2):
        fonk13(b5, b7)
    else:
        b7.append(b5)
def fonk14():
    b6 = []
    b7 = []
    while True:
        b8 = input("Enter node (format: b1,b2) or leave empty to finish: ")
        if not b8:
            break
        try:
            b1, b2 = b8.split(",")
            b2 = float(b2)
            b6.append(class1(b1.strip(), b2))
        except ValueError:
            print("Invalid input format. Please enter in format: b1,b2")
    if b6 and sorted(b6, b9 = lambda x: x.fonk9(), reverse=True) != b6:
        print("Nodes not sorted! Sorting...")
        b6.sort(b9 = lambda x: x.fonk9(), reverse=True)
        print("New b6 order:")
        for node in b6:
            print(f"  {node}")
    while len(b6) > 1:
        b10 = b6[:-2]
        b11 = class2(b6[-1], b6[-2])
        for i, obj in enumerate(b10):
            if b11.fonk9() >= obj.fonk9():
                b10.insert(i, b11)
                break
        else:
            b10.append(b11)
        b6 = b10
    if len(b6) == 1:
        b12 = b6[0]
        b12.fonk11("")
        if isinstance(b12, class1):
            b7.append(b12)
        else:
            fonk13(b12, b7)
    b7.sort(b9 = lambda x: x.fonk10())
    print("\nHuffman Codes:")
    for node in b7:
        print(f"class1 {node.fonk10()} has b3 {node.fonk12()}")
if b13 = = "__main__":
    fonk14()