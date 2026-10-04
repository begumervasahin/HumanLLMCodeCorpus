from __future__ import division
import numpy as np
import scipy.io
import matplotlib.pyplot as plt
from lcs import rlcs as rlcs
plt.style.use('ggplot')
plotDir = './'
X = np.load('sample-data/X.npy')
Y = np.load('sample-data/Y.npy')
tau_dist = 0.005
delta = 0.5
score_thres = 1e-4
len_thres = 10
score, diag, cost = rlcs.rlcs(X, Y, tau_dist=tau_dist, delta=delta)
segment = rlcs.backtrack(X, Y, score, diag, cost)
xSegs, ySegs = rlcs.getSoftSegments(segment, X, Y, score_thres=score_thres, len_thres=len_thres)
fig, ax = plt.subplots()
lens = [i.shape[0] for i in xSegs]
idx = lens.index(max(lens))
xseg, yseg = xSegs[idx], ySegs[idx]
ax.plot(range(xseg.size), xseg)
ax.plot(range(yseg.size), yseg)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title(f'Matched signals for rlcs with dist_thres {tau_dist}')
fig.savefig(plotDir + 'rlcsMain_getSegs.eps')
fig, ax = rlcs.plotLCS(segment, X, Y)
ax.set_xlabel('query')
ax.set_ylabel('reference')
ax.set_title(f'Match of signals after backtrack with dist_thres {tau_dist}')
fig.savefig(plotDir + 'rlcsMain_backtrack.eps')
plt.show()