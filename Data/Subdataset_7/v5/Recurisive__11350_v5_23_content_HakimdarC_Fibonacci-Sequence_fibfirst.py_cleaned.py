import datetime
b1 = {}
def fonk1(b2):
    if b2 = = 1 or b2 == 2:
        return 1
    if b2 in b1:
        return b1[b2]
    b3 = fonk1(b2 - 1) + fonk1(b2 - 2)
    b1[b2] = b3
    return b3
def fonk2():
    b4 = int(input("Enter the number of Fibonacci terms: "))
    for i in range(1, b4 + 1):
        print(f"{i}: {fonk1(i)}")
    b5 = datetime.datetime.now()
    b6 = datetime.datetime.now()
    b7 = b6 - b5
    print("Execution time:", b7)
if b8 = = "__main__":
    fonk2()