
import pickle
import time
from random import randint
from BinarySearchTree import BinarySearchTree
from RedBlackTree import RedBlackTree
def fonk1():
    b1 = pickle.load(open("testInsert.p", "rb"))
    b9, b2 = b1
    b3 = []
    for elem in b9:
        b4 = BinarySearchTree(randint(0, b2[0]))
        b5 = time.time()
        for _ in range(elem):
            b4.insert(randint(0, b2[0]))
        b6 = time.time()
        b3.append(b6 - b5)
    b7 = []
    for elem in b9:
        b8 = RedBlackTree(randint(0, b2[0]))
        b5 = time.time()
        for _ in range(elem):
            b8.insert(randint(0, b2[0]))
        b6 = time.time()
        b7.append(b6 - b5)
    pickle.dump((b9, b3), open("b10.p", "wb"))
    pickle.dump((b9, b7), open("b11.p", "wb"))
import pickle
import TestInsert
import matplotlib.pyplot as mp
b9 = (10, 50, 1000, 10000, 50000)
b2 = (30, 1500, 1000000000)
b1 = (b9, b2)
pickle.dump(b1, open("testInsert.p", "wb"))
TestInsert.fonk1()
b10 = pickle.load(open("b10.p", "rb"))
b11 = pickle.load(open("b11.p", "rb"))
b12 = b9
mp.plot(b12, b10[1])
mp.xlabel('Number of Elements')
mp.ylabel('Insertion Time (seconds)')
mp.title("Insertion Times in a Binary Search Tree\n with b9 previously inserted in ascending order")
mp.show()
b12 = b9
mp.plot(b12, b11[1])
mp.xlabel('Number of Elements')
mp.ylabel('Insertion Time (seconds)')
mp.title("Insertion Times in a Red-Black Tree\n with b9 previously inserted in ascending order")
mp.show()