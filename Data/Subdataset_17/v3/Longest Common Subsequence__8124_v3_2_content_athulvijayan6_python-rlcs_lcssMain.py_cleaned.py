from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from lcs import rlcs as rlcs
plt.style.use('ggplot')
plot_dir = './'
def load_data():
    X = np.load('sample-data/X.npy')
    Y = np.load('sample-data/Y.npy')
    return X, Y
def compute_rlcs(X, Y, tau_dist, delta):
    score, diag, cost = rlcs.rlcs(X, Y, tau_dist=tau_dist, delta=delta)
    segment = rlcs.backtrack(X, Y, score, diag, cost)
    return score, diag, cost, segment
def extract_segments(segment, X, Y, score_thres, len_thres):
    xSegs, ySegs = rlcs.getSoftSegments(segment, X, Y, score_thres=score_thres, len_thres=len_thres)
    return xSegs, ySegs
def plot_matched_signals(xSegs, ySegs, tau_dist):
    fig, ax = plt.subplots()
    lens = [segment.shape[0] for segment in xSegs]
    idx = lens.index(max(lens))
    xseg, yseg = xSegs[idx], ySegs[idx]
    ax.plot(range(xseg.size), xseg, label='X Segment')
    ax.plot(range(yseg.size), yseg, label='Y Segment')
    ax.set_xlabel('Time')
    ax.set_ylabel('Amplitude')
    ax.set_title(f'Matched signals for RLCS with distance threshold {tau_dist}')
    ax.legend()
    fig.savefig(plot_dir + 'rlcsMain_getSegs.eps')
def plot_lcs(segment, X, Y, tau_dist):
    fig, ax = rlcs.plotLCS(segment, X, Y)
    ax.set_xlabel('Query Index')
    ax.set_ylabel('Reference Index')
    ax.set_title(f'Match of signals after backtrack with distance threshold {tau_dist}')
    fig.savefig(plot_dir + 'rlcsMain_backtrack.eps')
def main():
    tau_dist = 0.005
    delta = 0.5
    score_thres = 1e-4
    len_thres = 10
    X, Y = load_data()
    score, diag, cost, segment = compute_rlcs(X, Y, tau_dist, delta)
    xSegs, ySegs = extract_segments(segment, X, Y, score_thres, len_thres)
    plot_matched_signals(xSegs, ySegs, tau_dist)
    plot_lcs(segment, X, Y, tau_dist)
    plt.show()
if __name__ == "__main__":
    main()