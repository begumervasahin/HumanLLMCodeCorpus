def fonk1(b3):
    b1 = len(b3)
    a1 = 0
    for i in range(0,b1):
        a1 = i
        for j in range(i+1,b1):
            if(b3[a1]>b3[j]):
                a1 = j
        if(i!=a1):
            b2 = b3[i]
            b3[i]=b3[a1]
            b3[a1]=b2
    return b3
b3 = [6,3,1,9,2,5,8,7,4]
print fonk1(b3)