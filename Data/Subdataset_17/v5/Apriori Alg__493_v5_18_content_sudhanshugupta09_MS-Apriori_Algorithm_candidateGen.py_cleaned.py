def generate_level2_candidates(L, phi, MIS, support_count):
    candidates = []
    for i, l in enumerate(L):
        if support_count[l] >= MIS[l]:
            for h in L[i + 1:]:
                if support_count[h] >= MIS[l] and abs(support_count[h] - support_count[l]) <= phi:
                    candidates.append((l, h))
    return candidates
def generate_MS_candidates(F, phi, support_count, k, MIS):
    candidates = []
    for f1 in F:
        for f2 in F:
            if f1 != f2 and f1[:-1] == f2[:-1] and f1[-1] < f2[-1] and abs(support_count[f1[-1]] - support_count[f2[-1]]) <= phi:
                candidate = f1 + (f2[-1],)
                candidates.append(candidate)
                for i in range(len(candidate)):
                    subset = candidate[:i] + candidate[i + 1:]
                    if candidate[0] in subset or MIS[candidate[1]] == MIS[candidate[0]]:
                        if subset not in F:
                            candidates.remove(candidate)
                            break
    return candidates