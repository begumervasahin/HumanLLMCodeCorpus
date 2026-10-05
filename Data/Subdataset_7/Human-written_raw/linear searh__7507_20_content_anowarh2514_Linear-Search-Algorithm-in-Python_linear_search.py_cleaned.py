def fonk1(b1,b2):
    a1 = 0
    while a1 < len(b1):
        if b1[a1] == int(b2):
            globals()['a2'] = a1
            return True
        a1 = a1 + 1
    return False
a2 = -1
b1 = [21,33,45,9,24,9,34,7,88,96,54,35,66,77]
b2 = input("Input The Number You Searching For = ")
if fonk1(b1,int(b2)):
    print("The Number Is Found At: ", a2+1)
else:
    print("Not Found")