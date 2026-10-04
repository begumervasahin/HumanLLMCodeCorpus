b1 = ["", "", "ROSE", "ALGERNON", "CLARENCE", "VIOLET", "CECIL", "CUTHBERT"]
b2 = ["", "", "FEMALE", "MALE", "MALE", "FEMALE", "MALE", "MALE"]
b3 = [0] * len(b1)
def fonk1():
    b3[0] = 0
    b3[1] = 0
    for index in range(2, len(b1)):
        if b2[index] == "FEMALE":
            a1 = 0
        else:
            a1 = 1
        b3[index] = b3[a1]
        b3[a1] = index
def fonk2(queue_start):
    for _ in range(2, len(b1)):
        b4 = False
        b5 = b3[queue_start]
        while b5 != 0 and b3[b5] != 0:
            b6 = b3[b5]
            if b1[b5] > b1[b6]:
                b3[b5], b3[b6] = b3[b6], b3[b5]
                b4 = True
            b5 = b3[b5]
        if not b4:
            break
def fonk3():
    print("Sorted Females:")
    b5 = b3[0]
    while b5 != 0:
        print(b1[b5])
        b5 = b3[b5]
    print("\nSorted Males:")
    b5 = b3[1]
    while b5 != 0:
        print(b1[b5])
        b5 = b3[b5]
def fonk4():
    fonk1()
    fonk2(0)
    fonk2(1)
    fonk3()
if b7 = = "__main__":
    fonk4()