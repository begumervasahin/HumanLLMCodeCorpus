import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
def fonk1(arr, index_1, index_2):
    if index_1 != index_2:
        arr[index_1], arr[index_2] = arr[index_2], arr[index_1]
def fonk2(b8):
    if len(b8) == 1:
        return
    b1 = True
    for b19 in range(len(b8) - 1):
        if not b1:
            break
        b1 = False
        for b2 in range(len(b8) - 1 - b19):
            if b8[b2] > b8[b2 + 1]:
                fonk1(b8, b2, b2 + 1)
                b1 = True
            yield b8
def fonk3(b8):
    for b19 in range(1, len(b8)):
        b2 = b19
        while b2 > 0 and b8[b2] < b8[b2 - 1]:
            fonk1(b8, b2, b2 - 1)
            b2 -= 1
            yield b8
def fonk4(left, right):
    b3 = []
    a1 = 0
    a2 = 0
    while a1 < len(left) and a2 < len(right):
        if left[a1] < right[a2]:
            b3.append(left[a1])
            a1 += 1
        else:
            b3.append(right[a2])
            a2 += 1
    b3.extend(left[a1:])
    b3.extend(right[a2:])
    return b3
def fonk5(b8, start, end):
    if end <= start:
        return
    b4 = start + ((end - start + 1)
    yield from fonk5(b8, start, b4)
    yield from fonk5(b8, b4 + 1, end)
    yield from fonk4(b8[start:b4 + 1], b8[b4 + 1:end + 1])
def fonk6(b8, start, end):
    if start >= end:
        return
    b5 = b8[end]
    b6 = start
    for b19 in range(start, end):
        if b8[b19] < b5:
            fonk1(b8, b19, b6)
            b6 += 1
        yield b8
    fonk1(b8, end, b6)
    yield b8
    yield from fonk6(b8, start, b6 - 1)
    yield from fonk6(b8, b6 + 1, end)
b7 = int(input("Enter number of integers you want to sort: "))
b8 = [x + 1 for x in range(b7)]
random.seed(time.time())
random.shuffle(b8)
b9 = int(input("Enter speed of sorting (1/Fast, 2/Medium, 3/Slow, 4/Manual): "))
if b9 = = 1:
    b9 = 10
elif b9 = = 2:
    b9 = 100
elif b9 = = 3:
    b9 = 500
elif b9 = = 4:
    b9 = int(input("Enter speed (1-1000 milliseconds): "))
    if b9 < 0:
        print("Speed cannot be negative")
        exit()
else:
    print("Invalid choice")
    exit()
b10 = "Enter sorting method:\n\
                   1/Bubble Sort\n\
                   2/Insertion Sort\n\
                   3/Merge Sort\n\
                   4/Quick Sort\n\
                   Choice:"
b11 = input(b10)
if b11 = = "1":
    b12 = "Bubble sort"
    b13 = fonk2(b8.copy())
elif b11 = = "2":
    b12 = "Insertion sort"
    b13 = fonk3(b8.copy())
elif b11 = = "3":
    b12 = "Merge sort"
    b13 = fonk5(b8.copy(), 0, b7 - 1)
elif b11 = = "4":
    b12 = "Quicksort"
    b13 = fonk6(b8.copy(), 0, b7 - 1)
else:
    print("Please select 1, 2, 3, or 4 next time")
    exit()
fig, b14 = plt.subplots()
b14.set_title(b12)
b15 = b14.bar(range(len(b8)), b8, align="edge")
b14.set_xlim(0, b7)
b14.set_ylim(0, int(1.07 * b7))
b16 = b14.text(0.02, 0.95, "", transform=b14.transAxes)
b17 = b14.text(0.02, 0.91, "", transform=b14.transAxes)
b18 = b14.text(0.02, 0.87, f"Interval duration: {b9} ms", transform=b14.transAxes)
b19 = [0]
b20 = time.time()
def fonk7(b8, rects, b19):
    for rect, val in zip(rects, b8):
        rect.set_height(val)
    b19[0] += 1
    b16.set_text(f"No. of operations: {b19[0]}")
    b21 = (time.time() - b20)
    b21 = float("{0:.2f}".format(b21))
    b21 = str(b21)
    b17.set_text(f"Time taken: {b21} sec")
b22 = animation.FuncAnimation(fig, func=update_fig,
    b23 = (b15, b19), frames=b13, b18=b9,
    b24 = False)
plt.show()