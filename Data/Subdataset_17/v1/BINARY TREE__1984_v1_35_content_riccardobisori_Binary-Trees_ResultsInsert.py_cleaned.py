
import pickle
import time
from random import randint
from BinarySearchTree import BinarySearchTree
from RedBlackTree import RedBlackTree
def testInsert():
    testValues = pickle.load(open("testInsert.p", "rb"))
    elements, rangeElements = testValues
    bst_times = []
    for elem in elements:
        bst = BinarySearchTree(randint(0, rangeElements[0]))
        start_time = time.time()
        for _ in range(elem):
            bst.insert(randint(0, rangeElements[0]))
        end_time = time.time()
        bst_times.append(end_time - start_time)
    rbt_times = []
    for elem in elements:
        rbt = RedBlackTree(randint(0, rangeElements[0]))
        start_time = time.time()
        for _ in range(elem):
            rbt.insert(randint(0, rangeElements[0]))
        end_time = time.time()
        rbt_times.append(end_time - start_time)
    pickle.dump((elements, bst_times), open("resultInsertABR.p", "wb"))
    pickle.dump((elements, rbt_times), open("resultInsertRB.p", "wb"))
import pickle
import TestInsert
import matplotlib.pyplot as mp
elements = (10, 50, 1000, 10000, 50000)
rangeElements = (30, 1500, 1000000000)
testValues = (elements, rangeElements)
pickle.dump(testValues, open("testInsert.p", "wb"))
TestInsert.testInsert()
resultInsertABR = pickle.load(open("resultInsertABR.p", "rb"))
resultInsertRB = pickle.load(open("resultInsertRB.p", "rb"))
x = elements
mp.plot(x, resultInsertABR[1])
mp.xlabel('Number of Elements')
mp.ylabel('Insertion Time (seconds)')
mp.title("Insertion Times in a Binary Search Tree\n with elements previously inserted in ascending order")
mp.show()
x = elements
mp.plot(x, resultInsertRB[1])
mp.xlabel('Number of Elements')
mp.ylabel('Insertion Time (seconds)')
mp.title("Insertion Times in a Red-Black Tree\n with elements previously inserted in ascending order")
mp.show()