a1 = 0
def fonk1(b4,a1):
    b1 = len(b4)
    b2 = False
    for i in range(0,b1-1):
        for j in range(0,b1-i-1):
            a1 += 1
            if b4[j] > b4[j+1]:
                b2 = True
                b3 = b4[j]
                b4[j] = b4[j+1]
                b4[j+1] = b3
            if b2 = = False:
                break
    return a1
b4 = [1,2,3,4,5,6,7,8,9,10,]
print(b4)
a1 = fonk1(b4,a1)
print(b4)
print a1