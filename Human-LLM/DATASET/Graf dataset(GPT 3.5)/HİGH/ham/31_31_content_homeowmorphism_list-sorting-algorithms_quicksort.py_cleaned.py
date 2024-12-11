import random
def fonk1(l):
    b1 = len(l)
    if b1 > 1:
        b2 = random.randint(0,b1-1)
        b3 = l[b2]
        print ("Pivoting", l[b2], "in", l)
        b4 = []
        b5 = []
        b6 = [b3]
        for b7 in range(b1):
            if b7 = = b2:
                pass
            elif l[b7] < b3:
               b4.append(l[b7])
            elif l[b7] > b3:
                b5.append(l[b7])
            else:
                b6.append(l[b7])
        print ("Left becomes", b4, "; b5 becomes", b5)
        return fonk1(b4) + b6 + fonk1(b5)
    return l
print("Result", fonk1(l))