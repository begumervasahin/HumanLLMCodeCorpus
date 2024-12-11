import time
from random import randrange
import matplotlib.pyplot as plt
from Selection_Algorithm import *
from Linkedlist import Linkedlist
import math
def fonk1(b4, b5, b6,  b7, max_input):
    plt.figure(b1 = (13, 6))
    plt.gcf().canvas.set_window_title('Comparison')
    plt.subplot(2, 1, 1)
    plt.grid(True)
    plt.title("Comparison")
    plt.xlabel("size of inputs")
    plt.ylabel("time")
    plt.annotate('T of Linked List with swapping nodes', b2 = (max_input, b5[2]), xytext=(math.ceil(max_input + 0.1 * max_input), b5[2] + 0.5), arrowprops=dict(facecolor='blue', shrink=0.05))
    plt.annotate('T of Linked List with swapping data', b2 = (max_input, b6[2]), xytext=(math.ceil(max_input + 0.1 * max_input), b6[2] + 0.5), arrowprops=dict(facecolor='cyan', shrink=0.05))
    plt.annotate('T of List', b2 = (max_input, b4[2]), xytext=(math.ceil(max_input + 0.1 * max_input), b4[2] + 0.5), arrowprops=dict(facecolor='red', shrink=0.05))
    plt.plot(b7, b4, 'r', b7, b5, 'b', b7, b6, 'c')
    plt.axis([0, 1500, 0, 6])
    plt.subplot(2, 1, 2)
    plt.grid(True)
    plt.xlabel("size of inputs")
    plt.ylabel("time")
    plt.bar(b7, b5, 50, b3 = 'b', align='center')
    plt.bar(b7, b6, 50, b3 = 'c', align='center')
    plt.bar(b7, b4, 50, b3 = 'r', align='center')
    plt.show()
def fonk2():
    b4 = []
    b5 = []
    b6 = []
    b7 = []
    b8 = []
    a1 = 0
    b9 = Linkedlist()
    a2 = 10
    while a2 < 10000:
        b7.append(a2)
        for j in range(0, a2):
            b10 = randrange(0, 1000000)
            b8.append(b10)
            b9.add(b10)
            a1 = a2
        b11 = time.time()
        Selection_Sort_Array(b8)
        b12 = time.time()
        b4.append(b12 - b11)
        b11 = time.time()
        Selection_Sort_Linked_List(b9)
        b12 = time.time()
        b5.append(b12 - b11)
        b11 = time.time()
        selectionsort_linked(b9)
        b12 = time.time()
        b6.append(b12 - b11)
        a2 *= 10
    fonk1(b4, b5, b6, b7, a1)
def fonk3(b9, b8, b7):
    b13 = Linkedlist()
    b11 = time.time()
    Selection_Sort_Array(b8)
    b12 = time.time()
    b14 = float(b12 - b11)
    b11 = time.time()
    Selection_Sort_Linked_List(b9)
    b12 = time.time()
    b15 = float(b12 - b11)
    b11 = time.time()
    selectionsort_linked(b9)
    b12 = time.time()
    b16 = float(b12 - b11)
    b14 *= 1000000000
    b15 *= 1000000000
    b16 *= 1000000000
    print(b14)
    print(b15)
    print(b16)
    plt.figure(b1 = (13, 6))
    plt.title(b11 = "Comparison")
    plt.grid(True)
    plt.xlabel("size of inputs")
    plt.ylabel("time in milliseconds")
    plt.axis([0, math.ceil(b7 * 1.1), 0, math.ceil(b15 * 1.1)])
    plt.annotate('T of Linked List with swapping nodes', b2 = (b7, b15), xytext=(math.ceil(b7 * 1.1), b15 + 0.5), arrowprops=dict(facecolor='blue', shrink=0.05))
    plt.annotate('T of Linked List with swapping data', b2 = (b7, b16), xytext=(math.ceil(b7 * 1.1), b16 + 0.5), arrowprops=dict(facecolor='cyan', shrink=0.05))
    plt.annotate('T of List', b2 = (b7, b14), xytext=(math.ceil(1.1 * b7), b14 + 0.5), arrowprops=dict(facecolor='red', shrink=0.05))
    plt.bar(b7, b14, math.ceil(0.05 * b7), b3 = 'b', align='center')
    plt.bar(b7, b15, math.ceil(0.05 * b7), b3 = 'c', align='center')
    plt.bar(b7, b16, math.ceil(0.05 * b7), b3 = 'r', align='center')
    plt.show()