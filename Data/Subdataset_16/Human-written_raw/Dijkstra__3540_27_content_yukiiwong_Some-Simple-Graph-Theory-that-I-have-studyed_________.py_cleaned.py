def fonk1(adict,alist):
    a1 = 10000
    a2 = -1
    for i in alist:
        if adict[i] < a1:
            a1 = adict[i]
            a2 = i
    return a2
a3 = 10000
b1 = [[0,1,a3,2,a3,a3],
          [a3,0,3,4,a3,a3],
          [a3,a3,0,5,1,a3],
          [a3,4,a3,0,a3,a3],
          [a3,a3,2,3,0,a3],
          [a3,a3,2,a3,2,0]]
a4 = 1
b2 = [i for i in range(len(b1))]
b3 = []
b2.remove(a4)
b3.append(a4)
a1 = {a4 : 0}
for i in b2:
    a1[i] = 10000
b4 = [0]*len(b1)
for i in b3:
    for j in b2:
        b5 = a1[i] + b1[i][j]
        if b5 < a1[j]:
            a1[j] = b5
            b4[j] = i
    b6 = fonk1(a1,b2)
    if b6 = = -1:
        print("æ æ³å°è¾¾ç¹{}".format(b2))
        b2.remove(b2[0])
    else:
        b3.append(b6)
        b2.remove(b6)
        print("%d -> %d" %(b4[b6],b6))
    if b2 = = []:
        break
print(a1)