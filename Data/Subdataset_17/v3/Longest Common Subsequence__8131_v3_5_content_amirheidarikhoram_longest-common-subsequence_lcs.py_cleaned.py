import sys
def lcs(action, i, j):
    if i >= 0 and j >= 0:
        if action == 'check':
            i, j = find_matching_indices(i, j)
            if i < 0 or j < 0:
                return
            if first[i] == second[j]:
                ans.append(first[i])
                lcs('check', i - 1, j - 1)
            else:
                inear = lcs('row', i - 1, j)
                if inear == 'nf':
                    inear = i
                jnear = lcs('col', i, j - 1)
                if jnear == 'nf':
                    jnear = j
                next_action = determine_next_action(inear, jnear, i, j)
                lcs('check', *next_action)
        elif action == 'row':
            return find_row_match(i, j)
        elif action == 'col':
            return find_col_match(i, j)
    else:
        if action == 'row' or action == 'col':
            return 0
        else:
            ans.reverse()
            return 0
def find_matching_indices(i, j):
    li, lj = i, j
    while second.find(first[i], 0, lj + 1) == -1 and i >= 0:
        i -= 1
    while first.find(second[j], 0, li + 1) == -1 and j >= 0:
        j -= 1
    return i, j
def determine_next_action(inear, jnear, i, j):
    if inear == i and jnear == j:
        return (i - 1, j - 1)
    elif inear == i:
        return (i, jnear)
    elif jnear == j:
        return (inear, j)
    else:
        return (inear, j) if (inear + 1) * (j + 1) > (jnear + 1) * (i + 1) else (i, jnear)
def find_row_match(i, j):
    if i == 0 and num(i, j) != 1:
        return 'nf' if num(i, j) != 1 else 0
    return i if num(i, j) == 1 else lcs('row', i - 1, j)
def find_col_match(i, j):
    if j == 0:
        return 'nf' if num(i, j) != 1 else 0
    return j if num(i, j) == 1 else lcs('col', i, j - 1)
def num(i, j):
    return 1 if first[i] == second[j] else 0
if __name__ == "__main__":
    if len(sys.argv) >= 3:
        first = sys.argv[1]
        second = sys.argv[2]
        ans = []
        lcs('check', len(first) - 1, len(second) - 1)
        print(ans, 'with length:', len(ans))
    else:
        print('Not enough arguments passed\n > Try: LCS.py [first_argument] [second_argument]')