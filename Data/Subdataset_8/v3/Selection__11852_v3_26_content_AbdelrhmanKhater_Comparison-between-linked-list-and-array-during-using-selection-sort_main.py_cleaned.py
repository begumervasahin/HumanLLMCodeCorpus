import time
import math
from random import randrange
import matplotlib.pyplot as plt
from Selection_Algorithm import Selection_Sort_Array, Selection_Sort_Linked_List, selectionsort_linked
from Linkedlist import Linkedlist
def draw_comparison_chart(t1, t2, t3, siz, max_input):
    plt.figure(figsize=(13, 6))
    plt.gcf().canvas.set_window_title('Comparison')
    plt.subplot(2, 1, 1)
    plt.grid(True)
    plt.title("Comparison")
    plt.xlabel("Size of Inputs")
    plt.ylabel("Time")
    annotate_plot('T of Linked List with Swapping Nodes', max_input, t2[2], 0.1)
    annotate_plot('T of Linked List with Swapping Data', max_input, t3[2], 0.1)
    annotate_plot('T of List', max_input, t1[2], 0.1)
    plt.plot(siz, t1, 'r', siz, t2, 'b', siz, t3, 'c')
    plt.axis([0, 1500, 0, 6])
    plt.subplot(2, 1, 2)
    plt.grid(True)
    plt.xlabel("Size of Inputs")
    plt.ylabel("Time")
    plt.bar(siz, t2, 50, color='b', align='center')
    plt.bar(siz, t3, 50, color='c', align='center')
    plt.bar(siz, t1, 50, color='r', align='center')
    plt.show()
def automatic_comparison():
    t1 = []
    t2 = []
    t3 = []
    siz = []
    arr = []
    max_input = 0
    linked_list = Linkedlist()
    i = 10
    while i < 10000:
        siz.append(i)
        for j in range(0, i):
            x = randrange(0, 1000000)
            arr.append(x)
            linked_list.add(x)
            max_input = i
        s = time.time()
        Selection_Sort_Array(arr)
        e = time.time()
        t1.append(e - s)
        s = time.time()
        Selection_Sort_Linked_List(linked_list)
        e = time.time()
        t2.append(e - s)
        s = time.time()
        selectionsort_linked(linked_list)
        e = time.time()
        t3.append(e - s)
        i *= 10
    draw_comparison_chart(t1, t2, t3, siz, max_input)
def help_manual_comparison(linked_list, arr, siz):
    linked_list1 = Linkedlist()
    s = time.time()
    Selection_Sort_Array(arr)
    e = time.time()
    time_array = float(e - s)
    s = time.time()
    Selection_Sort_Linked_List(linked_list)
    e = time.time()
    time_linked_list_node = float(e - s)
    s = time.time()
    selectionsort_linked(linked_list)
    e = time.time()
    time_linked_list_data = float(e - s)
    time_array *= 1000000000
    time_linked_list_node *= 1000000000
    time_linked_list_data *= 1000000000
    print(time_array)
    print(time_linked_list_node)
    print(time_linked_list_data)
    plt.figure(figsize=(13, 6))
    plt.title(s="Comparison")
    plt.grid(True)
    plt.xlabel("Size of Inputs")
    plt.ylabel("Time in Milliseconds")
    plt.axis([0, math.ceil(siz * 1.1), 0, math.ceil(time_linked_list_node * 1.1)])
    annotate_plot('T of Linked List with Swapping Nodes', siz, time_linked_list_node, 0.1)
    annotate_plot('T of Linked List with Swapping Data', siz, time_linked_list_data, 0.1)
    annotate_plot('T of List', siz, time_array, 0.1)
    plt.bar(siz, time_array, math.ceil(0.05 * siz), color='b', align='center')
    plt.bar(siz, time_linked_list_node, math.ceil(0.05 * siz), color='c', align='center')
    plt.bar(siz, time_linked_list_data, math.ceil(0.05 * siz), color='r', align='center')
    plt.show()
def annotate_plot(label, x, y, shift):
    plt.annotate(label, xy=(x, y), xytext=(math.ceil(x * (1 + shift)), y + 0.5),
                 arrowprops=dict(facecolor='blue', shrink=0.05))
if __name__ == "__main__":
    automatic_comparison()