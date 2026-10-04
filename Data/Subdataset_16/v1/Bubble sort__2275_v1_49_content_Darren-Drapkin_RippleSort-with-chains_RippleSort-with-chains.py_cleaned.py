b1 = ["", "", "ROSE", "ALGERNON", "CLARENCE", "VIOLET", "CECIL", "CUTHBERT"]
b2 = ["", "", "FEMALE", "MALE", "MALE", "FEMALE", "MALE", "MALE"]
b3 = [0] * len(b1)
def fonk1():
    b3[0] = 0
    b3[1] = 0
    for index in range(2, len(b1)):
        if b2[index] == "FEMALE":
            a1 = 0
            b3[index] = b3[a1]
            b3[a1] = index
        elif b2[index] == "MALE":
            a1 = 1
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
            if b1[b5] > b1[b7]:
                b4 = True
                b3[b6], b3[b5], b3[b7] = (
                    b3[b5],
                    b3[b7],
                    b3[b6],
                )
                b5 = b7
        if not b4:
            break
def fonk3():
    b5 = b3[0]
    print("Sorted Females:")
    while b5 != 0:
        print(b1[b5])
        b5 = b3[b5]
    b5 = b3[1]
    print("Sorted Males:")
    while b5 != 0:
        print(b1[b5])
        b5 = b3[b5]
def fonk4():
    fonk1()
    fonk2()
    fonk3()
if b8 = = "__main__":
    fonk4()