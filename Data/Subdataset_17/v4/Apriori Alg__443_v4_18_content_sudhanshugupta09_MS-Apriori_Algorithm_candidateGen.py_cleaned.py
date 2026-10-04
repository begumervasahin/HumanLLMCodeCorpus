def level2_candidate_gen(L, phi, MIS, support_count):
    temp_list = []
    for i, l in enumerate(L):
        if support_count[l] >= MIS[l]:
            for h in L[i+1:]:
                if support_count[h] >= MIS[l] and abs(support_count[h] - support_count[l]) <= phi:
                    temp_list.append((l, h))
    return temp_list
def MSCandidate_gen(F, phi, support_count, k, MIS):
    temp_list = []
    for f1 in F:
        for f2 in F:
            if f1 != f2 and f1[:-1] == f2[:-1] and f1[-1] < f2[-1] and abs(support_count[f1[-1]] - support_count[f2[-1]]) <= phi:
                c = f1 + f2[-1:]
                temp_list.append(c)
                for i in range(len(c)):
                    s = c[:i] + c[i+1:]
                    if c[0] in s or MIS[c[1]] == MIS[c[0]]:
                        if s not in F:
                            temp_list.remove(c)
                            break
    return temp_list