import datetime
b1 = {}
def fonk1(b3):
    b2 = datetime.datetime.now()
    if b3 = = 1:
        a1 = 1
    elif b3 = = 2:
        a1 = 1
    elif b3 > 2:
        if b3 in b1:
            a1 = b1[b3]
        else:
            a1 = fonk1(b3 - 1) + fonk1(b3 - 2)
            b1[b3] = a1
    return a1
def fonk2():
    b3 = int(input("Enter the number of Fibonacci terms: "))
    for i in range(1, b3 + 1):
        print(i, ":", fonk1(i))
    b4 = datetime.datetime.now()
    b5 = b4 - b4
    print("Execution time:", b5)
if b6 = = "__main__":
    fonk2()