import itertools
import numpy as np
def calculate_continuity_score(sequence):
    if 0 in sequence:
        zero_groups = [list(group) for key, group in itertools.groupby(sequence) if key == 0]
        longest_zero_group = max(len(group) for group in zero_groups)
        total_zeros = sequence.count(0)
        continuity_score = 1 - longest_zero_group / total_zeros
    else:
        continuity_score = 0
    return continuity_score
def find_max_continuity_pair(sequence):
    n = len(sequence) - 1
    zero_indices = []
    for i in range(n):
        if sequence[i] + sequence[i + 1] == 0:
            zero_indices.extend([i, i + 1])
    pairs = np.array(zero_indices).reshape(-1, 2)
    continuity_scores = []
    for pair in pairs:
        sequence_copy = sequence[:]
        sequence_copy[pair[0]], sequence_copy[pair[1]] = 1, 1
        continuity_score = calculate_continuity_score(sequence_copy)
        continuity_scores.append(continuity_score)
        sequence_copy[pair[0]], sequence_copy[pair[1]] = 0, 0
    if len(continuity_scores) == 0:
        max_pair = np.array([9, 9])
        max_continuity = 9
    else:
        max_continuity = min(continuity_scores)
        max_continuity_index = continuity_scores.index(min(continuity_scores))
        max_pair = pairs[max_continuity_index]
    return max_pair, max_continuity
if __name__ == '__main__':
    sequence = [0, 1, 0, 0, 0, 0]
    print(find_max_continuity_pair(sequence))