import random
b1 = "\x1B[31m"
b2 = "\x1B[32m"
b3 = "\x1B[0m"
def fonk1():
    fonk2()
    b4 = fonk3()
    fonk5(b4)
def fonk2():
    print("------------------")
    print("| codedrome.com  |")
    print("| Selection Sort |")
    print("------------------\n")
def fonk3():
    b4 = []
    for _ in range(16):
        b4.append(random.randint(1, 99))
    return b4
def fonk4(b4, a1):
    for i, num in enumerate(b4):
        if i < a1:
            print(b2 + "%-3d " % num + b3, b5 = "")
        else:
            print(b1 + "%-3d " % num + b3, b5 = "")
    print("\n")
def fonk5(b4):
    print("Unsorted...")
    fonk4(b4, 0)
    print("Selection Sorting...")
    a1 = 0
    while a1 < len(b4) - 1:
        b6 = fonk7(b4, a1)
        fonk6(b4, a1, b6)
        a1 += 1
        fonk4(b4, a1)
    print("Sorted!")
def fonk6(b4, i1, i2):
    if i1 != i2:
        b4[i1], b4[i2] = b4[i2], b4[i1]
def fonk7(b4, start):
    b7 = start
    for i in range(start, len(b4)):
        if b4[i] < b4[b7]:
            b7 = i
    return b7
if b8 = = "__main__":
    fonk1()