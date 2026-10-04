class class1:
    def fonk1(self, value, b2):
        self.b1 = value
        self.b2 = b2
        self.b3 = ""
    def fonk2(self):
        return f"({self.b1})"
    def fonk3(self, b3):
        self.b3 = b3
    def fonk4(self):
        return self.b3
class class2:
    def fonk5(self, b4, b5):
        self.b4 = b4
        self.b5 = b5
        self.b2 = b4.b2 + b5.b2
        self.b3 = ""
    def fonk6(self):
        return f"({self.b4},{self.b5})"
    def fonk7(self, b3):
        self.b3 = b3
    def fonk8(self):
        return self.b3
def fonk9(node, b10):
    b3 = node.fonk8()
    b4, b5 = node.b4, node.b5
    b4.fonk7(b3 + "1")
    b5.fonk7(b3 + "0")
    if isinstance(b4, class2):
        fonk9(b4, b10)
    else:
        b10.append(b4)
    if isinstance(b5, class2):
        fonk9(b5, b10)
    else:
        b10.append(b5)
def fonk10():
    b6 = []
    while True:
        b7 = input("Enter node (or leave blank to stop): ")
        if not b7:
            break
        if "," not in b7:
            print("Invalid input. Please use the format 'value,b2'.")
            continue
        value, b2 = b7.split(",")
        b6.append(class1(value, float(b2)))
    if not b6:
        print("No b6 entered. Exiting.")
        return
    b6.sort(b8 = lambda x: x.b2, reverse=True)
    print("Nodes sorted by b2:")
    for node in b6:
        print(f"  {node}")
    while len(b6) > 1:
        b6.sort(b8 = lambda x: x.b2)
        b4 = b6.pop(0)
        b5 = b6.pop(0)
        b9 = class2(b4, b5)
        b6.append(b9)
    b10 = []
    b11 = b6[0]
    b11.fonk7("")
    if isinstance(b11, class1):
        b10.append(b11)
    else:
        fonk9(b11, b10)
    b10.sort(b8 = lambda x: x.b1)
    print("\nHuffman Codes:")
    for node in b10:
        print(f"class1 {node} has b3 {node.fonk8()}")
if b12 = = "__main__":
    fonk10()