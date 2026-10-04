import time
a1 = 0
def fonk1(b6):
    global a1
    if len(b6) > 1:
        b1 = len(b6)
        b2 = b6[:b1]
        b3 = b6[b1:]
        fonk1(b2)
        fonk1(b3)
        b4 = j = k = 0
        while b4 < len(b2) and j < len(b3):
            a1 += 1
            if b2[b4] < b3[j]:
                b6[k] = b2[b4]
                b4 += 1
            else:
                b6[k] = b3[j]
                j += 1
            k += 1
        while b4 < len(b2):
            a1 += 1
            b6[k] = b2[b4]
            b4 += 1
            k += 1
        while j < len(b3):
            a1 += 1
            b6[k] = b3[j]
            j += 1
            k += 1
def fonk2(b6):
    print(" ".join(map(str, b6)))
def fonk3():
    b5 = time.time()
    with open("case", "r") as file:
        b6 = file.read().split()
    b7 = [int(num) for num in b6]
    fonk1(b7)
    print("Sorted array is:")
    fonk2(b7)
    print(f"Number of comparisons: {a1}")
    b8 = time.time()
    print(f"Time taken: {b8 - b5:.6f} seconds")
if b9 = = "__main__":
    fonk3()