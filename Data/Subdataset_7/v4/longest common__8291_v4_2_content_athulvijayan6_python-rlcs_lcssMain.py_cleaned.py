from __future__ import division
import numpy as np
import scipy.io
import matplotlib.pyplot as plt
from lcs import rlcs as rlcs
b1 = './'
b2 = np.load('sample-data/b2.npy')
b3 = np.load('sample-data/b3.npy')
a1 = 0.005
a2 = 1e-4
a3 = 10
score, diag, b4 = rlcs.rlcs(b2, b3, a1=a1, delta=0.5)
b5 = rlcs.backtrack(b2, b3, score, diag, b4)
xSegs, b6 = rlcs.getSoftSegments(b5, b2, b3, a2=a2, a3=a3)
fig, b7 = plt.subplots()
b8 = [seg.shape[0] for seg in xSegs]
b9 = b8.index(max(b8))
xseg, b10 = xSegs[b9], b6[b9]
b7.plot(range(xseg.size), xseg)
b7.plot(range(b10.size), b10)
b7.set_xlabel('x')
b7.set_ylabel('y')
b7.set_title('Matched signals for RLCS with distance threshold ' + str(a1))
fig.savefig(b1 + 'rlcsMain_getSegs.eps')
fig, b7 = rlcs.plotLCS(b5, b2, b3)
b7.set_xlabel('query')
b7.set_ylabel('reference')
b7.set_title('Match of signals after backtrack with distance threshold ' + str(a1))
fig.savefig(b1 + 'rlcsMain_backtrack.eps')
plt.show()