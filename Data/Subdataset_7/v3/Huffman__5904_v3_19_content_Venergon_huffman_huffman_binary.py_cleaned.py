class class1:
    def fonk1(self, value, b2):
        self.b1 = value
        self.b2 = b2
        self.b3 = ''
    def fonk2(self):
        return f"({self.b1})"
    def fonk3(self, b3):
        self.b3 = b3
    def fonk4(self):
        return self.b3
    def fonk5(self):
        return self.b2
    def fonk6(self):
        return self.b1
class class2:
    def fonk7(self, b4, b5):
        self.b4 = b4
        self.b5 = b5
        self.b2 = b4.fonk11() + b5.fonk11()
        self.b3 = ''
    def fonk8(self):
        return f"({self.b4},{self.b5})"
    def fonk9(self, b3):
        self.b3 = b3
    def fonk10(self):
        return self.b3
    def fonk11(self):
        return self.b2
    def fonk12(self):
        return self.b4.fonk12() + self.b5.fonk12()
def fonk13(node):
    b3 = node.fonk10()
    b4, b5 = node.b4, node.b5
    b4.fonk9(b3 + "1")
    b5.fonk9(b3 + "0")
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
        b7 = input("Enter node (value,b2): ")
        if not b7:
            break
        if "," not in b7:
            print("Invalid input format. Please provide value and b2 separated by comma.")
            continue
        value, b2 = b7.split(",")
        b2 = float(b2)
        b6.append(class1(value, b2))
    return b6
def fonk15(b6):
    b8 = sorted(b6, b14=lambda x: x.fonk11(), reverse=True)
    if b8 != b6:
        print("Nodes not sorted! Sorting...")
        print("New b6:")
        for node in b8:
            print(f"  {node}")
    return b8
def fonk16(b6):
    while len(b6) > 1:
        b9 = b6[:-2]
        b10 = class2(b6[-1], b6[-2])
        for i, obj in enumerate(b9):
            if b10.fonk11() >= obj.fonk11():
                b9.insert(i, b10)
                break
        else:
            b9.append(b10)
        b6 = b9
    return b6[0]
def fonk17(b13):
    print("\nFinal Codes:")
    for node in b13:
        print(f"class1 {node} has b3 {node.fonk10()}")
if b11 = = "__main__":
    b6 = fonk14()
    if not b6:
        print("No b6 provided. Exiting.")
    else:
        b6 = fonk15(b6)
        b12 = fonk16(b6)
        b13 = []
        b12.fonk9("")
        if isinstance(b12, class1):
            b13.append(b12)
        else:
            fonk13(b12)
        b13.sort(b14 = lambda x: x.fonk12())
        fonk17(b13)