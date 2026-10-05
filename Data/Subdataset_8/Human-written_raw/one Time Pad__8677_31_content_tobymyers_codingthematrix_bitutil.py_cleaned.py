
from GF2 import zero, one
import mat
import random
def str2bits(inp):
    bs = [1<<i for i in range(8)]
    return [one if ord(s)&b else zero for s in inp for b in bs]
def bits2str(inp):
    bs = [1<<i for i in range(8)]
    return ''.join(chr(sum(bv if bit else 0 for bv,bit in zip(bs, inp[i:i+8]))) for i in range(0, len(inp), 8))
def bits2mat(bits,nrows=4,trans=False):
    ncols = len(bits)
    f = {(i,j):one for j in range(ncols) for i in range(nrows) if bits[nrows*j+i]}
    A = mat.Mat((set(range(nrows)), set(range(ncols))), f)
    if trans: A = mat.transpose(A)
    return A
def mat2bits(A, trans=False):
    if trans:
        return [A[i,j] for i in sorted(A.D[0]) for j in sorted(A.D[1])]
    else:
        return [A[i,j] for j in sorted(A.D[1]) for i in sorted(A.D[0])]
def noise(A,freq):
    f = {(i,j):one for i in A.D[0] for j in A.D[1] if random.random() < freq}
    return mat.Mat(A.D, f)