import time
a1 = 0
a2 = 0
def fonk1(b9):
    global a1, a2
    a1 = 0
    a2 = 0
    b1 = time.time()
    b2 = fonk2(b9)
    b3 = time.time()
    print(f"QUICK SORT\nComparisons: {a1}\nSwaps: {a2}")
    print(f"Time elapsed: {b3 - b1:.4f} seconds\n")
    return b2
def fonk2(array):
    global a1, a2
    if len(array) <= 1:
        return array
    b4 = array[len(array) - 1]
    b5 = [x for x in array if x < b4]
    b6 = [x for x in array if x == b4]
    b7 = [x for x in array if x > b4]
    a1 += len(array) - 1
    a2 += 1
    return fonk2(b5) + b6 + fonk2(b7)
if b8 = = "__main__":
    b9 = [4, 10, 3, 5, 1]
    b10 = fonk1(b9)
    print(f"Sorted array: {b10}")