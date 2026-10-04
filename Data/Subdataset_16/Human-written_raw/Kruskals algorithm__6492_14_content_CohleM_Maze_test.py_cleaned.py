import random
from collections import defaultdict
b1 = list()
b2 = defaultdict(list)
a1 = 0
for b5 in range(9):
    for b in range(9):
        b2[a1].append((b5,b))
        a1 +=1
        for b6 in range(-1,2):
            for d in range(-1,2):
                if abs(b6) == abs(d) : continue
                b3 = (b5 + b6,b + d)
                if ((b3[0] >=0 and b3[0] <=8) and (b3[1] >=0 and b3[1] <=8)):
                    if [b3,(b5,b)] in b1: continue
                    b1.append([(b5,b),b3])
b4 = list()
while len(b2) > 1:
    b5 = random.randint(0,(len(b1)-1))
    for b in b2:
        for b6 in b2[b]:
            if b6 = = b1[b5][0]:
                b7 = (b,b6)
                break
    for d in b2:
        for b8 in b2[d]:
            if b8 = = b1[b5][1]:
                b9 = (d,b8,b2[d])
                break
    if b7[0] == b9[0]: continue
    print(b1[b5])
    print('\n')
    print('b7[0]',b2[b7[0]])
    print('b9[2] : ' ,b9[2])
    for q in b9[2]:
        b2[b7[0]].append(q)
    b2.pop(b9[0],None)
    b1.pop(b5)
    b4.append(b5)
    for k in b2:
        print(b2[k])
    print(len(b1),len(b2) , b5 )
    print('\n')
for key,value in b2.items():
    print(key , ':', value)