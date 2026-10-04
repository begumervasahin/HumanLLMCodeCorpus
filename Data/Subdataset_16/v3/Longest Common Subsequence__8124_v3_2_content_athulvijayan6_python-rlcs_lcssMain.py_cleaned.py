from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from lcs import rlcs as rlcs
plt.style.use('ggplot')
b1 = './'
def fonk1():
    b2 = np.load('sample-data/b2.npy')
    b3 = np.load('sample-data/b3.npy')
    return b2, b3
def fonk2(b2, b3, a1, a2):
    score, diag, b4 = rlcs.rlcs(b2, b3, a1=a1, a2=a2)
    b5 = rlcs.backtrack(b2, b3, score, diag, b4)
    return score, diag, b4, b5
def fonk3(b5, b2, b3, a3, a4):
    xSegs, b6 = rlcs.getSoftSegments(b5, b2, b3, a3=a3, a4=a4)
    return xSegs, b6
def fonk4(xSegs, b6, a1):
    fig, b7 = plt.subplots()
    b8 = [b5.shape[0] for b5 in xSegs]
    b9 = b8.index(max(b8))
    xseg, b10 = xSegs[b9], b6[b9]
    b7.plot(range(xseg.size), xseg, b11 = 'b2 Segment')
    b7.plot(range(b10.size), b10, b11 = 'b3 Segment')
    b7.set_xlabel('Time')
    b7.set_ylabel('Amplitude')
    b7.set_title(f'Matched signals for RLCS with distance threshold {a1}')
    b7.legend()
    fig.savefig(b1 + 'rlcsMain_getSegs.eps')
def fonk5(b5, b2, b3, a1):
    fig, b7 = rlcs.plotLCS(b5, b2, b3)
    b7.set_xlabel('Query Index')
    b7.set_ylabel('Reference Index')
    b7.set_title(f'Match of signals after backtrack with distance threshold {a1}')
    fig.savefig(b1 + 'rlcsMain_backtrack.eps')
def fonk6():
    a1 = 0.005
    a2 = 0.5
    a3 = 1e-4
    a4 = 10
    b2, b3 = fonk1()
    score, diag, b4, b5 = fonk2(b2, b3, a1, a2)
    xSegs, b6 = fonk3(b5, b2, b3, a3, a4)
    fonk4(xSegs, b6, a1)
    fonk5(b5, b2, b3, a1)
    plt.show()
if b12 = = "__main__":
    fonk6()