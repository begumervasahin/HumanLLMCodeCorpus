from __future__ import division
import numpy as np
import scipy.io
from lcs import rlcs as rlcs
import matplotlib.pyplot as plt
plt.style.use('ggplot')
b1 = './'
b2 = np.load('sample-data/b2.npy')
b3 = np.load('sample-data/b3.npy')
a1 = 0.005
score, diag, b4 = rlcs.rlcs(b2, b3, a1= a1,  delta=0.5)
b5 = rlcs.backtrack(b2, b3, score, diag, b4)
b6 = b5.shape[0]
a2 = 1e-4
a3 = 10
xSegs, b7 = rlcs.getSoftSegments(b5, b2, b3, a2=a2, a3=a3)
fig, b8 = plt.subplots()
b9 = [i.shape[0] for i in xSegs]
b10 = b9.index(max(b9))
xseg, b11 = xSegs[b10], b7[b10]b8.plot(xrange(xseg.size), xseg)
b8.plot(xrange(b11.size), b11)
b8.set_xlabel('x')
b8.set_ylabel('y')
b8.set_title('Matched signals for rlcs with dist_thres ' + str(a1))
fig.savefig(b1+'rlcsMain_getSegs.eps')
fig, b8 = rlcs.plotLCS(b5, b2, b3)
b8.set_xlabel('query')
b8.set_ylabel('reference')
b8.set_title('Match of signals after backtrack with dist_thres ' + str(a1))
fig.savefig(b1+'rlcsMain_backtrack.eps')
plt.show()