import time
def fonk1(b9):
    a1, b1 = fonk2(b9)
    return a1, b1
def fonk2(array):
    a1 = 0
    b1 = 0
    if len(array) > 1:
        b2 = array[len(array) - 1]
        b3 = []
        b4 = []
        b5 = []
        for b6 in array:
            if b6 < b2:
                a1 += 1
                b3.append(b6)
            elif b6 = = b2:
                a1 += 1
                b4.append(b6)
            elif b6 > b2:
                a1 += 1
                b5.append(b6)
        b1 += 1
        comparisons_less, b7 = fonk2(b3)
        comparisons_greater, b8 = fonk2(b5)
        return a1 + comparisons_less + comparisons_greater, b1 + b7 + b8
    else:
        return a1, b1
b9 = [12, 11, 13, 5, 6, 7]
print("Unsorted array:", b9)
b10 = time.time()
a1, b1 = fonk1(b9)
b11 = time.time()
print("Sorted array:", b9)
print("QUICK SORT")
print("Comparisons:", a1)
print("Swaps:", b1)
print("Time elapsed:", b11 - b10)