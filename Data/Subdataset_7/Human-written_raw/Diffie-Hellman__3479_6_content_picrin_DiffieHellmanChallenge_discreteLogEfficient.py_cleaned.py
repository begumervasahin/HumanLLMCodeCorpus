import sys
b1 = sys.argv[1]
with open(b1, "r") as f:
    b2 = int(f.readlines()[0])
b3 = int(sys.argv[2])
import random
b4 = random.randint(0, b2)
b5 = b2
b6 = b4
a1 = -1
a2 = -1
b7 = {b5: [1, 0], b6: [0, 1]}
b8 = b5
b9 = b6
a3 = 0
while a1 != 0:
    a1 = b8 % b9
    a3 += 1
    b10 = b8 / b9
    b11 = b7[b8]
    b12 = b7[b9]
    b13 = b10 * b12[0]
    b14 = b10 * b12[1]
    b7[a1] = [b11[0] - b13, b11[1] - b14]
    b8 = b9
    if a1 = = 0:
        a2 = b9
    b9 = a1
b15 = (b7[a2][1] + b2) % b2
print (b3 * b15)