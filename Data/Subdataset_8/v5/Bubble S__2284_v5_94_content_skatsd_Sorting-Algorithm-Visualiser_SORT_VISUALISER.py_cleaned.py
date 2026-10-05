import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
def swap(arr, index_1, index_2):
    if index_1 != index_2:
        arr[index_1], arr[index_2] = arr[index_2], arr[index_1]
def bubblesort(A):
    if len(A) == 1:
        return
    swapped = True
    for i in range(len(A) - 1):
        if not swapped:
            break
        swapped = False
        for j in range(len(A) - 1 - i):
            if A[j] > A[j + 1]:
                swap(A, j, j + 1)
                swapped = True
            yield A
def insertionsort(A):
    for i in range(1, len(A)):
        j = i
        while j > 0 and A[j] < A[j - 1]:
            swap(A, j, j - 1)
            j -= 1
            yield A
def merge_sort(A, start, end):
    if end <= start:
        return
    mid = start + ((end - start + 1)
    yield from merge_sort(A, start, mid)
    yield from merge_sort(A, mid + 1, end)
    yield from merge(A, start, mid, end)
    yield A
def merge(A, start, mid, end):
    merged = []
    leftIdx = start
    rightIdx = mid + 1
    while leftIdx <= mid and rightIdx <= end:
        if A[leftIdx] < A[rightIdx]:
            merged.append(A[leftIdx])
            leftIdx += 1
        else:
            merged.append(A[rightIdx])
            rightIdx += 1
    while leftIdx <= mid:
        merged.append(A[leftIdx])
        leftIdx += 1
    while rightIdx <= end:
        merged.append(A[rightIdx])
        rightIdx += 1
    for i, sorted_val in enumerate(merged):
        A[start + i] = sorted_val
        yield A
def quicksort(A, start, end):
    if start >= end:
        return
    pivot = A[end]
    pivotIdx = start
    for i in range(start, end):
        if A[i] < pivot:
            swap(A, i, pivotIdx)
            pivotIdx += 1
        yield A
    swap(A, end, pivotIdx)
    yield A
    yield from quicksort(A, start, pivotIdx - 1)
    yield from quicksort(A, pivotIdx + 1, end)
N = int(input("Enter number of integers you want to sort:\n"))
A = [x + 1 for x in range(N)]
random.seed(time.time())
random.shuffle(A)
speed_options = {
    '1': 10,
    '2': 100,
    '3': 500
}
speed = input("Enter speed of sorting:\n"\
              "1/Fast\n"\
              "2/Medium\n"\
              "3/Slow\n"\
              "CHOICE: ")
if speed in speed_options:
    speedofSort = speed_options[speed]
elif speed == '4':
    speedofSort = int(input("Enter any value from 1 to 1000 in millisec\n"\
                            "(1 being fastest, 1000 being slowest)\n"\
                            "SPEED: "))
    if speedofSort < 0:
        print("Speed cannot be negative")
        exit()
else:
    print("INVALID CHOICE")
    exit()
sorting_methods = {
    '1': bubblesort,
    '2': insertionsort,
    '3': merge_sort,
    '4': quicksort
}
sortingSelection = input("Enter sorting method:\n"\
                         "1/Bubble Sort\n"\
                         "2/Insertion Sort\n"\
                         "3/Merge Sort\n"\
                         "4/Quick Sort\n"\
                         "CHOICE: ")
if sortingSelection in sorting_methods:
    sort_func = sorting_methods[sortingSelection]
    title = sort_func.__name__.replace('_', ' ').title()
    generator = sort_func(A, 0, N - 1)
else:
    print("PLEASE SELECT 1, 2, 3 NEXT TIME")
    exit()
fig, ax = plt.subplots()
ax.set_title(title)
bar_rects = ax.bar(range(len(A)), A, align="edge")
ax.set_xlim(0, N)
ax.set_ylim(0, int(1.07 * N))
noOfOperations = ax.text(0.02, 0.95, "", transform=ax.transAxes)
timeTaken = ax.text(0.02, 0.91, "", transform=ax.transAxes)
interval = ax.text(0.02, 0.87, "Interval duration: " + str(speedofSort) + "ms", transform=ax.transAxes)
i = [0]
start_time = time.time()
def update_fig(A, rects, i):
    for rect, val in zip(rects, A):
        rect.set_height(val)
    i[0] += 1
    noOfOperations.set_text("No. of operations: " + str(i[0]))
    time_elapsed = (time.time() - start_time)
    time_elapsed = float("{0:.2f}".format(time_elapsed))
    time_elapsed = str(time_elapsed)
    timeTaken.set_text("Time taken: " + time_elapsed + " sec")
anim = animation.FuncAnimation(fig, func=update_fig,
                               fargs=(bar_rects, i), frames=generator, interval=speedofSort,
                               repeat=False)
plt.show()