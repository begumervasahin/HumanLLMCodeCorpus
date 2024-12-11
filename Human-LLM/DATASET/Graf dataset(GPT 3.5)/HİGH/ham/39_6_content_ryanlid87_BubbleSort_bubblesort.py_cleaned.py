def fonk1(a):
        for a1 in range(len(a)):
                for x in range(0,len(a)-1):
                        if a[x] > a[x+1]:
                                a[x+1],a[x] = a[x],a[x+1]
        return a
def fonk2(a):
        if len(a)>1:
                b1 = len(a)
                b2 = a[:b1]
                b3 = a[b1:]
                fonk2(b2)
                fonk2(b3)
                a1 = 0
                a2 = 0
                a3 = 0
                print b2,b3
                while a1<len(b2) and a2<len(b3):
                        if b2[a1] < b3[a2]:
                                a[a3]=b2[a1]
                                a1 = a1+1
                        else:
                                a[a3]=b3[a2]
                                a2 = a2+1
                        a3 = a3+1
                while a1< len(b2):
                        a[a3]=b2[a1]
                        a1 = a1+1
                        a3 = a3+1
                while a2 < len(b3):
                        a[a3]=b3[a2]
                        a2 = a2+1
                        a3 = a3+1
                print a