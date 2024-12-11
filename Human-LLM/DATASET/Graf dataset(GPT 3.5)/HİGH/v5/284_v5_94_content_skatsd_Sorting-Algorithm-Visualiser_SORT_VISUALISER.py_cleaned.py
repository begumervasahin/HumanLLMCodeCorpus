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
    for b24 in range(len(b10) - 1):
        if not b1:
            break
        b1 = False
        for b2 in range(len(b10) - 1 - b24):
            if b10[b2] > b10[b2 + 1]:
                fonk1(b10, b2, b2 + 1)
                b1 = True
            yield b10
def fonk3(b10):
    for b24 in range(1, len(b10)):
        b2 = b24
        while b2 > 0 and b10[b2] < b10[b2 - 1]:
            fonk1(b10, b2, b2 - 1)
            b2 -= 1
            yield b10
def fonk4(b10, start, end):
    if end <= start:
        return
    b3 = start + ((end - start + 1)
    yield from fonk4(b10, start, b3)
    yield from fonk4(b10, b3 + 1, end)
    yield from fonk5(b10, start, b3, end)
    yield b10
def fonk5(b10, start, b3, end):
    b4 = []
    b5 = start
    b6 = b3 + 1
    while b5 <= b3 and b6 <= end:
        if b10[b5] < b10[b6]:
            b4.append(b10[b5])
            b5 += 1
        else:
            b4.append(b10[b6])
            b6 += 1
    while b5 <= b3:
        b4.append(b10[b5])
        b5 += 1
    while b6 <= end:
        b4.append(b10[b6])
        b6 += 1
    for b24, sorted_val in enumerate(b4):
        b10[start + b24] = sorted_val
        yield b10
def fonk6(b10, start, end):
    if start >= end:
        return
    b7 = b10[end]
    b8 = start
    for b24 in range(start, end):
        if b10[b24] < b7:
            fonk1(b10, b24, b8)
            b8 += 1
        yield b10
    fonk1(b10, end, b8)
    yield b10
    yield from fonk6(b10, start, b8 - 1)
    yield from fonk6(b10, b8 + 1, end)
b9 = int(input("Enter number of integers you want to sort:\n"))
b10 = [x + 1 for x in range(b9)]
random.seed(time.time())
random.shuffle(b10)
b11 = {
    '1': 10,
    '2': 100,
    '3': 500
}
b12 = input("Enter b12 of sorting:\n"\
              "1/Fast\n"\
              "2/Medium\n"\
              "3/Slow\n"\
              "CHOICE: ")
if b12 in b11:
    b13 = b11[b12]
elif b12 = = '4':
    b13 = int(input("Enter any value from 1 to 1000 in millisec\n"\
                            "(1 being fastest, 1000 being slowest)\n"\
                            "SPEED: "))
    if b13 < 0:
        print("Speed cannot be negative")
        exit()
else:
    print("INVALID CHOICE")
    exit()
b14 = {
    '1': bubblesort,
    '2': insertionsort,
    '3': merge_sort,
    '4': quicksort
}
b15 = input("Enter sorting method:\n"\
                         "1/Bubble Sort\n"\
                         "2/Insertion Sort\n"\
                         "3/Merge Sort\n"\
                         "4/Quick Sort\n"\
                         "CHOICE: ")
if b15 in b14:
    b16 = b14[b15]
    b17 = b16.__name__.replace('_', ' ').b17()
    b18 = b16(b10, 0, b9 - 1)
else:
    print("PLEASE SELECT 1, 2, 3 NEXT TIME")
    exit()
fig, b19 = plt.subplots()
b19.set_title(b17)
b20 = b19.bar(range(len(b10)), b10, align="edge")
b19.set_xlim(0, b9)
b19.set_ylim(0, int(1.07 * b9))
b21 = b19.text(0.02, 0.95, "", transform=b19.transAxes)
b22 = b19.text(0.02, 0.91, "", transform=b19.transAxes)
b23 = b19.text(0.02, 0.87, "Interval duration: " + str(b13) + "ms", transform=b19.transAxes)
b24 = [0]
b25 = time.time()
def fonk7(b10, rects, b24):
    for rect, val in zip(rects, b10):
        rect.set_height(val)
    b24[0] += 1
    b21.set_text("No. of operations: " + str(b24[0]))
    b26 = (time.time() - b25)
    b26 = float("{0:.2f}".format(b26))
    b26 = str(b26)
    b22.set_text("Time taken: " + b26 + " sec")
b27 = animation.FuncAnimation(fig, func=update_fig,
                               b28 = (b20, b24), frames=b18, b23=b13,
                               b29 = False)
plt.show()