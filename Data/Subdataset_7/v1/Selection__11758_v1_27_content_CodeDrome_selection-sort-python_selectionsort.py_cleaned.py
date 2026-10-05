import random
b1 = "\x1B[31m"
b2 = "\x1B[32m"
b3 = "\x1B[0m"
def fonk1():
    print("------------------")
    print("| codedrome.com  |")
    print("| Selection Sort |")
    print("------------------\n")
    b4 = fonk2()
    fonk4(b4)
def fonk2():
    b4 = []
    for i in range(0, 16):
        b4.append(random.randint(1, 99))
    return b4
def fonk3(b4, sortedto):
    for i in range(0, len(b4)):
        if i < sortedto:
            print(b2 + "%-3d " % b4[i] + b3, b5 = "")
        else:
            print(b1 + "%-3d " % b4[i] + b3, b5 = "")
    print("\n")
def fonk4(b4):
    print("Unsorted...")
    fonk3(b4, 0)
    print("Selection Sorting...")
    a1 = 0
    while a1 < len(b4) - 1:
        b6 = fonk6(b4, a1)
        fonk5(b4, a1, b6)
        a1 += 1
        fonk3(b4, a1)
    print("Sorted!")
def fonk5(b4, i1, i2):
    if i1 != i2:
        b4[i1] = b4[i1] ^ b4[i2]
        b4[i2] = b4[i1] ^ b4[i2]
        b4[i1] = b4[i1] ^ b4[i2]
def fonk6(b4, start):
    b7 = start
    for i in range(start, len(b4)):
        if b4[i] < b4[b7]:
            b7 = i
    return b7
if b8 = = "__main__":
    fonk1()