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
def fonk13(node):
    b3 = node.fonk12()
    b4, b5 = node.b4, node.b5
    b4.fonk11(b3 + "1")
    b5.fonk11(b3 + "0")
    if isinstance(b4, class2):
        fonk13(b4)
    else:
        b13.append(b4)
    if isinstance(b5, class2):
        fonk13(b5)
    else:
        b13.append(b5)
def fonk14():
    b6 = []
    while True:
        b7 = input("Enter node (b1, b2): ").strip()
        if not b7:
            break
        if "," not in b7:
            print("Invalid input format. Please enter (b1, b2).")
            continue
        b1, b2 = b7.split(",")
        b2 = float(b2)
        b6.append(class1(b1, b2))
    return b6
def fonk15(b6):
    if sorted(b6, b8 = lambda x: x.fonk9(), reverse=True) != b6:
        print("Nodes are not sorted! Sorting...")
        b6.sort(b8 = lambda x: x.fonk9(), reverse=True)
        print("New b6:")
        for node in b6:
            print("  " + str(node))
    return b6
def fonk16(b6):
    while len(b6) > 1:
        b9 = b6[:-2]
        b10 = class2(b6[-1], b6[-2])
        for i, obj in enumerate(b9):
            if b10.fonk9() >= obj.fonk9():
                b9.insert(i, b10)
                break
        else:
            b9.append(b10)
        b6 = b9
    assert len(b6) == 1
    return b6[0]
def fonk17():
    b6 = fonk14()
    b6 = fonk15(b6)
    b11 = fonk16(b6)
    b11.fonk11("")
    if isinstance(b11, class1):
        b13.append(b11)
    else:
        fonk13(b11)
    b13.sort(b8 = lambda x: x.fonk10())
    print()
    for node in b13:
        print(f"class1 {node} has b3 {node.fonk12()}")
if b12 = = "__main__":
    b13 = []
    fonk17()