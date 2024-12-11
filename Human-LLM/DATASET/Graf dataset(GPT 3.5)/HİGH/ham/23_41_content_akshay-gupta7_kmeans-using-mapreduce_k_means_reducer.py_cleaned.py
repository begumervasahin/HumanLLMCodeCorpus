import sys, random
import numpy as np
b1 = []
b2 = np.zeros((5,), dtype=np.float)
b3 = np.zeros((5,), dtype=np.float)
b4 = np.zeros((5,), dtype=np.int)
for line in sys.stdin:
    b5 = line.strip().split("\t")
    a2, salary , b6 = b5
    b2[int(a2)]+= float(salary)
    b3[int(a2)]+=float(b6)
    b4[int(a2)]+=1
print b2
print "\n"
print b3
print "\n"
print b4
a1 = 0
a2 = 0
for a1 in range(len(b4)):
    if (b4[a1]!=0) :
        b1.append((a2, float(b2[a1]/b4[a1]), float(b3[a1]/b4[a1])))
    a2+=1
print b1
b7 = open("b1.txt","w+")
a1 = 0
for a1 in range(len(b1)):
    b9, sly, b8 = str(b1[a1]).split(",")
    print b9
    print sly
    print b8
    b9 = b9[:0] + b9[1:]
    print b9
    print sly
    b8 = b8[:-1]
    print b8
    b7.write(b9)
    b7.write("\t")
    b7.write(sly)
    b7.write(";")
    b7.write(b8)
    b7.write("\n")
b7.close()