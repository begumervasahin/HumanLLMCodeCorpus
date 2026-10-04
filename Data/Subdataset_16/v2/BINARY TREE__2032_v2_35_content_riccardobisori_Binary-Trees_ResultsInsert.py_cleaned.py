import pickle
import time
from random import randint
from BinarySearchTree import BinarySearchTree
from RedBlackTree import RedBlackTree
def fonk1():
    b1 = pickle.load(open("testInsert.p", "rb"))
    b10, b2 = b1
    b3 = []
    for num_elements in b10:
        b4 = BinarySearchTree(randint(0, b2[0]))
        b5 = time.time()
        for _ in range(num_elements):
            b4.insert(randint(0, b2[0]))
        b6 = time.time()
        b3.append(b6 - b5)
    b7 = []
    for num_elements in b10:
        b8 = RedBlackTree(randint(0, b2[0]))
        b5 = time.time()
        for _ in range(num_elements):
            b8.insert(randint(0, b2[0]))
        b6 = time.time()
        b7.append(b6 - b5)
    with open("resultInsertABR.p", "wb") as f:
        pickle.dump((b10, b3), f)
    with open("resultInsertRB.p", "wb") as f:
        pickle.dump((b10, b7), f)
if b9 = = "__main__":
    fonk1()
import pickle
import matplotlib.pyplot as plt
def fonk2(filename):
    with open(filename, "rb") as f:
        return pickle.load(f)
def fonk3(b10, times, title, ylabel):
    plt.plot(b10, times)
    plt.xlabel('Number of Elements')
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()
def fonk4():
    b10 = (10, 50, 1000, 10000, 50000)
    b2 = (30, 1500, 1000000000)
    b1 = (b10, b2)
    with open("testInsert.p", "wb") as f:
        pickle.dump(b1, f)
    import TestInsert
    TestInsert.fonk1()
    b11 = fonk2("resultInsertABR.p")
    b12 = fonk2("resultInsertRB.p")
    fonk3(b11[0], b11[1],
                 "Insertion Times in a Binary Search Tree\nwith b10 previously inserted in ascending order",
                 "Insertion Time (seconds)")
    fonk3(b12[0], b12[1],
                 "Insertion Times in a Red-Black Tree\nwith b10 previously inserted in ascending order",
                 "Insertion Time (seconds)")
if b9 = = "__main__":
    fonk4()