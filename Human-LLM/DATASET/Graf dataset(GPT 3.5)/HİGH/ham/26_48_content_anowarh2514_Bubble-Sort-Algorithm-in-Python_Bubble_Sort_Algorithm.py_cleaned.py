def fonk1(b2):
    for i in range(len(b2)-1,0,-1):
        for j in range(i):
            if b2[j] > b2[j+1]:
                b1 = b2[j]
                b2[j] = b2[j+1]
                b2[j+1] = b1
        print(b2)
b2 = [5,3,8,6,7,2]
print("Unsorted b3 = ",b2)
fonk1(b2)
print(b2)