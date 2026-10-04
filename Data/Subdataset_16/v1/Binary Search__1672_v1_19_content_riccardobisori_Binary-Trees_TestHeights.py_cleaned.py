import random
import ABR
import RB
import sys
import pickle
sys.setrecursionlimit(4400)
def fonk1():
    b1 = pickle.load(open("tests.p", "rb"))
    b2 = fonk2(b1)
    result_RB_random, b3 = fonk3(b1)
    pickle.dump(b2, open("resultHeightABR.p", "wb"))
    pickle.dump(result_RB_random, open("resultHeightRB_random.p", "wb"))
    pickle.dump(b3, open("resultHeightRB_ordered.p", "wb"))
def fonk2(b1):
    elements, b4 = b1
    b5 = []
    print("\n" + "=" * 100)
    print("Average b7 of Binary Search Trees for random elements. 3 executions.")
    print("Columns: ranges [20, 200, 1000, 10000000].")
    print("Lines: elements [10, 50, 500, 1000, 10000, 50000]")
    print("=" * 100 + "\n")
    for p in elements:
        b6 = []
        for i in b4:
            b7 = []
            for _ in range(3):
                b8 = ABR.BinarySearchTree()
                for _ in range(p):
                    b8.insert(random.randint(0, i))
                b9 = b8.getHeight(b8.root)
                b7.append(b9)
            b6.append(sum(b7) / len(b7))
        b5.append(b6)
        print(b6)
    return b5
def fonk3(b1):
    elements, b4 = b1
    b10 = []
    b11 = []
    print("\n" + "=" * 100)
    print("Average b7 of Red-Black Trees for random elements. 10 executions.")
    print("Columns: ranges [20, 200, 1000, 10000000].")
    print("Lines: elements [10, 50, 500, 1000, 10000, 50000]")
    print("=" * 100 + "\n")
    for p in elements:
        b12 = []
        for i in b4:
            b7 = []
            for _ in range(10):
                b13 = RB.RedBlackTree()
                for _ in range(p):
                    b13.insert(random.randint(0, i))
                b14 = b13.getHeight(b13.root)
                b7.append(b14)
            b12.append(sum(b7) / len(b7))
        b10.append(b12)
        print(b12)
    print("\n" + "=" * 100)
    print("Average b7 of Red-Black Trees for ordered elements. 5 executions.")
    print("Columns: ranges [20, 200, 1000, 10000000].")
    print("Lines: elements [10, 50, 500, 1000, 10000, 50000]")
    print("=" * 100 + "\n")
    for p in elements:
        b12 = []
        for _ in range(len(b4)):
            b7 = []
            for _ in range(5):
                b13 = RB.RedBlackTree()
                for k in range(p):
                    b13.insert(k)
                b14 = b13.getHeight(b13.root)
                b7.append(b14)
            b12.append(sum(b7) / len(b7))
        b11.append(b12)
        print(b12)
    return b10, b11
if b15 = = "__main__":
    fonk1()