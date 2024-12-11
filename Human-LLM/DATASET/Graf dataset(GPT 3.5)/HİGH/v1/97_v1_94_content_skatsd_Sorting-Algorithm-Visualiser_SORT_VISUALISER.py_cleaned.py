import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
def fonk1(arr, index_1, index_2):
    if index_1 != index_2:
        arr[index_1], arr[index_2] = arr[index_2], arr[index_1]
def fonk2(b10):
    if len(b10) == 1:
        return
    b1 = True
    for b21 in range(len(b10) - 1):
        if not b1:
            break
        b1 = False
        for b2 in range(len(b10) - 1 - b21):
            if b10[b2] > b10[b2 + 1]:
                fonk1(b10, b2, b2 + 1)
                b1 = True
            yield b10
def fonk3(b10):
    for b21 in range(1, len(b10)):
        b2 = b21
        while b2 > 0 and b10[b2] < b10[b2 - 1]:
            fonk1(b10, b2, b2 - 1)
            b2 -= 1
            yield b10
def fonk4(b10, start, b6, end):
    b3 = []
    b4 = start
    b5 = b6 + 1
    while b4 <= b6 and b5 <= end:
        if b10[b4] < b10[b5]:
            b3.append(b10[b4])
            b4 += 1
        else:
            b3.append(b10[b5])
            b5 += 1
    while b4 <= b6:
        b3.append(b10[b4])
        b4 += 1
    while b5 <= end:
        b3.append(b10[b5])
        b5 += 1
    for b21, sorted_val in enumerate(b3):
        b10[start + b21] = sorted_val
        yield b10
def fonk5(b10, start, end):
    if end <= start:
        return
    b6 = start + ((end - start + 1)
    yield from fonk5(b10, start, b6)
    yield from fonk5(b10, b6 + 1, end)
    yield from fonk4(b10, start, b6, end)
    yield b10
def fonk6(b10, start, end):
    if start >= end:
        return
    b7 = b10[end]
    b8 = start
    for b21 in range(start, end):
        if b10[b21] < b7:
            fonk1(b10, b21, b8)
            b8 += 1
        yield b10
    fonk1(b10, end, b8)
    yield b10
    yield from fonk6(b10, start, b8 - 1)
    yield from fonk6(b10, b8 + 1, end)
b9 = int(input("Enter number of integers you want to sort: "))
b10 = [x + 1 for x in range(b9)]
random.seed(time.time())
random.shuffle(b10)
b11 = int(input("Enter speed of sorting (1/Fast, 2/Medium, 3/Slow, 4/Manual): "))
if b11 = = 1:
    b11 = 10
elif b11 = = 2:
    b11 = 100
elif b11 = = 3:
    b11 = 500
elif b11 = = 4:
    b11 = int(input("Enter speed (1-1000 milliseconds): "))
    if b11 < 0:
        print("Speed cannot be negative")
        exit()
else:
    print("Invalid choice")
    exit()
b12 = "Enter sorting method:\n\
                   1/Bubble Sort\n\
                   2/Insertion Sort\n\
                   3/Merge Sort\n\
                   4/Quick Sort\n\
                   Choice:"
b13 = input(b12)
if b13 = = "1":
    b14 = "Bubble sort"
    b15 = fonk2(b10.copy())
elif b13 = = "2":
    b14 = "Insertion sort"
    b15 = fonk3(b10.copy())
elif b13 = = "3":
    b14 = "Merge sort"
    b15 = fonk5(b10.copy(), 0, b9 - 1)
elif b13 = = "4":
    b14 = "Quicksort"
    b15 = fonk6(b10.copy(), 0, b9 - 1)
else:
    print("Please select 1, 2, 3, or 4 next time")
    exit()
fig, b16 = plt.subplots()
b16.set_title(b14)
b17 = b16.bar(range(len(b10)), b10, align="edge")
b16.set_xlim(0, b9)
b16.set_ylim(0, int(1.07 * b9))
b18 = b16.text(0.02, 0.95, "", transform=b16.transAxes)
b19 = b16.text(0.02, 0.91, "", transform=b16.transAxes)
b20 = b16.text(0.02, 0.87, f"Interval duration: {b11} ms", transform=b16.transAxes)
b21 = [0]
b22 = time.time()
def fonk7(b10, rects, b21):
    for rect, val in zip(rects, b10):
        rect.set_height(val)
    b21[0] += 1
    b18.set_text(f"No. of operations: {b21[0]}")
    b23 = (time.time() - b22)
    b23 = float("{0:.2f}".format(b23))
    b23 = str(b23)
    b19.set_text(f"Time taken: {b23} sec")
b24 = animation.FuncAnimation(fig, func=update_fig,
    b25 = (b17, b21), frames=b15, b20=b11,
    b26 = False)
plt.show()