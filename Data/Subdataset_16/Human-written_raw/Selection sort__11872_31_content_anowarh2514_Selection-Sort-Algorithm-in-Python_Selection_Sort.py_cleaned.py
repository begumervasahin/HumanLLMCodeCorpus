def fonk1(b3):
    for i in range(10):
        b1 = i
        for j in range(i,11):
            if b3[j] < b3[b1]:
                b1 = j
        b2 = b3[i]
        b3[i] = b3[b1]
        b3[b1] = b2
        print(b3)
b3 = [5,3,7,2,4,1,11,8,10,9,6]
fonk1(b3)
print(b3)