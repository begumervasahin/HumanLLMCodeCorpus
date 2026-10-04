import time
a1 = 0
def fonk1(b8):
    global a1
    if len(b8) > 1:
        b1 = len(b8)
        b2 = b8[:b1]
        b3 = b8[b1:]
        fonk1(b2)
        fonk1(b3)
        b4 = j = k = 0
        while b4 < len(b2) and j < len(b3):
            a1 += 1
            if b2[b4] < b3[j]:
                b8[k] = b2[b4]
                b4 += 1
            else:
                b8[k] = b3[j]
                j += 1
            k += 1
        while b4 < len(b2):
            a1 += 1
            b8[k] = b2[b4]
            b4 += 1
            k += 1
        while j < len(b3):
            a1 += 1
            b8[k] = b3[j]
            j += 1
            k += 1
def fonk2(b8):
    for b4 in range(len(b8)):
        print(b8[b4], b5 = " ")
    print()
if b6 = = '__main__':
    b7 = time.time()
    with open("case") as fp:
        b8 = fp.read().split()
    b9 = [int(num) for num in b8]
    fonk1(b9)
    print("Sorted array is: ", b5 = "\n")
    fonk2(b9)
    print("Number of comparisons:", a1)
    b5 = time.time()
    print("Time taken:", b5 - b7)