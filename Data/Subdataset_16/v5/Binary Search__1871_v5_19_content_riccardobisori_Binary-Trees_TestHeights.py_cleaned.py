import random
import sys
import pickle
import ABR
import RB
sys.setrecursionlimit(4400)
def fonk1():
    b13, b1 = fonk2("tests.p")
    b2 = fonk4(b13, b1)
    fonk3(b2, "resultHeightABR.p")
    b3 = fonk5(b13, b1)
    fonk3(b3, "resultHeightRB.p")
def fonk2(filename):
    with open(filename, "rb") as file:
        b4 = pickle.load(file)
    return b4
def fonk3(data, filename):
    with open(filename, "wb") as file:
        pickle.dump(data, file)
def fonk4(b13, b1):
    b5 = []
    fonk6("Binary Search Trees (ABR)", b13, b1, b6 = 3)
    for num_elements in b13:
        b7 = []
        for range_limit in b1:
            b8 = [
                fonk7(ABR.BinarySearchTree(), num_elements, range_limit)
                for _ in range(3)
            ]
            b7.append(fonk9(b8))
        b5.append(b7)
        print(b7)
    return b5
def fonk5(b13, b1):
    b9 = []
    b10 = []
    fonk6("Red-Black Trees (RB)", b13, b1, b6 = 10, b11="random")
    b9 = fonk8(RB.RedBlackTree, b13, b1, b6=10, b12=True)
    fonk6("Red-Black Trees (RB)", b13, b1, b6 = 5, b11="ordered")
    b10 = fonk8(RB.RedBlackTree, b13, b1, b6=5, b12=False)
    return b9, b10
def fonk6(tree_type, b13, b1, b6, b11 = "random"):
    """
    Print the header for the test results.
    Args:
        tree_type (str): The type of tree being tested (e.g., "Binary Search Trees").
        b13 (list): List of numbers of b13 to insert into the trees.
        b1 (list): List of range limits for generating random b13.
        b6 (int): Number of b6 performed for each test.
        b11 (str): The type of test being performed ("random" or "ordered").
    """
    print("\n", "=" * 100)
    print(f"Average b8 of {tree_type} for {b11} b13. {b6} executions.")
    print(f"Columns: b1 {b1}.")
    print(f"Lines: b13 {b13}.")
    print("=" * 100, "\n")
def fonk7(tree, num_elements, range_limit, b12 = True):
    if b12:
        b13 = (random.randint(0, range_limit) for _ in range(num_elements))
    else:
        b13 = range(num_elements)
    for element in b13:
        tree.insert(element)
    return tree.getHeight(tree.root)
def fonk8(tree_class, b13, b1, b6, b12 = True):
    b5 = []
    for num_elements in b13:
        b7 = []
        for range_limit in b1:
            b8 = [
                fonk7(tree_class(), num_elements, range_limit, b12)
                for _ in range(b6)
            ]
            b7.append(fonk9(b8))
        b5.append(b7)
        print(b7)
    return b5
def fonk9(b8):
    return sum(b8) / len(b8)
if b14 = = "__main__":
    fonk1()