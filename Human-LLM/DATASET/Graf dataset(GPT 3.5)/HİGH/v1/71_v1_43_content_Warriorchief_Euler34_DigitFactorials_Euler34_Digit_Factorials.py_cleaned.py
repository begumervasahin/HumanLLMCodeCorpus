def fonk1(x):
    a1 = 1
    for i in range(1, x + 1):
        a1 *= i
    return a1
def fonk2(num):
    return list(str(num))
def fonk3(num):
    b1 = fonk2(num)
    b2 = sum(fonk1(int(char)) for char in b1)
    return b2 = = num
def fonk4(max_num):
    b3 = []
    for i in range(3, max_num):
        if i % b4 = = 0:
            print("Trying i as", i, "so there's another hundred thousand tested")
        if fonk3(i):
            b3.append(i)
    print("Special numbers are", b3, "so there are", len(b3), "that are less than", max_num)
    return b3
if b5 = = "__main__":
    fonk4(100000000)