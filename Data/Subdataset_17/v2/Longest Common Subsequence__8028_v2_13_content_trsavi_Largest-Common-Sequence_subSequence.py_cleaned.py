def sub_sequence(st1, st2):
    st1, st2 = list(st1), list(st2)
    longest_subseq = []
    if len(st1) <= len(st2):
        shorter, longer = st1, st2
    else:
        shorter, longer = st2, st1
    def find_subsequence(start):
        temp_subseq, index = [], 0
        for char in shorter[start:]:
            if char in longer[index:]:
                temp_subseq.append(char)
                index = longer.index(char, index) + 1
        return temp_subseq
    for start in range(len(shorter) + 1):
        current_subseq = find_subsequence(start)
        if all(current_subseq.count(char) <= min(shorter.count(char), longer.count(char)) for char in current_subseq):
            if len(current_subseq) > len(longest_subseq):
                longest_subseq = current_subseq
    return ''.join(longest_subseq)
print(sub_sequence('ABCABA', 'ABBA'))
print(sub_sequence('aaaaa', 'aa'))
print(sub_sequence('AGGTAB', 'GXTXAYB'))
print(sub_sequence('ABAZDC', 'BACBAD'))
