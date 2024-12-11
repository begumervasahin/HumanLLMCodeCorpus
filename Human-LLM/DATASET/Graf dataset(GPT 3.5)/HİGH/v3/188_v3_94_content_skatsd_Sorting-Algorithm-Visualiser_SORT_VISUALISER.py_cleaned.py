from random import shuffle, seed
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
def fonk1(arr, index_1, index_2):
    arr[index_1], arr[index_2] = arr[index_2], arr[index_1]
def fonk2(b6):
    if len(b6) == 1:
        yield b6
        return
    b1 = True
    for b15 in range(len(b6) - 1):
        if not b1:
            break
        b1 = False
        for b2 in range(len(b6) - 1 - b15):
            if b6[b2] > b6[b2 + 1]:
                fonk1(b6, b2, b2 + 1)
                b1 = True
            yield b6
def fonk3(b6):
    for b15 in range(1, len(b6)):
        b2 = b15
        while b2 > 0 and b6[b2] < b6[b2 - 1]:
            fonk1(b6, b2, b2 - 1)
            b2 -= 1
            yield b6
def fonk4():
    b3 = int(input("Enter speed of sorting (1/Fast, 2/Medium, 3/Slow, 4/Manual): "))
    if b3 = = 1:
        return 10
    elif b3 = = 2:
        return 100
    elif b3 = = 3:
        return 500
    elif b3 = = 4:
        return int(input("Enter speed (1-1000 milliseconds): "))
    else:
        print("Invalid choice")
        exit()
def fonk5():
    b4 = input("Enter sorting method (1/Bubble Sort, 2/Insertion Sort, 3/Merge Sort, 4/Quick Sort): ")
    if b4 = = "1":
        return "Bubble Sort", bubblesort_generator
    elif b4 = = "2":
        return "Insertion Sort", insertionsort_generator
def fonk6():
    seed(time.time())
    b5 = int(input("Enter number of integers you want to sort: "))
    b6 = [x + 1 for x in range(b5)]
    shuffle(b6)
    b7 = fonk4()
    title, b8 = fonk5()
    b9 = b8(b6.copy())
    fig, b10 = plt.subplots()
    b10.set_title(title)
    b11 = b10.bar(range(len(b6)), b6, align="edge")
    b10.set_xlim(0, b5)
    b10.set_ylim(0, int(1.07 * b5))
    b12 = b10.text(0.02, 0.95, "", transform=b10.transAxes)
    b13 = b10.text(0.02, 0.91, "", transform=b10.transAxes)
    b14 = b10.text(0.02, 0.87, f"Interval duration: {b7} ms", transform=b10.transAxes)
    b15 = [0]
    b16 = time.time()
    def fonk7(b6, rects, b15):
        for rect, val in zip(rects, b6):
            rect.set_height(val)
        b15[0] += 1
        b12.set_text(f"No. of operations: {b15[0]}")
        b17 = (time.time() - b16)
        b17 = float("{0:.2f}".format(b17))
        b17 = str(b17)
        b13.set_text(f"Time taken: {b17} sec")
    b18 = animation.FuncAnimation(fig, func=update_fig,
        b19 = (b11, b15), frames=b9, b14=b7,
        b20 = False)
    plt.show()
if b21 = = "__main__":
    fonk6()