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
    b7 = []
    b8 = []
    print "\n", "=" * 100
    print "Average heights of Binary Search Trees for random b4. 3 executions. "
    print "Columns: ranges [20, 200, 1000, 10000000]. "
    print "Lines: b4 [10, 50, 500, 1000, 10000, 50000]"
    print "=" * 100, "\n"
    for p in b4:
        for i in b5:
            for j in range(3):
                b9 = ABR.BinarySearchTree()
                for k in range(p):
                    b9.insert(random.randint(0, i))
                b10 = b9.getHeight(b9.root)
                b6.append(b10)
            b8.append(sum(b6)/len(b6))
            b6 = []
        b7.append(b8)
        print b8
        b8 = []
    return b7
def fonk3(b1):
    b4 = b1[0]
    b5 = b1[1]
    b11 = []
    b12 = []
    b13 = []
    b14 = []
    print "\n", "=" * 100
    print "Average heights of Red-Black Trees for random b4. 10 executions. "
    print "Columns: ranges [20, 200, 1000, 10000000]. "
    print "Lines: b4 [10, 50, 500, 1000, 10000, 50000]"
    print "=" * 100, "\n"
    for p in b4:
        for i in b5:
            for j in range(10):
                b15 = RB.RedBlackTree()
                for k in range(p):
                    b15.insert(random.randint(0, i))
                b16 = b15.getHeight(b15.root)
                b11.append(b16)
            b14.append(sum(b11)/len(b11))
            b11 = []
        b12.append(b14)
        print b14
        b14 = []
    print
    print "\n", "=" * 100
    print "Average heights of Red-Black Trees for ordered b4. 5 executions. "
    print "Columns: ranges [20, 200, 1000, 10000000]. "
    print "Lines: b4 [10, 50, 500, 1000, 10000, 50000]"
    print "=" * 100, "\n"
    for p in b4:
        for i in range(len(b5)):
            for j in range(5):
                b15 = RB.RedBlackTree()
                for k in range(p):
                    b15.insert(k)
                b16 = b15.getHeight(b15.root)
                b11.append(b16)
            b14.append(sum(b11)/len(b11))
            b11 = []
        b13.append(b14)
        print b14
        b14 = []
    return b12, b13