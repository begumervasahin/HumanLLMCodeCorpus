from random import randint
from time import time
from tkinter import *
def selection_sort(values):
    for i in range(len(values)):
        min_pos = minimum_position(values, i)
        temp = values[min_pos]
        values[min_pos] = values[i]
        values[i] = temp
def minimum_position(values, start):
    min_pos = start
    for i in range(start + 1, len(values)):
        if values[i] < values[min_pos]:
            min_pos = i
    return min_pos
def main():
    print()
    n_min = int(input("Enter the minimum list size: "))
    print()
    n_max = int(input("Enter the maximum list size: "))
    print()
    runs = int(input("Enter the number of different measurements to run: "))
    n = n_min
    table_array = []
    for i in range(runs):
        values = [randint(1, 1000) for _ in range(n)]
        start_time = time()
        selection_sort(values)
        end_time = time()
        table_array.append([n, round((end_time - start_time), 3)])
        n = int(n + ((n_max - n_min) / (runs - 1))) - int(n + ((n_max - n_min) / (runs - 1))) % 5
    window = Tk()
    window.title("Results of Sample Runs - Selection Sort")
    label_sort_size = Label(text='Sort Size')
    label_seconds_to_sort = Label(text='Seconds to Sort')
    label_sort_size.grid(row=0, column=1, sticky=NSEW)
    label_seconds_to_sort.grid(row=0, column=2, sticky=NSEW)
    for i in range(runs):
        label_n = Label(text='%.0f' % table_array[i][0], relief=RIDGE, width=20, height=2)
        label_seconds = Label(text='%.3f' % table_array[i][1], relief=RIDGE, width=20, height=2)
        label_n.grid(row=i + 1, column=1, sticky=NSEW)
        label_seconds.grid(row=i + 1, column=2, sticky=NSEW)
    window.mainloop()
if __name__ == "__main__":
    main()