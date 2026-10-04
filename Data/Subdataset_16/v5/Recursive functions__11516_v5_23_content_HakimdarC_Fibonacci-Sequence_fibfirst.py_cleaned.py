import datetime
b1 = {}
def fonk1(b2):
    if b2 in b1:
        return b1[b2]
    if b2 = = 1 or b2 == 2:
        a1 = 1
    else:
        a1 = fonk1(b2 - 1) + fonk1(b2 - 2)
        b1[b2] = a1
    return a1
def fonk2():
    b3 = int(input("Give the number of Fibonacci terms: "))
    b4 = datetime.datetime.now()
    for i in range(1, b3 + 1):
        print(f"{i}: {fonk1(i)}")
    b5 = datetime.datetime.now()
    b6 = b5 - b4
    print(f"Elapsed time: {b6}")
if b7 = = "__main__":
    fonk2()