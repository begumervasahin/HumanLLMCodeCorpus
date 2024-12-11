import time
b1 = time.time()
a1 = 0
def fonk1(b8):
    global a1
    if len(b8) > 1:
        b2 = len(b8)
        b3 = b8[:b2]
        b4 = b8[b2:]
        fonk1(b3)
        fonk1(b4)
        b5 = j = k = 0
        while b5 < len(b3) and j < len(b4):
            a1 += 1
            if b3[b5] < b4[j]:
                b8[k] = b3[b5]
                b5 += 1
            else:
                b8[k] = b4[j]
                j += 1
            k += 1
        while b5 < len(b3):
            a1 += 1
            b8[k] = b3[b5]
            b5 += 1
            k += 1
        while j < len(b4):
            a1 += 1
            b8[k] = b4[j]
            j += 1
            k += 1
def fonk2(b8):
    for b5 in range(len(b8)):
        print(b8[b5], b6 = " ")
    print()
if b7 = = '__main__':
    with open("case", "r") as fp:
        b8 = fp.read().split(" ")
        b9 = [int(x) for x in b8]
    fonk1(b9)
    print("Sorted array is:")
    fonk2(b9)
    print("Total comparisons:", a1)
b10 = time.time()
print("Execution time:", b10 - b1)