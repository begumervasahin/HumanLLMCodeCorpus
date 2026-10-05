
b1 = ["", "", "ROSE", "ALGERNON", "CLARENCE", "VIOLET", "CECIL", "CUTHBERT"]
b2 = ["", "", "FEMALE", "MALE", "MALE", "FEMALE", "MALE", "MALE"]
b3 = [0, 0]
def fonk1():
    for index in range(2, len(b1)):
        b4 = 0 if b2[index] == "FEMALE" else 1
        b3[index] = b3[b4]
        b3[b4] = index
def fonk2():
    for index in range(2, len(b1)):
        b5 = False
        b6 = b3[0]
        for index1 in range(2, len(b1) - index):
            b7 = b6
            b6 = b3[b6]
            b8 = b3[b6]
            if b1[b6] >= b1[b8]:
                b5 = True
                b9 = b3[b7]
                b3[b7] = b3[b6]
                b3[b6] = b3[b8]
                b3[b8] = b9
                b6 = b8
        if not b5:
            return
fonk1()
fonk2()
b10 = [b1[index] for index in b3 if index != 0]
print("Sorted b1:", b10)