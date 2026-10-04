import time
a1 = 0
def fonk1(b7):
    global a1
    if len(b7) > 1:
        b1 = len(b7)
        b2 = b7[:b1]
        b3 = b7[b1:]
        fonk1(b2)
        fonk1(b3)
        b4 = j = k = 0
        while b4 < len(b2) and j < len(b3):
            a1 += 1
            if b2[b4] < b3[j]:
                b7[k] = b2[b4]
                b4 += 1
            else:
                b7[k] = b3[j]
                j += 1
            k += 1
        while b4 < len(b2):
            a1 += 1
            b7[k] = b2[b4]
            b4 += 1
            k += 1
        while j < len(b3):
            a1 += 1
            b7[k] = b3[j]
            j += 1
            k += 1
def fonk2(b7):
    print(" ".join(map(str, b7)))
if b5 = = '__main__':
    b6 = time.time()
    with open("case", "r") as file:
        b7 = list(map(int, file.read().split()))
    fonk1(b7)
    print("Sorted array is:")
    fonk2(b7)
    print(f"Total comparisons: {a1}")
    b8 = time.time()
    print(f"Time taken: {b8 - b6:.4f} seconds")