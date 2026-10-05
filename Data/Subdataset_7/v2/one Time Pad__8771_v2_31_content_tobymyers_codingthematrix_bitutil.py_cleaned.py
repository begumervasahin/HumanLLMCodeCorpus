from GF2 import zero, one
import mat
import random
def fonk1(input_str):
    b1 = [1 << i for i in range(8)]
    return [one if ord(char) & bit else zero for char in input_str for bit in b1]
def fonk2(b1):
    a1 = 8
    return ''.join(chr(sum(bitval if bit else 0 for bitval, bit in zip(b1[i:i + a1], range(a1)))) for i in range(0, len(b1), a1))
def fonk3(b1, b2 = 4, b6=False):
    b3 = len(b1)
    b4 = {(i, j): one for j in range(b3) for i in range(b2) if b1[b2 * j + i]}
    b5 = mat.Mat((set(range(b2)), set(range(b3))), b4)
    if b6:
        b5 = mat.b6(b5)
    return b5
def fonk4(b5, b6 = False):
    if b6:
        return [b5[i, j] for i in sorted(b5.D[0]) for j in sorted(b5.D[1])]
    else:
        return [b5[i, j] for j in sorted(b5.D[1]) for i in sorted(b5.D[0])]
def fonk5(b5, frequency):
    b4 = {(i, j): one for i in b5.D[0] for j in b5.D[1] if random.random() < frequency}
    return mat.Mat(b5.D, b4)