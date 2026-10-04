b1 = ["", "", "ROSE", "ALGERNON", "CLARENCE", "VIOLET", "CECIL", "CUTHBERT"]
b2 = ["", "", "FEMALE", "MALE", "MALE", "FEMALE", "MALE", "MALE"]
b3 = [0, 0] + [0] * (len(b1) - 2)
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
    for i in range(2, len(b1)):
        b4 = False
        b5 = b3[0]
        for j in range(2, len(b1) - i + 1):
            b6 = b5
            b5 = b3[b5]
            b7 = b3[b5]
            if b1[b5] >= b1[b7]:
                b4 = True
                b3[b6], b3[b5], b3[b7] = b3[b5], b3[b7], b3[b6]
                b5 = b7
        if not b4:
            break
if b8 = = "__main__":
    fonk1()
    print("Initial b3:", b3)
    fonk2()
    print("Sorted b3:", b3)
    def fonk3(queue_index):
        b9 = []
        b5 = b3[queue_index]
        while b5 != 0:
            b9.append(b1[b5])
            b5 = b3[b5]
        return b9
    b10 = fonk3(0)
    b11 = fonk3(1)
    print("Sorted female b1:", b10)
    print("Sorted male b1:", b11)