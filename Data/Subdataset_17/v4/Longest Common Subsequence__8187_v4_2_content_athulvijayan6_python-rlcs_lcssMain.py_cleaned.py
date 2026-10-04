from __future__ import division
import numpy as np
import scipy.io
import matplotlib.pyplot as plt
import rlcs
plt.style.use('ggplot')
plot_dir = './'
X = np.load('sample-data/X.npy')
Y = np.load('sample-data/Y.npy')
tau_dist = 0.005
delta = 0.5
score, diag, cost = rlcs.rlcs(X, Y, tau_dist=tau_dist, delta=delta)
segment = rlcs.backtrack(X, Y, score, diag, cost)
len_segment = segment.shape[0]
score_threshold = 1e-4
length_threshold = 10
x_segments, y_segments = rlcs.getSoftSegments(segment, X, Y, score_thres=score_threshold, len_thres=length_threshold)
segment_lengths = [seg.shape[0] for seg in x_segments]
longest_segment_index = segment_lengths.index(max(segment_lengths))
x_segment, y_segment = x_segments[longest_segment_index], y_segments[longest_segment_index]
fig, ax = plt.subplots()
ax.plot(range(x_segment.size), x_segment, label='X Segment')
ax.plot(range(y_segment.size), y_segment, label='Y Segment')
ax.set_xlabel('Index')
ax.set_ylabel('Value')
ax.set_title(f'Matched signals for RLCS with dist_thres {tau_dist}')
ax.legend()
fig.savefig(plot_dir + 'rlcsMain_getSegs.eps')
fig, ax = rlcs.plotLCS(segment, X, Y)
ax.set_xlabel('Query')
ax.set_ylabel('Reference')
ax.set_title(f'Match of signals after backtrack with dist_thres {tau_dist}')
fig.savefig(plot_dir + 'rlcsMain_backtrack.eps')
plt.show()