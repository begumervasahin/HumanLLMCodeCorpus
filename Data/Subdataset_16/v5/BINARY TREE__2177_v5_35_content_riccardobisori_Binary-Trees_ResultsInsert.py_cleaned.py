import pickle
import TestInsert
import matplotlib.pyplot as plt
def fonk1(filename, values):
    with open(filename, "wb") as file:
        pickle.dump(values, file)
def fonk2(filename):
    with open(filename, "rb") as file:
        return pickle.load(file)
def fonk3(x, y, xlabel, ylabel, title):
    plt.plot(x, y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()
b1 = (10, 50, 1000, 10000, 50000)
b2 = (30, 1500, 1000000000)
b3 = (b1, b2)
fonk1("testInsert.p", b3)
TestInsert.testInsert()
b4 = fonk2("resultInsertABR.p")
b5 = fonk2("resultInsertRB.p")
b6 = (30, 100, 500, 1000)
fonk3(
    b6,
    b4[1],
    'Range of Elements',
    'Insertion Time of (max(range) + 1)',
    "Insertion Times in a Binary Search Tree\n with Elements Previously Inserted in Ascending Order"
)
b7 = (30, 100, 500, 1000, 1500)
fonk3(
    b7,
    b5[1],
    'Range of Elements',
    'Insertion Time of (max(range) + 1)',
    "Insertion Times in a Red-Black Tree\n with Elements Previously Inserted in Ascending Order"
)