def longest_common_subsequence(selector, i, j):
    if i < 0 or j < 0:
        if selector == 'check':
            return answer[::-1], len(answer)
        return 0
    if selector == 'check':
        last_i, last_j = i, j
        while last_j >= 0 and second.find(first[i], 0, last_j + 1) == -1:
            i -= 1
        while last_i >= 0 and first.find(second[j], 0, last_i + 1) == -1:
            j -= 1
        if not matching_characters(i, j):
            nearest_row = longest_common_subsequence('row', i - 1, j)
            nearest_col = longest_common_subsequence('col', i, j - 1)
            if nearest_row == 'nf':
                nearest_row = i
            if nearest_col == 'nf':
                nearest_col = j
            if nearest_row == i and nearest_col == j:
                longest_common_subsequence('check', i - 1, j - 1)
            elif nearest_row == i and nearest_col != j:
                longest_common_subsequence('check', i, nearest_col)
            elif nearest_row != i and nearest_col == j:
                longest_common_subsequence('check', nearest_row, j)
            else:
                longest_common_subsequence('check', nearest_row, j) if (nearest_row + 1) * (j + 1) > (
                            nearest_col + 1) * (i + 1) else longest_common_subsequence('check', i, nearest_col)
        else:
            answer.append(first[i])
            longest_common_subsequence('check', i - 1, j - 1)
    elif selector == 'row':
        if i == 0 and not matching_characters(i, j):
            return 'nf' if not matching_characters(i, j) else 0
        return i if matching_characters(i, j) else longest_common_subsequence('row', i - 1, j)
    elif selector == 'col':
        if j == 0:
            return 'nf' if not matching_characters(i, j) else 0
        return j if matching_characters(i, j) else longest_common_subsequence('col', i, j - 1)
def matching_characters(i, j):
    return first[i] == second[j]
from sys import argv
if len(argv) >= 3:
    first = argv[1]
    second = argv[2]
    answer = []
    longest_common_subsequence('check', len(first) - 1, len(second) - 1)
    print(answer, 'with length:', len(answer))
else:
    print('Not enough arguments passed\n > Try: LCS.py [first_argument] [second_argument]')