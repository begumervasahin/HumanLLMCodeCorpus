def longest_common_subsequence(selector, index_first, index_second):
    if index_first >= 0 and index_second >= 0:
        if selector == 'check':
            last_index_first, last_index_second = index_first, index_second
            while second.find(first[index_first], 0, last_index_second + 1) == -1 and index_first >= 0:
                index_first -= 1
            while first.find(second[index_second], 0, last_index_first + 1) == -1 and index_second >= 0:
                index_second -= 1
            if matching_characters(index_first, index_second) != 1:
                nearest_row = longest_common_subsequence('row', index_first - 1, index_second)
                if nearest_row == 'nf':
                    nearest_row = index_first
                nearest_col = longest_common_subsequence('col', index_first, index_second - 1)
                if nearest_col == 'nf':
                    nearest_col = index_second
                if nearest_row == index_first and nearest_col == index_second:
                    longest_common_subsequence('check', index_first - 1, index_second - 1)
                elif nearest_row == index_first and nearest_col != index_second:
                    longest_common_subsequence('check', index_first, nearest_col)
                elif nearest_row != index_first and nearest_col == index_second:
                    longest_common_subsequence('check', nearest_row, index_second)
                else:
                    longest_common_subsequence('check', nearest_row, index_second) if (nearest_row + 1) * (
                            index_second + 1) > (nearest_col + 1) * (index_first + 1) else longest_common_subsequence(
                        'check', index_first, nearest_col)
            else:
                answer.append(first[index_first])
                longest_common_subsequence('check', index_first - 1, index_second - 1)
        elif selector == 'row':
            if index_first == 0 and matching_characters(index_first, index_second) != 1:
                return 'nf' if matching_characters(index_first, index_second) != 1 else 0
            else:
                return index_first if matching_characters(index_first, index_second) == 1 else longest_common_subsequence(
                    'row', index_first - 1, index_second)
        elif selector == 'col':
            if index_second == 0:
                return 'nf' if matching_characters(index_first, index_second) != 1 else 0
            else:
                return index_second if matching_characters(index_first, index_second) == 1 else longest_common_subsequence(
                    'col', index_first, index_second - 1)
    else:
        if selector == 'row' or selector == 'col':
            return 0
        else:
            answer.reverse()
            return 0
def matching_characters(index_first, index_second):
    return 1 if first[index_first] == second[index_second] else 0
from sys import argv
if len(argv) >= 3:
    first_string = argv[1]
    second_string = argv[2]
    answer = []
    longest_common_subsequence('check', len(first_string) - 1, len(second_string) - 1)
    print(answer, ' with length: ', len(answer))
else:
    print('Not enough arguments passed\n > Try: LCS.py [first_argument] [second_argument]')