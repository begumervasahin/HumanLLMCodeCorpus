import pickle
import TestInsert
import matplotlib.pyplot as plt
b1 = (10, 50, 1000, 10000, 50000)
b2 = (30, 1500, 1000000000)
b3 = (b1, b2)
with open("testInsert.p", "wb") as file:
    pickle.dump(b3, file)
TestInsert.testInsert()
with open("resultInsertABR.p", "rb") as file:
    b4 = pickle.load(file)
with open("resultInsertRB.p", "rb") as file:
    b5 = pickle.load(file)
b6 = (30, 100, 500, 1000)
plt.plot(b6, b4[1])
plt.xlabel('Range of Elements')
plt.ylabel('Insertion Time of (max(range) + 1)')
plt.title("Insertion Times in a Binary Search Tree\n with Elements Previously Inserted in Ascending Order")
plt.show()
b6 = (30, 100, 500, 1000, 1500)
plt.plot(b6, b5[1])
plt.xlabel('Range of Elements')
plt.ylabel('Insertion Time of (max(range) + 1)')
plt.title("Insertion Times in a Red-Black Tree\n with Elements Previously Inserted in Ascending Order")
plt.show()