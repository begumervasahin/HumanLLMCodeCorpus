import datetime
b1 = {}
def fonk1(b2):
    if b2 in b1:
        return b1[b2]
    if b2 = = 1:
        a1 = 1
    elif b2 = = 2:
        a1 = 1
    else:
        a1 = fonk1(b2 - 1) + fonk1(b2 - 2)
    b1[b2] = a1
    return a1
b2 = int(input("Give the number of Fibonacci terms: "))
b3 = datetime.datetime.now()
for i in range(1, b2 + 1):
    print(i, ":", fonk1(i))
b4 = datetime.datetime.now()
b5 = b4 - b3
print("Time taken:", b5)