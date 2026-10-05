def sub_sequence(st1, st2):
    st1 = list(st1)
    st2 = list(st2)
    current_subsequence = []
    longest_subsequence = []
    if len(st1) <= len(st2):
        shorter_string = st1
        longer_string = st2
    else:
        shorter_string = st2
        longer_string = st1
    for start_index in range(0, len(shorter_string) + 1):
        for char in shorter_string[start_index:]:
            if char in longer_string[index:]:
                current_subsequence.append(char)
                index = longer_string[index:].index(char) + index + 1
        index = 0
        for char in current_subsequence:
            if current_subsequence.count(char) > shorter_string.count(char) or current_subsequence.count(char) > longer_string.count(char):
                current_subsequence = []
        if len(current_subsequence) >= len(longest_subsequence):
            longest_subsequence = current_subsequence
            current_subsequence = []
        else:
            current_subsequence = []
    result = ''.join(longest_subsequence)
    return result
print(sub_sequence('ABCABA', 'ABBA'))
print(sub_sequence('aaaaa', 'aa'))
print(sub_sequence('AGGTAB', 'GXTXAYB'))
print(sub_sequence('ABAZDC', 'BACBAD'))
