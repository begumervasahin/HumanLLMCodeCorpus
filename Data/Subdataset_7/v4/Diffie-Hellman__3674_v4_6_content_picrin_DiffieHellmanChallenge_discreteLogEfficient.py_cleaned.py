import sys
import random
b1 = sys.argv[1]
with open(b1, "r") as file:
    b2 = int(file.readline().strip())
b3 = int(sys.argv[2])
b4 = random.randint(0, b2)
left, b5 = b2, b4
a1 = -1
a2 = -1
b6 = {left: [1, 0], b5: [0, 1]}
b12, b7 = left, b5
a3 = 0
while a1 != 0:
    a1 = b12 % b7
    a3 += 1
    b8 = b12
    reconstruct_left, b9 = b6[b12], b6[b7]
    b10 = b8 * b9[0]
    b11 = b8 * b9[1]
    b6[a1] = [reconstruct_left[0] - b10, reconstruct_left[1] - b11]
    b12 = b7
    if a1 = = 0:
        a2 = b7
    b7 = a1
b13 = (b6[a2][1] + b2) % b2
print(b3 * b13)