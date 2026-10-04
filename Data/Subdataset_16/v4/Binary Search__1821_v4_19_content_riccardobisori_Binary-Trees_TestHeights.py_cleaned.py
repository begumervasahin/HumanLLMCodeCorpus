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
    pickle.dump(b2, open("resultHeightABR.p", "wb"))
    pickle.dump(b3, open("resultHeightRB.p", "wb"))
def fonk2(b1):
    b4 = b1[0]
    b5 = b1[1]
    b6 = []
    print("\n", "=" * 100)
    print("Average b8 of Binary Search Trees for random b4. 3 executions.")
    print("Columns: ranges [20, 200, 1000, 10000000].")
    print("Lines: b4 [10, 50, 500, 1000, 10000, 50000]")
    print("=" * 100, "\n")
    for num_elements in b4:
        b7 = []
        for range_limit in b5:
            b8 = []
            for _ in range(3):
                b9 = ABR.BinarySearchTree()
                for _ in range(num_elements):
                    b9.insert(random.randint(0, range_limit))
                b10 = b9.getHeight(b9.root)
                b8.append(b10)
            b7.append(sum(b8) / len(b8))
        b6.append(b7)
        print(b7)
    return b6
def fonk3(b1):
    b4 = b1[0]
    b5 = b1[1]
    b11 = []
    b12 = []
    print("\n", "=" * 100)
    print("Average b8 of Red-Black Trees for random b4. 10 executions.")
    print("Columns: ranges [20, 200, 1000, 10000000].")
    print("Lines: b4 [10, 50, 500, 1000, 10000, 50000]")
    print("=" * 100, "\n")
    for num_elements in b4:
        b7 = []
        for range_limit in b5:
            b8 = []
            for _ in range(10):
                b13 = RB.RedBlackTree()
                for _ in range(num_elements):
                    b13.insert(random.randint(0, range_limit))
                b14 = b13.getHeight(b13.root)
                b8.append(b14)
            b7.append(sum(b8) / len(b8))
        b11.append(b7)
        print(b7)
    print("\n", "=" * 100)
    print("Average b8 of Red-Black Trees for ordered b4. 5 executions.")
    print("Columns: ranges [20, 200, 1000, 10000000].")
    print("Lines: b4 [10, 50, 500, 1000, 10000, 50000]")
    print("=" * 100, "\n")
    for num_elements in b4:
        b7 = []
        for _ in range(len(b5)):
            b8 = []
            for _ in range(5):
                b13 = RB.RedBlackTree()
                for k in range(num_elements):
                    b13.insert(k)
                b14 = b13.getHeight(b13.root)
                b8.append(b14)
            b7.append(sum(b8) / len(b8))
        b12.append(b7)
        print(b7)
    return b11, b12
if b15 = = "__main__":
    fonk1()