def fonk1(b3):
    b1 = int(''.join(str(x) for x in b3))
    b1+=1
    b2 = [int(i) for i in str(b1)]
    return b2
b3 = [1,2,4,5,3,2,2,9]
print(fonk1(b3))