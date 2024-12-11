b1 = ["", "", "ROSE", "ALGERNON", "CLARENCE", "VIOLET", "CECIL", "CUTHBERT"]
b2 = ["", "", "FEMALE", "MALE", "MALE", "FEMALE", "MALE", "MALE"]
b3 = [0, 0]
def fonk1():
    for index in range(2, len(b1)):
        if b2[index] == "FEMALE":
            fonk2(0, index)
        elif b2[index] == "MALE":
            fonk2(1, index)
def fonk2(que, index):
    b3[index] = b3[que]
    b3[que] = index
def fonk3():
    for index in range(2, len(b1)):
        b4 = False
        b5 = b3[0]
        for index1 in range(2, len(b1) - index):
            b6 = b5
            b5 = b3[b5]
            b7 = b3[b5]
            if b1[b5] >= b1[b7]:
                b4 = True
                fonk4(b6, b5, b7)
                b5 = b7
        if not b4:
            return
def fonk4(b6, b5, b7):
    b8 = b3[b6]
    b3[b6] = b3[b5]
    b3[b5] = b3[b7]
    b3[b7] = b8
fonk1()
fonk3()