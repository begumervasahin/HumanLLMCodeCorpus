def fonk1(b2):
    for passnum in range(len(b2)-1,0,-1):
        for i in range(passnum):
            if b2[i]>b2[i+1]:
                b1 = b2[i]
                b2[i] = b2[i+1]
                b2[i+1] = b1
b2 = [54,26,93,17,77,31,44,55,20]
fonk1(b2)
print(b2)