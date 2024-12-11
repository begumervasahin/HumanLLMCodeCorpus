import time
a1 = 0
a2 = 0
def fonk1(arr):
    b1 = time.time()
    fonk2(arr)
    b2 = time.time()
    print("QUICK SORT")
    print("Comparisons:", a1)
    print("Swaps:", a2)
    print("Time elapsed:", b2 - b1, "\n")
def fonk2(array):
    global a1, a2
    b3 = []
    b4 = []
    b5 = []
    if len(array) > 1:
        b6 = array[-1]
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
        return fonk2(b3) + b4 + fonk2(b5)
    else:
        return array