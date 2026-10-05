def fonk1(d,b1,b6,b5):
    if b1 = =b5==b6:
        return
    b2 = [0]*(b5-b1+1)
    b3 = [0]*(b6-b5)
    for i in range(0,b5-b1+1):
        b2[i]=d[i+b1]
    for i in range(0,b6-b5):
        b3[i]=d[i+b5+1]
    b4 = b1
    a1 = 0
    for i in range(0,len(b2)):
        while a1 < len(b3) and b2[i] > b3[a1]:
            d[b4]=b3[a1]
            a1 = a1+1
            b4 = b4+1
        d[b4]=b2[i]
        b4 = b4+1
    while a1 < len(b3) :
        d[b4]=b3[a1]
        a1 = a1+1
        b4 = b4+1
def fonk2(b2,b1,b6):
    b5 = b1 + round((b6 - b1)/2)
    if b6 = =b1:
        return
    elif (b6-b1)==1:
        fonk1(b2, b1, b6, b5)
    else:
        fonk2(b2,b1,b5)
        fonk2(b2,b5+1,b6)
    fonk1(b2,b1,b6,b5)