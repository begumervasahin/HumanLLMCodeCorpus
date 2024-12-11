import random
import ABR
import RB
import sys
import pickle
sys.setrecursionlimit(4400)
def fonk1():
    b1 = fonk2("tests.p")
    b2 = fonk3(b1)
    b3 = fonk4(b1)
    fonk8(b2, "resultHeightABR.p")
    fonk8(b3, "resultHeightRB.p")
def fonk2(filename):
    return pickle.load(open(filename, "rb"))
def fonk3(b1):
    elements, b4 = b1
    fonk5("Binary Search Trees", "random", 3)
    b5 = []
    for p in elements:
        b6 = fonk6(p, b4, 3)
        b5.append(b6)
        print(b6)
    return b5
def fonk4(b1):
    elements, b4 = b1
    fonk5("Red-Black Trees", "random", 10)
    b7 = []
    b8 = []
    for p in elements:
        b9 = fonk7(p, b4, 10)
        b7.append(b9)
        print(b9)
    fonk5("Red-Black Trees", "b16", 5)
    for p in elements:
        b10 = fonk7(p, b4, 5, b16=True)
        b8.append(b10)
        print(b10)
    return b7, b8
def fonk5(tree_type, randomness, executions):
    print("\n" + "=" * 100)
    print(f"Average b12 of {tree_type} for {randomness} elements. {executions} executions.")
    print("Columns: ranges [20, 200, 1000, 10000000].")
    print("Lines: elements [10, 50, 500, 1000, 10000, 50000]")
    print("=" * 100 + "\n")
def fonk6(elements, b4, executions):
    b11 = []
    for i in b4:
        b12 = []
        for _ in range(executions):
            b13 = ABR.BinarySearchTree()
            for _ in range(elements):
                b13.insert(random.randint(0, i))
            b14 = b13.get_height(b13.root)
            b12.append(b14)
        b15 = sum(b12) / len(b12)
        b11.append(b15)
    return b11
def fonk7(elements, b4, executions, b16 = False):
    b17 = []
    if b16:
        fonk5("Red-Black Trees", "b16", executions)
    else:
        fonk5("Red-Black Trees", "random", executions)
    for i in b4:
        b12 = []
        for _ in range(executions):
            b18 = RB.RedBlackTree()
            for _ in range(elements):
                if b16:
                    b18.insert(_)
                else:
                    b18.insert(random.randint(0, i))
            b19 = b18.get_height(b18.root)
            b12.append(b19)
        b15 = sum(b12) / len(b12)
        b17.append(b15)
    return b17
def fonk8(results, filename):
    pickle.dump(results, open(filename, "wb"))
if b20 = = "__main__":
    fonk1()