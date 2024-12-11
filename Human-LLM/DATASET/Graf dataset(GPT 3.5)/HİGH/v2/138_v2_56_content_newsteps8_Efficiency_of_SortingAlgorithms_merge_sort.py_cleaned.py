import time
def fonk1(b8):
    if len(b8) > 1:
        b1 = len(b8)
        b2 = b8[:b1]
        b3 = b8[b1:]
        fonk1(b2)
        fonk1(b3)
        b4 = j = k = 0
        while b4 < len(b2) and j < len(b3):
            if b2[b4] < b3[j]:
                b8[k] = b2[b4]
                b4 += 1
            else:
                b8[k] = b3[j]
                j += 1
            k += 1
        while b4 < len(b2):
            b8[k] = b2[b4]
            b4 += 1
            k += 1
        while j < len(b3):
            b8[k] = b3[j]
            j += 1
            k += 1
def fonk2(b8):
    for num in b8:
        print(num, b5 = " ")
    print()
if b6 = = '__main__':
    b7 = time.time()
    a1 = 0
    with open("case", "r") as fp:
        b8 = fp.read().split()
        b9 = [int(x) for x in b8]
    fonk1(b9)
    print("Sorted array:")
    fonk2(b9)
    print("Total comparisons:", a1)
    b10 = time.time()
    print("Execution time:", b10 - b7)