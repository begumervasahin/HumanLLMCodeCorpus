import itertools
import numpy as np
def calculate_continuity(x):
    if 0 in x:
        zero_groups = [list(group) for key, group in itertools.groupby(x) if key == 0]
        max_zero_group = max(len(group) for group in zero_groups)
        total_zeros = x.count(0)
        continuity = 1 - max_zero_group / total_zeros
    else:
        continuity = 0
    return continuity
def find_maximum_continuity_pair(lyst):
    n = len(lyst) - 1
    zero_indices = []
    for i in range(n):
        if lyst[i] + lyst[i + 1] == 0:
            zero_indices.extend([i, i + 1])
    pairs = np.array(zero_indices).reshape(-1, 2)
    continuity_values = []
    for pair in pairs:
        lyst_copy = lyst[:]
        lyst_copy[pair[0]], lyst_copy[pair[1]] = 1, 1
        continuity = calculate_continuity(lyst_copy)
        continuity_values.append(continuity)
        lyst_copy[pair[0]], lyst_copy[pair[1]] = 0, 0
    if len(continuity_values) == 0:
        max_pair = np.array([9, 9])
        max_continuity = 9
    else:
        max_continuity = min(continuity_values)
        max_continuity_index = continuity_values.index(min(continuity_values))
        max_pair = pairs[max_continuity_index]
    return max_pair, max_continuity
if __name__ == '__main__':
    sequence = [0, 1, 0, 0, 0, 0]
    print(find_maximum_continuity_pair(sequence))