class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
def fonk2():
    b4 = int(input("Enter node value (-1 for no node): "))
    if b4 = = -1:
        return None
    b5 = class1(b4)
    b5.b2 = fonk2()
    b5.b3 = fonk2()
    return b5
def fonk3(b5):
    if b5 is None:
        return
    print(f"{b5.b1}:", b6 = "")
    if b5.b2:
        print(f"{b5.b2.b1},", b6 = "")
    else:
        print("-1,", b6 = "")
    if b5.b3:
        print(f"{b5.b3.b1}")
    else:
        print("-1")
    fonk3(b5.b2)
    fonk3(b5.b3)
def fonk4(b5):
    if b5 is None:
        return 0
    b7 = fonk4(b5.b2)
    b8 = fonk4(b5.b3)
    return 1 + b7 + b8
def fonk5(b5):
    if b5 is None:
        return
    print(b5.b1, b6 = " ")
    fonk5(b5.b2)
    fonk5(b5.b3)
def fonk6(b5):
    if b5 is None:
        return
    fonk6(b5.b2)
    print(b5.b1, b6 = " ")
    fonk6(b5.b3)
def fonk7(b5):
    if b5 is None:
        return
    fonk7(b5.b2)
    fonk7(b5.b3)
    print(b5.b1, b6 = " ")
def fonk8(b5):
    if b5 is None:
        return 0
    b9 = fonk8(b5.b2)
    b10 = fonk8(b5.b3)
    return max(b9, b10) + 1
def fonk9(b5, b11):
    if b5 is None:
        return
    if b11 = = 0:
        print(b5.b1, b6 = " ")
        return
    fonk9(b5.b2, b11 - 1)
    fonk9(b5.b3, b11 - 1)
def fonk10(b5, depth):
    if b5 is None:
        return
    b5.b1 = depth
    fonk10(b5.b2, depth + 1)
    fonk10(b5.b3, depth + 1)
def fonk11(b5):
    if b5 is None:
        return None
    if b5.b2 is None and b5.b3 is None:
        return None
    b5.b2 = fonk11(b5.b2)
    b5.b3 = fonk11(b5.b3)
    return b5
def fonk12(b5):
    if b5 is None:
        return
    b5.b2, b5.b3 = b5.b3, b5.b2
    fonk12(b5.b2)
    fonk12(b5.b3)
    return b5
import queue
class class2:
    def fonk13(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
def fonk14():
    b4 = int(input("Enter b5 node value: "))
    if b4 = = -1:
        return None
    b5 = class2(b4)
    b12 = queue.Queue()
    b12.put(b5)
    while not b12.empty():
        b13 = b12.get()
        b14 = int(input(f"Enter b2 child of {b13.b1}: "))
        if b14 != -1:
            b15 = class2(b14)
            b13.b2 = b15
            b12.put(b15)
        b16 = int(input(f"Enter b3 child of {b13.b1}: "))
        if b16 != -1:
            b17 = class2(b16)
            b13.b3 = b17
            b12.put(b17)
    return b5
def fonk15(b5):
    if b5 is None:
        return
    b12 = queue.Queue()
    b12.put(b5)
    while not b12.empty():
        b13 = b12.get()
        print(f"{b13.b1}:", b6 = "")
        if b13.b2:
            print(f"{b13.b2.b1},", b6 = "")
            b12.put(b13.b2)
        else:
            print("-1,", b6 = "")
        if b13.b3:
            print(f"{b13.b3.b1}")
            b12.put(b13.b3)
        else:
            print("-1")
def fonk16(b25, b26):
    if not b25:
        return None
    b4 = b25.pop()
    b5 = class2(b4)
    b18 = b26.b18(b4)
    b19 = b26[:b18]
    b20 = b26[b18 + 1:]
    b21 = b25[:len(b19)]
    b22 = b25[len(b19):]
    b5.b2 = fonk16(b21, b19)
    b5.b3 = fonk16(b22, b20)
    return b5
if b23 = = "__main__":
    b5 = fonk2()
    fonk3(b5)
    print(f"Total nodes: {fonk4(b5)}")
    print("Preorder traversal:")
    fonk5(b5)
    print("\nInorder traversal:")
    fonk6(b5)
    print("\nPostorder traversal:")
    fonk7(b5)
    print(f"\nTree height: {fonk8(b5)}")
    b11 = int(input("Enter depth b11: "))
    print(f"Nodes at depth {b11}:")
    fonk9(b5, b11)
    print()
    fonk10(b5, 0)
    print("Tree after replacing nodes with their depth:")
    fonk3(b5)
    b5 = fonk11(b5)
    print("Tree after removing leaves:")
    fonk3(b5)
    b5 = fonk12(b5)
    print("Mirrored tree:")
    fonk3(b5)
    b24 = fonk14()
    fonk15(b24)
    b25 = [4, 5, 2, 6, 7, 3, 1]
    b26 = [4, 2, 5, 1, 6, 3, 7]
    b27 = fonk16(b25, b26)
    fonk15(b27)