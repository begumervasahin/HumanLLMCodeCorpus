from __future__ import division
import numpy as np
import scipy.io
import matplotlib.pyplot as plt
import rlcs
plt.style.use('ggplot')
b1 = './'
b2 = np.load('sample-data/b2.npy')
b3 = np.load('sample-data/b3.npy')
a1 = 0.005
a2 = 0.5
score, diag, b4 = rlcs.rlcs(b2, b3, a1=a1, a2=a2)
b5 = rlcs.backtrack(b2, b3, score, diag, b4)
b6 = b5.shape[0]
a3 = 1e-4
a4 = 10
x_segments, b7 = rlcs.getSoftSegments(b5, b2, b3, score_thres=a3, len_thres=a4)
b8 = [seg.shape[0] for seg in x_segments]
b9 = b8.index(max(b8))
x_segment, b10 = x_segments[b9], b7[b9]
fig, b11 = plt.subplots()
b11.plot(range(x_segment.size), x_segment, b12 = 'b2 Segment')
b11.plot(range(b10.size), b10, b12 = 'b3 Segment')
b11.set_xlabel('Index')
b11.set_ylabel('Value')
b11.set_title(f'Matched signals for RLCS with dist_thres {a1}')
b11.legend()
fig.savefig(b1 + 'rlcsMain_getSegs.eps')
fig, b11 = rlcs.plotLCS(b5, b2, b3)
b11.set_xlabel('Query')
b11.set_ylabel('Reference')
b11.set_title(f'Match of signals after backtrack with dist_thres {a1}')
fig.savefig(b1 + 'rlcsMain_backtrack.eps')
plt.show()