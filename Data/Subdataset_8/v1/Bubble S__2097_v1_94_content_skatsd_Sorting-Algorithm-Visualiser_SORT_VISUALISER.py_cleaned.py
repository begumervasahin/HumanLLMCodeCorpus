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
def mergesort(A, start, end):
    if end <= start:
        return
    mid = start + ((end - start + 1)
    yield from mergesort(A, start, mid)
    yield from mergesort(A, mid + 1, end)
    yield from merge(A, start, mid, end)
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
N = int(input("Enter number of integers you want to sort: "))
A = [x + 1 for x in range(N)]
random.seed(time.time())
random.shuffle(A)
speedofSort = int(input("Enter speed of sorting (1/Fast, 2/Medium, 3/Slow, 4/Manual): "))
if speedofSort == 1:
    speedofSort = 10
elif speedofSort == 2:
    speedofSort = 100
elif speedofSort == 3:
    speedofSort = 500
elif speedofSort == 4:
    speedofSort = int(input("Enter speed (1-1000 milliseconds): "))
    if speedofSort < 0:
        print("Speed cannot be negative")
        exit()
else:
    print("Invalid choice")
    exit()
sortChooser_msg = "Enter sorting method:\n\
                   1/Bubble Sort\n\
                   2/Insertion Sort\n\
                   3/Merge Sort\n\
                   4/Quick Sort\n\
                   Choice:"
sortingSelection = input(sortChooser_msg)
if sortingSelection == "1":
    title = "Bubble sort"
    generator = bubblesort(A.copy())
elif sortingSelection == "2":
    title = "Insertion sort"
    generator = insertionsort(A.copy())
elif sortingSelection == "3":
    title = "Merge sort"
    generator = mergesort(A.copy(), 0, N - 1)
elif sortingSelection == "4":
    title = "Quicksort"
    generator = quicksort(A.copy(), 0, N - 1)
else:
    print("Please select 1, 2, 3, or 4 next time")
    exit()
fig, ax = plt.subplots()
ax.set_title(title)
bar_rects = ax.bar(range(len(A)), A, align="edge")
ax.set_xlim(0, N)
ax.set_ylim(0, int(1.07 * N))
noOfOperations = ax.text(0.02, 0.95, "", transform=ax.transAxes)
timeTaken = ax.text(0.02, 0.91, "", transform=ax.transAxes)
interval = ax.text(0.02, 0.87, f"Interval duration: {speedofSort} ms", transform=ax.transAxes)
i = [0]
start_time = time.time()
def update_fig(A, rects, i):
    for rect, val in zip(rects, A):
        rect.set_height(val)
    i[0] += 1
    noOfOperations.set_text(f"No. of operations: {i[0]}")
    time_elapsed = (time.time() - start_time)
    time_elapsed = float("{0:.2f}".format(time_elapsed))
    time_elapsed = str(time_elapsed)
    timeTaken.set_text(f"Time taken: {time_elapsed} sec")
anim = animation.FuncAnimation(fig, func=update_fig,
    fargs=(bar_rects, i), frames=generator, interval=speedofSort,
    repeat=False)
plt.show()