import pickle
import TestInsert
import matplotlib.pyplot as plt
elements = (10, 50, 1000, 10000, 50000)
rangeElements = (30, 1500, 1000000000)
testValues = (elements, rangeElements)
with open("testInsert.p", "wb") as f:
    pickle.dump(testValues, f)
TestInsert.testInsert()
resultInsertABR = pickle.load(open("resultInsertABR.p", "rb"))
resultInsertRB = pickle.load(open("resultInsertRB.p", "rb"))
x = (30, 100, 500, 1000)
plt.plot(x, resultInsertABR[1])
plt.xlabel('Range of elements')
plt.ylabel('Insertion time of (max(range) + 1)')
plt.title("Insertion times in a Binary Search Tree with elements previously inserted in ascending order")
plt.show()
x = (30, 100, 500, 1000, 1500)
plt.plot(x, resultInsertRB[1])
plt.xlabel('Range of elements')
plt.ylabel('Insertion time of (max(range) + 1)')
plt.title("Insertion times in a Red-Black Tree with elements previously inserted in ascending order")
plt.show()