import time
def fonk1(b7):
    if len(b7) <= 1:
        return
    b1 = len(b7)
    b2 = b7[:b1]
    b3 = b7[b1:]
    fonk1(b2)
    fonk1(b3)
    fonk2(b7, b2, b3)
def fonk2(b7, b2, b3):
    b4 = j = k = 0
    while b4 < len(b2) and j < len(b3):
        if b2[b4] <= b3[j]:
            b7[k] = b2[b4]
            b4 += 1
        else:
            b7[k] = b3[j]
            j += 1
        k += 1
    while b4 < len(b2):
        b7[k] = b2[b4]
        b4 += 1
        k += 1
    while j < len(b3):
        b7[k] = b3[j]
        j += 1
        k += 1
def fonk3(b7):
    print(" ".join(map(str, b7)))
if b5 = = '__main__':
    b6 = time.time()
    with open("case", "r") as fp:
        b7 = list(map(int, fp.read().split()))
    fonk1(b7)
    print("Sorted array:")
    fonk3(b7)
    b8 = time.time()
    print("Execution time:", b8 - b6)