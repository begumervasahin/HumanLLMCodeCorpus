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
b2 = int(input("Enter the number of Fibonacci terms: "))
for i in range(1, b2 + 1):
    print(f"Fibonacci({i}):", fonk1(i))
b4 = datetime.datetime.now()
b5 = datetime.datetime.now()
b6 = b5 - b4
print("Time taken:", b6)