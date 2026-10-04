def level2_candidate_gen(L, phi, MIS, support_count):
    temp_list = []
    for i in range(len(L)):
        l = L[i]
        if support_count[l] >= MIS[l]:
            for h in L[i+1:]:
                if support_count[h] >= MIS[l] and abs(support_count[h] - support_count[l]) <= phi:
                    temp_list.append((l, h))
    return temp_list
def MSCandidate_gen(F, phi, support_count, k, MIS):
    temp_list = []
    for f1 in F:
        for f2 in F:
            if f1 != f2 and f1[:-1] == f2[:-1] and f1[-1] < f2[-1]:
                if abs(support_count[f1[-1]] - support_count[f2[-1]]) <= phi:
                    candidate = f1 + (f2[-1],)
                    temp_list.append(candidate)
                    for j in range(len(candidate)):
                        subset = candidate[:j] + candidate[j+1:]
                        if (candidate[0] in subset or MIS[candidate[1]] == MIS[candidate[0]]) and subset not in F:
                            temp_list.remove(candidate)
                            break
    return temp_list
if __name__ == "__main__":
    L = [20, 30, 40, 50, 60, 70, 80, 90, 100, 120, 140]
    phi = 0.1
    MIS = {
        10: 0.43, 20: 0.30, 30: 0.30, 40: 0.40, 50: 0.40, 60: 0.30,
        70: 0.20, 80: 0.20, 90: 0.20, 100: 0.10, 120: 0.20, 140: 0.15
    }
    support_count = {
        20: 6, 30: 4, 40: 2, 50: 2, 60: 3, 70: 5, 80: 6,
        90: 2, 100: 1, 120: 1, 140: 1
    }
    level2_candidates = level2_candidate_gen(L, phi, MIS, support_count)
    print("Level 2 Candidates:", level2_candidates)
    F = [(20,), (30,), (40,), (50,), (60,), (70,), (80,), (90,), (100,), (120,), (140,)]
    k = 3
    candidates = MSCandidate_gen(F, phi, support_count, k, MIS)
    print("Candidates:", candidates)