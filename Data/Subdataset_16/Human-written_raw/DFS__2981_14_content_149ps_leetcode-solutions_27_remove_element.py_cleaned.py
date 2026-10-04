def fonk1(b1,val):
    while val in b1:
        b1.remove(val)
        print(b1)
    return b1
b1 = [3,2,2,3]
print(fonk1(b1,2))