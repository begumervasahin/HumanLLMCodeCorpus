def sub_sequence(st1, st2):
    st1 = list(st1)
    st2 = list(st2)
    if len(st1) <= len(st2):
        lower = st1
        bigger = st2
    else:
        lower = st2
        bigger = st1
    longest_subseq = []
    for start in range(len(lower)):
        current_subseq = []
        index_bigger = 0
        for char in lower[start:]:
            if char in bigger[index_bigger:]:
                current_subseq.append(char)
                index_bigger += bigger[index_bigger:].index(char) + 1
        if all(current_subseq.count(char) <= lower.count(char) and current_subseq.count(char) <= bigger.count(char) for char in current_subseq):
            if len(current_subseq) > len(longest_subseq):
                longest_subseq = current_subseq
    return ''.join(longest_subseq)
print(sub_sequence('ABCABA', 'ABBA'))
print(sub_sequence('aaaaa', 'aa'))
print(sub_sequence('AGGTAB', 'GXTXAYB'))
print(sub_sequence('ABAZDC', 'BACBAD'))
