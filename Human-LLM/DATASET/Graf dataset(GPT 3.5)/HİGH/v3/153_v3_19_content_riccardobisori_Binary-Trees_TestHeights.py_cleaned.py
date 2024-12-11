import random
import ABR
import RB
import sys
import pickle
sys.setrecursionlimit(4400)
def fonk1():
    b1 = fonk2()
    b2 = fonk3(b1)
    b3 = fonk5(b1)
    fonk8(b2, "result_height_abr.p")
    fonk8(b3, "result_height_rb.p")
def fonk2():
    return pickle.load(open("tests.p", "rb"))
def fonk3(b1):
    elements, b4 = b1
    fonk7("Average b7 of Binary Search Trees for random elements. 3 executions.")
    b5 = []
    for p in elements:
        b6 = []
        for b17 in b4:
            b7 = []
            for _ in range(3):
                b8 = fonk4(p, b17)
                b7.append(b8)
            b9 = sum(b7) / len(b7)
            b6.append(b9)
        b5.append(b6)
        print(b6)
    return b5
def fonk4(p, b17):
    b10 = ABR.BinarySearchTree()
    for _ in range(p):
        b10.insert(random.randint(0, b17))
    return b10.get_height(b10.root)
def fonk5(b1):
    elements, b4 = b1
    fonk7("Average b7 of Red-Black Trees for random elements. 10 executions.")
    b11 = []
    b12 = []
    for p in elements:
        b13 = []
        b14 = []
        for b17 in b4:
            b13 = []
            for _ in range(10):
                b8 = fonk6(p, b17)
                b13.append(b8)
            b15 = sum(b13) / len(b13)
            b11.append(b15)
        print(b11)
    fonk7("Average b7 of Red-Black Trees for ordered elements. 5 executions.")
    for p in elements:
        for _ in range(len(b4)):
            b14 = []
            for _ in range(5):
                b8 = fonk6(p)
                b14.append(b8)
            b16 = sum(b14) / len(b14)
            b12.append(b16)
        print(b12)
    return b11, b12
def fonk6(p, b17 = None):
    b18 = RB.RedBlackTree()
    if b17:
        for _ in range(p):
            b18.insert(random.randint(0, b17))
    else:
        for k in range(p):
            b18.insert(k)
    return b18.get_height(b18.root)
def fonk7(header_text):
    print("\n" + "=" * 100)
    print(header_text)
    print("Columns: ranges [20, 200, 1000, 10000000].")
    print("Lines: elements [10, 50, 500, 1000, 10000, 50000]")
    print("=" * 100 + "\n")
def fonk8(results, file_name):
    pickle.dump(results, open(file_name, "wb"))
if b19 = = "__main__":
    fonk1()