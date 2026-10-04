b1 = ["", "", "ROSE", "ALGERNON", "CLARENCE", "VIOLET", "CECIL", "CUTHBERT"]
b2 = ["", "", "FEMALE", "MALE", "MALE", "FEMALE", "MALE", "MALE"]
b3 = [0, 0]
def fonk1():
    for index in range(2, len(b1)):
        if b2[index] == "FEMALE":
            a1 = 0
        elif b2[index] == "MALE":
            a1 = 1
        else:
            continue
        b3[index] = b3[a1]
        b3[a1] = index
def fonk2():
    for index in range(2, len(b1)):
        b4 = False
        b5 = b3[0]
        for index1 in range(2, len(b1) - index + 1):
            b6 = b5
            b5 = b3[b5]
            b7 = b3[b5]
            if b1[b5] >= b1[b7]:
                b4 = True
                b8 = b3[b6]
                b3[b6] = b3[b5]
                b3[b5] = b3[b7]
                b3[b7] = b8
                b5 = b7
        if not b4:
            break
if b9 = = "__main__":
    fonk1()
    print("Initial b3:", b3)
    fonk2()
    print("Sorted b3:", b3)
    b5 = b3[0]
    b10 = []
    while b5 != 0:
        b10.append(b1[b5])
        b5 = b3[b5]
    b5 = b3[1]
    b11 = []
    while b5 != 0:
        b11.append(b1[b5])
        b5 = b3[b5]
    print("Sorted female b1:", b10)
    print("Sorted male b1:", b11)