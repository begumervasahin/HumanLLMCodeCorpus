from __future__ import division
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cbook
def union_changepoints(allchangepoints):
    startpoints = sorted(set(cbook.flatten(allchangepoints)))
    return [(startpoint, nextstartpoint) for startpoint, nextstartpoint in zip(startpoints[:-1], startpoints[1:])]
def plot_with_changepoints(data, changepoints):
    plt.figure()
    plt.plot(data)
    rect = plt.axis()
    plt.vlines([c[1] for c in changepoints[:-1]], rect[2], rect[3], color='r', linestyles='dashed')
    plt.axis(rect)
    plt.show()
def indicators_to_changepoints(indicators):
    pos, = np.where(np.diff(np.array(indicators, dtype=int)) == 1)
    pos = np.concatenate(((0,), pos + 1, (len(indicators),)))
    return [(a, b) for a, b in zip(pos[:-1], pos[1:])]
if __name__ == "__main__":
    data = np.random.rand(100)
    indicators = [False, False, True, False, False, False, False, True, False, False, True, False, False, False, True]
    changepoints = indicators_to_changepoints(indicators)
    plot_with_changepoints(data, changepoints)
    all_changepoints = [changepoints, [(0, 5), (5, 10), (10, 15)]]
    unified_changepoints = union_changepoints(all_changepoints)
    print("Unified Changepoints:", unified_changepoints)