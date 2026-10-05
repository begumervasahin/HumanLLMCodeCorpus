
from __future__ import division
import numpy as np
import scipy.io
import matplotlib.pyplot as plt
from lcs import rlcs as rlcs
plotDir = './'
X = np.load('sample-data/X.npy')
Y = np.load('sample-data/Y.npy')
tau_dist = 0.005
score_thres = 1e-4
len_thres = 10
score, diag, cost = rlcs.rlcs(X, Y, tau_dist=tau_dist, delta=0.5)
segment = rlcs.backtrack(X, Y, score, diag, cost)
xSegs, ySegs = rlcs.getSoftSegments(segment, X, Y, score_thres=score_thres, len_thres=len_thres)
fig, ax = plt.subplots()
segment_lengths = [i.shape[0] for i in xSegs]
max_length_index = segment_lengths.index(max(segment_lengths))
x_segment, y_segment = xSegs[max_length_index], ySegs[max_length_index]
ax.plot(range(x_segment.size), x_segment)
ax.plot(range(y_segment.size), y_segment)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Matched signals for RLCS with distance threshold ' + str(tau_dist))
fig.savefig(plotDir + 'rlcsMain_getSegs.eps')
fig, ax = rlcs.plotLCS(segment, X, Y)
ax.set_xlabel('query')
ax.set_ylabel('reference')
ax.set_title('Match of signals after backtrack with distance threshold ' + str(tau_dist))
fig.savefig(plotDir + 'rlcsMain_backtrack.eps')
plt.show()