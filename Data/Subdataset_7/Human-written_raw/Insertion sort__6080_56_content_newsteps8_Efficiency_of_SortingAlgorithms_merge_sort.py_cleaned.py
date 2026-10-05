import time
b1 = time.time()
a1 = 0
def fonk1(b9):
    global a1
    if len(b9) > 1:
        b2 = len(b9)
        b3 = b9[:b2]
        b4 = b9[b2:]
        fonk1(b3)
        fonk1(b4)
        b5 = j = k = 0
        while b5 < len(b3) and j < len(b4):
            a1 = a1 + 1
            if b3[b5] < b4[j]:
                b9[k] = b3[b5]
                b5 += 1
            else:
                b9[k] = b4[j]
                j += 1
            k += 1
        while b5 < len(b3):
            a1 = a1 + 1
            b9[k] = b3[b5]
            b5 += 1
            k += 1
        while j < len(b4):
            a1 = a1 + 1
            b9[k] = b4[j]
            j += 1
            k += 1
def fonk2(b9):
    for b5 in range(len(b9)):
        print(b9[b5], b6 = " ")
    print()
if b7 = = '__main__':
    b8 = open("case")
    b9 = b8.read().split(" ")
    b8.close()
    b10 = []
    for b5 in range(len(b9)):
        b11 = int(b9[b5])
        b10.append(b11)
    fonk1(b10)
    print("Sorted array is: ", b6 = "\n")
    fonk2(b10)
    print(a1)
b6 = time.time()
print(b6 - b1)