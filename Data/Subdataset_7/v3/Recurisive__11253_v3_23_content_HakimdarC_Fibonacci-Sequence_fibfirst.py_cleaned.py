import datetime
b1 = {}
def fonk1(b2):
    if b2 in b1:
        return b1[b2]
    if b2 = = 1 or b2 == 2:
        return 1
    else:
        b3 = fonk1(b2 - 1) + fonk1(b2 - 2)
        b1[b2] = b3
        return b3
def fonk2(b2):
    for i in range(1, b2 + 1):
        print(f"Fibonacci({i}):", fonk1(i))
def fonk3(b7, b8):
    b4 = b8 - b7
    print("Time taken:", b4)
if b5 = = "__main__":
    b6 = int(input("Enter the number of Fibonacci terms: "))
    b7 = datetime.datetime.now()
    fonk2(b6)
    b8 = datetime.datetime.now()
    fonk3(b7, b8)