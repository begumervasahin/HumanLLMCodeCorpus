import numpy as np
import operator
def fonk1():
    a1 = 1
    a2 = 2
    b1 = a1 + a2
    print("Result of basic operations example:", b1)
def fonk2():
    a2 = np.array([6, 7, 8])
    b1 = a2.shape[0]
    print("Shape of numpy array:", b1)
def fonk3():
    a1 = np.sum([[0, 1, 2], [2, 1, 3]])
    print("Sum of elements in array:", a1)
def fonk4():
    a1 = np.sum([[0, 1, 2], [2, 1, 3]], axis=0)
    print("Sum of elements along axis 0:", a1)
def fonk5():
    a1 = np.sum([[8, 1, 2], [2, 1, 3], [0, 0, 0]], axis=1)
    print("Sum of elements along axis 1:", a1)
def fonk6():
    a1 = np.array([5, 3, 1, 2, 4])
    b2 = np.argsort(a1)
    print("Indices that would sort the array:", b2)
def fonk7():
    b3 = {"A": 6, "B": 1, "C": 0, "D": 2}
    b4 = sorted(b3.items(), key=operator.itemgetter(1), reverse=True)
    print("Sorted dictionary by values:", b4)
def fonk8():
    b5 = np.array([[5, 8], [1, 2]])
    b6 = b5.flatten()
    print("Flattened array to vector:", b6)
def fonk9():
    b6 = np.array([[1, 2, 3, 4]])
    print("Accessing elements in a1 numpy array:", b6[0, 1])
fonk1()
fonk2()
fonk3()
fonk4()
fonk5()
fonk6()
fonk7()
fonk8()
fonk9()