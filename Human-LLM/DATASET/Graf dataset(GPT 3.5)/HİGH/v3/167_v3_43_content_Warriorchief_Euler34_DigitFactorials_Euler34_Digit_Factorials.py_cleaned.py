def fonk1(x):
    a1 = 1
    for i in range(1, x + 1):
        a1 *= i
    return a1
def fonk2(num):
    return list(str(num))
def fonk3(num):
    b1 = fonk2(num)
    b2 = sum(fonk1(int(digit)) for digit in b1)
    return b2 = = num
def fonk4(max_num):
    b3 = []
    for i in range(3, max_num):
        if i % b4 = = 0:
            print("Testing another hundred thousand at", i)
        if fonk3(i):
            b3.append(i)
    print("Special numbers found:", b3)
    print("Total count:", len(b3))
    return b3
if b5 = = "__main__":
    a2 = 100000000
    fonk4(a2)