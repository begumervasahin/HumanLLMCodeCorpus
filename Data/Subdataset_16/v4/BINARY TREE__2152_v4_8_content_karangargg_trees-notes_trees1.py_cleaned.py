class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = None
        self.b3 = None
def fonk2():
    b4 = int(input("Enter b1 (-1 for no node): "))
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
        print(f"{b5.b2.b1}", b6 = ",")
    else:
        print("-1", b6 = ",")
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
    return b7 + b8 + 1
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
    fonk9(b5.b2, b11-1)
    fonk9(b5.b3, b11-1)
def fonk10(b5, b12 = 0):
    if b5 is None:
        return
    b5.b1 = b12
    fonk10(b5.b2, b12+1)
    fonk10(b5.b3, b12+1)
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
        return None
    b5.b2, b5.b3 = b5.b3, b5.b2
    fonk12(b5.b2)
    fonk12(b5.b3)
    return b5
def fonk13():
    b4 = int(input("Enter b5 b1: "))
    if b4 = = -1 or b4 < 0:
        return None
    b5 = class1(b4)
    b13 = queue.Queue()
    b13.put(b5)
    while not b13.empty():
        b14 = b13.get()
        b15 = int(input(f"Enter b2 child of {b14.b1}: "))
        if b15 != -1:
            b16 = class1(b15)
            b14.b2 = b16
            b13.put(b16)
        b17 = int(input(f"Enter b3 child of {b14.b1}: "))
        if b17 != -1:
            b18 = class1(b17)
            b14.b3 = b18
            b13.put(b18)
    return b5
def fonk14(b5):
    if b5 is None:
        return
    b13 = queue.Queue()
    b13.put(b5)
    while not b13.empty():
        b14 = b13.get()
        print(f"{b14.b1}:", b6 = "")
        if b14.b2:
            print(f"{b14.b2.b1}", b6 = ",")
            b13.put(b14.b2)
        if b14.b3:
            print(f"{b14.b3.b1}", b6 = "")
            b13.put(b14.b3)
        print()
if b19 = = "__main__":
    import queue
    b5 = fonk2()
    fonk3(b5)
    b20 = fonk4(b5)
    print(f"Number of nodes: {b20}")
    print("Preorder traversal:")
    fonk5(b5)
    print()
    print("Inorder traversal:")
    fonk6(b5)
    print()
    print("Postorder traversal:")
    fonk7(b5)
    print()
    b21 = fonk8(b5)
    print(f"Height of the tree: {b21}")
    print("Nodes at b12 2:")
    fonk9(b5, 2)
    print()
    fonk10(b5)
    print("Tree after replacing node values with their b12:")
    fonk3(b5)
    b5 = fonk11(b5)
    print("Tree after removing leaf nodes:")
    fonk3(b5)
    b5 = fonk12(b5)
    print("Mirrored tree:")
    fonk3(b5)
    b5 = fonk13()
    print("Level-wise tree:")
    fonk14(b5)