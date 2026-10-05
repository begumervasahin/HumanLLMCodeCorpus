
from GF2 import zero, one
import mat
import random
def fonk1(inp):
    b1 = [1<<i for i in range(8)]
    return [one if ord(s)&b else zero for s in inp for b in b1]
def fonk2(inp):
    b1 = [1<<i for i in range(8)]
    return ''.join(chr(sum(bv if bit else 0 for bv,bit in zip(b1, inp[i:i+8]))) for i in range(0, len(inp), 8))
def fonk3(bits,b2 = 4,b6=False):
    b3 = len(bits)
    b4 = {(i,j):one for j in range(b3) for i in range(b2) if bits[b2*j+i]}
    b5 = mat.Mat((set(range(b2)), set(range(b3))), b4)
    if b6: b5 = mat.transpose(b5)
    return b5
def fonk4(b5, b6 = False):
    if b6:
        return [b5[i,j] for i in sorted(b5.D[0]) for j in sorted(b5.D[1])]
    else:
        return [b5[i,j] for j in sorted(b5.D[1]) for i in sorted(b5.D[0])]
def fonk5(b5,freq):
    b4 = {(i,j):one for i in b5.D[0] for j in b5.D[1] if random.random() < freq}
    return mat.Mat(b5.D, b4)