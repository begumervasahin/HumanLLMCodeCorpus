import random
import ABR
import RB
import sys
import pickle
sys.setrecursionlimit(4400)
def fonk1():
    b1 = pickle.load(open("tests.p", "rb"))
    b2 = fonk2(b1)
    b3 = fonk3(b1)
    pickle.dump(b2, open("result_height_abr.p", "wb"))
    pickle.dump(b3, open("result_height_rb.p", "wb"))
def fonk2(b1):
    b4 = b1[0]
    b5 = b1[1]
    b6 = []
    print("\n" + "=" * 100)
    print("Average b8 of Binary Search Trees for random b4. 3 executions.")
    print("Columns: ranges [20, 200, 1000, 10000000].")
    print("Lines: b4 [10, 50, 500, 1000, 10000, 50000]")
    print("=" * 100 + "\n")
    for p in b4:
        b7 = []
        for i in b5:
            b8 = []
            for _ in range(3):
                b9 = ABR.BinarySearchTree()
                for _ in range(p):
                    b9.insert(random.randint(0, i))
                b10 = b9.get_height(b9.root)
                b8.append(b10)
            b11 = sum(b8) / len(b8)
            b7.append(b11)
        b6.append(b7)
        print(b7)
    return b6
def fonk3(b1):
    b4 = b1[0]
    b5 = b1[1]
    b12 = []
    b13 = []
    print("\n" + "=" * 100)
    print("Average b8 of Red-Black Trees for random b4. 10 executions.")
    print("Columns: ranges [20, 200, 1000, 10000000].")
    print("Lines: b4 [10, 50, 500, 1000, 10000, 50000]")
    print("=" * 100 + "\n")
    for p in b4:
        b14 = []
        b15 = []
        for i in b5:
            b14 = []
            for _ in range(10):
                b16 = RB.RedBlackTree()
                for _ in range(p):
                    b16.insert(random.randint(0, i))
                b17 = b16.get_height(b16.root)
                b14.append(b17)
            b18 = sum(b14) / len(b14)
            b12.append(b18)
        print(b12)
    print("\n" + "=" * 100)
    print("Average b8 of Red-Black Trees for ordered b4. 5 executions.")
    print("Columns: ranges [20, 200, 1000, 10000000].")
    print("Lines: b4 [10, 50, 500, 1000, 10000, 50000]")
    print("=" * 100 + "\n")
    for p in b4:
        for _ in range(len(b5)):
            b15 = []
            for _ in range(5):
                b16 = RB.RedBlackTree()
                for k in range(p):
                    b16.insert(k)
                b17 = b16.get_height(b16.root)
                b15.append(b17)
            b19 = sum(b15) / len(b15)
            b13.append(b19)
        print(b13)
    return b12, b13
if b20 = = "__main__":
    fonk1()