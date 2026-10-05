import math
import time
b1 = input("Check prime numbers: ")
b2 = time.time()
b1 = int(b1)
a1 = 2
a2 = 0
b3 = []
b4 = True
b5 = True
with open('output.txt','r') as rf:
    for line in rf:
        b3.append(int(line))
    a1 = int(b3[-1])
while a1 <= b1:
    if len(b3) > a2:
        while b3[a2] <= math.sqrt(a1) and b5:
            if a1 % b3[a2] == 0:
                b4 = False
                b5 = False
            elif a2+1 < len(b3):
                a2 += 1
            else:
                b5 = False
        if b4:
            b3.append(a1)
    a1 += 1
    a2 = 0
    b4 = True
    b5 = True
'''
while a1 <= b1:
    while a2 < math.sqrt(a1):
        if a1%a2 = = 0:
            b4 = False
            a2 = a1
        else:
            a2 += 1
    if b4:
        b3.append(a1)
    a1 += 1
    a2 = 2
    b4 = True
'''
b6 = time.time()
with open('output.txt', 'w') as wf:
    for z in b3:
        wf.write(str(z)+ "\b1")
print(str(b6-b2) + " seconds to calculate")