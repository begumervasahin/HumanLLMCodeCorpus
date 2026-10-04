def fonk1(b3):
    b1 = len(b3)
    for i in range(0,b1):
        b2 = i
        for j in range(i+1,b1):
            if b3[j] < b3[b2]:
                b2 = j
        b3[i],b3[b2] = b3[b2], b3[i]
b3 = [6,5,8,4,3,2,8,9,10,15,0]
print(b3)
fonk1(b3)
print(b3)