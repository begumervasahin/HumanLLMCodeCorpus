import pickle
import TestInsert
import matplotlib.pyplot as plt
b1 = (10, 50, 1000, 10000, 50000)
b2 = (30, 1500, 1000000000)
b3 = (b1, b2)
with open("testInsert.p", "wb") as f:
    pickle.dump(b3, f)
TestInsert.testInsert()
b4 = pickle.load(open("b4.p", "rb"))
b5 = pickle.load(open("b5.p", "rb"))
b6 = (30, 100, 500, 1000)
plt.plot(b6, b4[1])
plt.xlabel('Range of b1')
plt.ylabel('Insertion time of (max(range) + 1)')
plt.title("Insertion times in a Binary Search Tree with b1 previously inserted in ascending order")
plt.show()
b6 = (30, 100, 500, 1000, 1500)
plt.plot(b6, b5[1])
plt.xlabel('Range of b1')
plt.ylabel('Insertion time of (max(range) + 1)')
plt.title("Insertion times in a Red-Black Tree with b1 previously inserted in ascending order")
plt.show()