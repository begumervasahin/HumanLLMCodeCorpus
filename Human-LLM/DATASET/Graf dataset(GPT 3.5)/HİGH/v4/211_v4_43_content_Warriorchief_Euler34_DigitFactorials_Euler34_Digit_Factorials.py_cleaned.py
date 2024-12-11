
def fonk1(x):
    a1 = 1
    for a2 in range(1, x + 1):
        a1 *= a2
    return a1
def fonk2(num):
    return list(str(num))
def fonk3(num):
    b1 = fonk2(num)
    b2 = sum(fonk1(int(char)) for char in b1)
    return b2 = = num
def fonk4(max_num):
    b3 = []
    a2 = 3
    while a2 < max_num:
        if a2 % b4 = = 0:
            print("Trying a2 as", a2, "so there's another hundred thousand tested")
        if fonk3(a2):
            b3.append(a2)
        a2 += 1
    print("Special numbers:", b3)
    print("Count:", len(b3))
    return b3
if b5 = = "__main__":
    a3 = 100000000
    fonk4(a3)