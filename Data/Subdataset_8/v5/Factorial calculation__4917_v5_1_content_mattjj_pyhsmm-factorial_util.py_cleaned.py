from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
def union_changepoints(all_changepoints):
    startpoints = sorted(set(cbook.flatten(all_changepoints)))
    return [(start, next_start) for start, next_start in zip(startpoints[:-1], startpoints[1:])]
def plot_with_changepoints(data, changepoints):
    plt.figure()
    plt.plot(data)
    rect = plt.axis()
    plt.vlines([c[1] for c in changepoints[:-1]], rect[2], rect[3], color='r', linestyles='dashed')
    plt.axis(rect)
    plt.show()
def indicators_to_changepoints(indicators):
    positions, = np.where(np.diff(np.array(indicators, dtype=int)) == 1)
    positions = np.concatenate(([0], positions + 1, [len(indicators)]))
    return [(a, b) for a, b in zip(positions[:-1], positions[1:])]
if __name__ == "__main__":
    data = np.random.rand(100)
    indicators = np.random.choice([False, True], size=100)
    changepoints = indicators_to_changepoints(indicators)
    plot_with_changepoints(data, changepoints)