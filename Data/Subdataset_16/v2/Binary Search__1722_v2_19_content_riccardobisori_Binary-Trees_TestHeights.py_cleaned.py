import random
import sys
import pickle
import ABR
import RB
sys.setrecursionlimit(4400)
def fonk1(filename):
    with open(filename, "rb") as f:
        return pickle.load(f)
def fonk2(filename, data):
    with open(filename, "wb") as f:
        pickle.dump(data, f)
def fonk3():
    b1 = fonk1("tests.p")
    b2 = fonk4(b1)
    rbt_random_results, b3 = fonk5(b1)
    fonk2("resultHeightABR.p", b2)
    fonk2("resultHeightRB_random.p", rbt_random_results)
    fonk2("resultHeightRB_ordered.p", b3)
def fonk4(test_params):
    elements, b4 = test_params
    b5 = []
    print("\n" + "=" * 100)
    print("Average b7 of Binary Search Trees for random elements. 3 executions per test.")
    print("Columns: ranges [20, 200, 1000, 10000000].")
    print("Rows: elements [10, 50, 500, 1000, 10000, 50000]")
    print("=" * 100 + "\n")
    for num_elements in elements:
        b6 = []
        for max_val in b4:
            b7 = []
            for _ in range(3):
                b8 = ABR.BinarySearchTree()
                for _ in range(num_elements):
                    b8.insert(random.randint(0, max_val))
                b7.append(b8.getHeight(b8.root))
            b6.append(sum(b7) / len(b7))
        b5.append(b6)
        print(b6)
    return b5
def fonk5(test_params):
    elements, b4 = test_params
    b5 = []
    b9 = []
    print("\n" + "=" * 100)
    print("Average b7 of Red-Black Trees for random elements. 10 executions per test.")
    print("Columns: ranges [20, 200, 1000, 10000000].")
    print("Rows: elements [10, 50, 500, 1000, 10000, 50000]")
    print("=" * 100 + "\n")
    for num_elements in elements:
        b6 = []
        for max_val in b4:
            b7 = []
            for _ in range(10):
                b10 = RB.RedBlackTree()
                for _ in range(num_elements):
                    b10.insert(random.randint(0, max_val))
                b7.append(b10.getHeight(b10.root))
            b6.append(sum(b7) / len(b7))
        b5.append(b6)
        print(b6)
    print("\n" + "=" * 100)
    print("Average b7 of Red-Black Trees for ordered elements. 5 executions per test.")
    print("Columns: ranges [20, 200, 1000, 10000000].")
    print("Rows: elements [10, 50, 500, 1000, 10000, 50000]")
    print("=" * 100 + "\n")
    for num_elements in elements:
        b6 = []
        for _ in range(len(b4)):
            b7 = []
            for _ in range(5):
                b10 = RB.RedBlackTree()
                for k in range(num_elements):
                    b10.insert(k)
                b7.append(b10.getHeight(b10.root))
            b6.append(sum(b7) / len(b7))
        b9.append(b6)
        print(b6)
    return b5, b9
if b11 = = "__main__":
    fonk3()