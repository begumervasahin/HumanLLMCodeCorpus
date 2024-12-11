import pickle
import TestInsert
import matplotlib.pyplot as plt
def fonk1(filename, b3):
    with open(filename, "wb") as file:
        pickle.dump(b3, file)
def fonk2(filename):
    with open(filename, "rb") as file:
        return pickle.load(file)
def fonk3(x_values, y_values, title):
    plt.plot(x_values, y_values)
    plt.xlabel('Range of b1')
    plt.ylabel('Time to insert (max(range) + 1)')
    plt.title(title)
    plt.show()
b1 = (10, 50, 1000, 10000, 50000)
b2 = (30, 1500, 1000000000)
b3 = (b1, b2)
fonk1("test_insert.p", b3)
TestInsert.test_insert()
b4 = fonk2("b4.p")
b5 = fonk2("b5.p")
b6 = (30, 100, 500, 1000)
fonk3(b6, b4[1], "Insertion times in a Binary Search Tree\n with b1 previously inserted in ascending order")
b7 = (30, 100, 500, 1000, 1500)
fonk3(b7, b5[1], "Insertion times in a Red-Black Tree\n with b1 previously inserted in ascending order")