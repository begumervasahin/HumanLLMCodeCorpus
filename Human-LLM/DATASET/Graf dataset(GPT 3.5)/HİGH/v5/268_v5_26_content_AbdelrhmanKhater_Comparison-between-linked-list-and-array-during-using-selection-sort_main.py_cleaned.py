import time
import numpy as np
import matplotlib.pyplot as plt
from random import randrange
from Selection_Algorithm import *
from Linkedlist import Linkedlist
def fonk1(b9, b13):
    plt.figure(b1 = (13, 6))
    plt.gcf().canvas.set_window_title('Comparison')
    plt.subplot(2, 1, 1)
    plt.grid(True)
    plt.title("Comparison")
    plt.xlabel("Size of Inputs")
    plt.ylabel("Time (seconds)")
    b2 = ['r', 'b', 'c']
    b3 = ['List', 'Linked List (Swap Nodes)', 'Linked List (Swap Data)']
    for i in range(len(b9)):
        plt.plot(b13, b9[i], b2[i], b4 = b3[i])
    plt.legend()
    plt.axis([0, 1500, 0, 6])
    plt.subplot(2, 1, 2)
    plt.grid(True)
    plt.xlabel("Size of Inputs")
    plt.ylabel("Time (seconds)")
    for i in range(len(b9)):
        plt.bar(b13, b9[i], 50, b5 = b2[i], align='center', b4=b3[i])
    plt.legend()
    plt.show()
def fonk2(a1):
    return [randrange(0, 1000000) for _ in range(a1)]
def fonk3(b14):
    b6 = Linkedlist()
    for item in b14:
        b6.add(item)
    return b6
def fonk4(func, *args):
    b7 = time.time()
    func(*args)
    b8 = time.time()
    return b8 - b7
def fonk5(b12, b14, b6, b13):
    b9 = []
    for a1 in b13:
        b10 = b14[:a1]
        b11 = b6.copy()
        if b12 = = 'List':
            b9.append(fonk4(Selection_Sort_Array, b10))
        elif b12 = = 'Linked List (Swap Nodes)':
            b9.append(fonk4(Selection_Sort_Linked_List, b11))
        elif b12 = = 'Linked List (Swap Data)':
            b9.append(fonk4(selectionsort_linked, b11))
    return b9
def fonk6():
    b13 = np.logspace(1, 4, num=4, dtype=int)
    b14 = fonk2(max(b13))
    b6 = fonk3(b14)
    b9 = []
    b3 = ['List', 'Linked List (Swap Nodes)', 'Linked List (Swap Data)']
    for b12 in b3:
        b9.append(fonk5(b12, b14, b6, b13))
    fonk1(b9, b13)
def fonk7():
    a1 = 10000
    b14 = fonk2(a1)
    b6 = fonk3(b14)
    b9 = []
    b3 = ['List', 'Linked List (Swap Nodes)', 'Linked List (Swap Data)']
    for b12 in b3:
        b9.append(fonk5(b12, b14, b6, [a1])[0])
    fonk1([b9], [a1])
if b15 = = '__main__':
    fonk6()