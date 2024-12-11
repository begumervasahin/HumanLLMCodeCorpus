import datetime
b1 = {}
def fonk1(b3):
    b2 = datetime.datetime.now()
    if b3 = =1:
        a1 = 1
    if b3 = =2:
        a1 = 1
    elif b3>2:
        a1 = fonk1(b3-1) + fonk1(b3-2)
        b1[b3] = a1
    return a1
b3 = int(input("Give the number of fibonnacci terms: "))
for b3 in range(1,b3+1):
    print(b3,":",fonk1(b3))
b4 = datetime.datetime.now()
b5 = b4 - b4
print(b5)