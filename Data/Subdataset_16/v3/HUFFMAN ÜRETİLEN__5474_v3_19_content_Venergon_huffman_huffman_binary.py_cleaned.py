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
def fonk9(node, b11):
    b3 = node.fonk8()
    b4, b5 = node.b4, node.b5
    b4.fonk7(b3 + "0")
    b5.fonk7(b3 + "1")
    if isinstance(b4, class2):
        fonk9(b4, b11)
    else:
        b11.append(b4)
    if isinstance(b5, class2):
        fonk9(b5, b11)
    else:
        b11.append(b5)
def fonk10(b8):
    while len(b8) > 1:
        b8.sort(b6 = lambda x: x.b2)
        b4 = b8.pop(0)
        b5 = b8.pop(0)
        b7 = class2(b4, b5)
        b8.append(b7)
    return b8[0]
def fonk11():
    b8 = []
    while True:
        b9 = input("Enter node (or leave blank to stop): ")
        if not b9:
            break
        try:
            b1, b2 = b9.split(",")
            b8.append(class1(b1, float(b2)))
        except ValueError:
            print("Invalid input. Please use the format 'value,b2'.")
            continue
    if not b8:
        print("No b8 entered. Exiting.")
        return
    b10 = fonk10(b8)
    b11 = []
    b10.fonk7("")
    if isinstance(b10, class1):
        b11.append(b10)
    else:
        fonk9(b10, b11)
    b11.sort(b6 = lambda x: x.b1)
    print("\nHuffman Codes:")
    for node in b11:
        print(f"class1 {node} has b3 {node.fonk8()}")
if b12 = = "__main__":
    fonk11()