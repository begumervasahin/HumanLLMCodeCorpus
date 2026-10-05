import time
a1 = 0
a2 = 0
def fonk1(b8):
    b1 = time.time()
    fonk2(b8)
    b2 = time.time()
    print("QUICK SORT\nComparisons: " + str(a1) + "\nSwaps: " + str(a2))
    print("Time elapsed: ", str(b2 - b1) + "\n")
def fonk2(array):
    global a1
    global a2
    b3 = []
    b4 = []
    b5 = []
    if len(array) > 1:
        b6 = array[len(array)-1]
        for b7 in array:
            if b7 < b6:
                a1 += 1
                b3.append(b7)
            elif b7 = = b6:
                a1 += 1
                b4.append(b7)
            elif b7 > b6:
                a1 += 1
                b5.append(b7)
        a2 += 1
        return fonk2(b3)+b4+fonk2(b5)
    else:
        return array
b8 = [12, 11, 13, 5, 6, 7]
print("Unsorted array:", b8)
fonk1(b8)
print("Sorted array:", b8)