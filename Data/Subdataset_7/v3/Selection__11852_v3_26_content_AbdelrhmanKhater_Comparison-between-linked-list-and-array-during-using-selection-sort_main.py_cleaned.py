import time
import math
from random import randrange
import matplotlib.pyplot as plt
from Selection_Algorithm import Selection_Sort_Array, Selection_Sort_Linked_List, selectionsort_linked
from Linkedlist import Linkedlist
def fonk1(b3, b4, b5, b6, a1):
    plt.figure(b1 = (13, 6))
    plt.gcf().canvas.set_window_title('Comparison')
    plt.subplot(2, 1, 1)
    plt.grid(True)
    plt.title("Comparison")
    plt.xlabel("Size of Inputs")
    plt.ylabel("Time")
    fonk4('T of Linked List with Swapping Nodes', a1, b4[2], 0.1)
    fonk4('T of Linked List with Swapping Data', a1, b5[2], 0.1)
    fonk4('T of List', a1, b3[2], 0.1)
    plt.plot(b6, b3, 'r', b6, b4, 'b', b6, b5, 'c')
    plt.axis([0, 1500, 0, 6])
    plt.subplot(2, 1, 2)
    plt.grid(True)
    plt.xlabel("Size of Inputs")
    plt.ylabel("Time")
    plt.bar(b6, b4, 50, b2 = 'b', align='center')
    plt.bar(b6, b5, 50, b2 = 'c', align='center')
    plt.bar(b6, b3, 50, b2 = 'r', align='center')
    plt.show()
def fonk2():
    b3 = []
    b4 = []
    b5 = []
    b6 = []
    b7 = []
    a1 = 0
    b8 = Linkedlist()
    a2 = 10
    while a2 < 10000:
        b6.append(a2)
        for j in range(0, a2):
            b9 = randrange(0, 1000000)
            b7.append(b9)
            b8.add(b9)
            a1 = a2
        b10 = time.time()
        Selection_Sort_Array(b7)
        b11 = time.time()
        b3.append(b11 - b10)
        b10 = time.time()
        Selection_Sort_Linked_List(b8)
        b11 = time.time()
        b4.append(b11 - b10)
        b10 = time.time()
        selectionsort_linked(b8)
        b11 = time.time()
        b5.append(b11 - b10)
        a2 *= 10
    fonk1(b3, b4, b5, b6, a1)
def fonk3(b8, b7, b6):
    b12 = Linkedlist()
    b10 = time.time()
    Selection_Sort_Array(b7)
    b11 = time.time()
    b13 = float(b11 - b10)
    b10 = time.time()
    Selection_Sort_Linked_List(b8)
    b11 = time.time()
    b14 = float(b11 - b10)
    b10 = time.time()
    selectionsort_linked(b8)
    b11 = time.time()
    b15 = float(b11 - b10)
    b13 *= 1000000000
    b14 *= 1000000000
    b15 *= 1000000000
    print(b13)
    print(b14)
    print(b15)
    plt.figure(b1 = (13, 6))
    plt.title(b10 = "Comparison")
    plt.grid(True)
    plt.xlabel("Size of Inputs")
    plt.ylabel("Time in Milliseconds")
    plt.axis([0, math.ceil(b6 * 1.1), 0, math.ceil(b14 * 1.1)])
    fonk4('T of Linked List with Swapping Nodes', b6, b14, 0.1)
    fonk4('T of Linked List with Swapping Data', b6, b15, 0.1)
    fonk4('T of List', b6, b13, 0.1)
    plt.bar(b6, b13, math.ceil(0.05 * b6), b2 = 'b', align='center')
    plt.bar(b6, b14, math.ceil(0.05 * b6), b2 = 'c', align='center')
    plt.bar(b6, b15, math.ceil(0.05 * b6), b2 = 'r', align='center')
    plt.show()
def fonk4(label, b9, y, shift):
    plt.annotate(label, b16 = (b9, y), xytext=(math.ceil(b9 * (1 + shift)), y + 0.5),
                 b17 = dict(facecolor='blue', shrink=0.05))
if b18 = = "__main__":
    fonk2()