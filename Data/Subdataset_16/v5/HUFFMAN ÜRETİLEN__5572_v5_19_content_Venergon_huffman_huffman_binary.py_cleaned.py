class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
        self.b3 = ""
    def fonk2(self):
        return f"({self.b1})"
    def fonk3(self, b3):
        self.b3 = b3
    def fonk4(self):
        return self.b3
class class2(class1):
    def fonk5(self, b4, b5):
        super().fonk5(b4.b1 + b5.b1, b4.b2 + b5.b2)
        self.b4 = b4
        self.b5 = b5
    def fonk6(self):
        return f"({self.b4},{self.b5})"
def fonk7(node, b11):
    b4, b5 = node.b4, node.b5
    b4.fonk3(node.fonk4() + "1")
    b5.fonk3(node.fonk4() + "0")
    if isinstance(b4, class2):
        fonk7(b4, b11)
    else:
        b11.append(b4)
    if isinstance(b5, class2):
        fonk7(b5, b11)
    else:
        b11.append(b5)
def fonk8(b7):
    while len(b7) > 1:
        b4, b5 = b7.pop(), b7.pop()
        b6 = class2(b4, b5)
        for i, node in enumerate(b7):
            if b6.b2 >= node.b2:
                b7.insert(i, b6)
                break
        else:
            b7.append(b6)
    return b7[0]
def fonk9():
    b7 = []
    while True:
        b8 = input("Enter node (format: b1,b2) or leave empty to finish: ")
        if not b8:
            break
        try:
            b1, b2 = b8.split(",")
            b2 = float(b2.strip())
            b7.append(class1(b1.strip(), b2))
        except ValueError:
            print("Invalid input format. Please enter in format: b1,b2")
    if not b7:
        print("No b7 entered. Exiting.")
        return
    b7.sort(b9 = lambda x: x.b2, reverse=True)
    print("Nodes sorted by b2:")
    for node in b7:
        print(f"  {node}")
    b10 = fonk8(b7)
    b11 = []
    if isinstance(b10, class2):
        fonk7(b10, b11)
    else:
        b11.append(b10)
    b11.sort(b9 = lambda x: x.b1)
    print("\nHuffman Codes:")
    for node in b11:
        print(f"class1 {node.b1} has b3 {node.fonk4()}")
if b12 = = "__main__":
    fonk9()