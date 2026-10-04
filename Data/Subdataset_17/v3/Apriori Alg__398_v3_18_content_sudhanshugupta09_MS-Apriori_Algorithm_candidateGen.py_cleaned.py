def generate_level2_candidates(L, phi, MIS, support_count):
    level2_candidates = []
    for i in range(len(L)):
        item1 = L[i]
        if support_count[item1] >= MIS[item1]:
            for item2 in L[i+1:]:
                if (support_count[item2] >= MIS[item1] and
                        abs(support_count[item2] - support_count[item1]) <= phi):
                    level2_candidates.append((item1, item2))
    return level2_candidates
def generate_MSCandidates(frequent_itemsets, phi, support_count, k, MIS):
    candidates = []
    for f1 in frequent_itemsets:
        for f2 in frequent_itemsets:
            if f1 != f2 and f1[:-1] == f2[:-1] and f1[-1] < f2[-1]:
                if abs(support_count[f1[-1]] - support_count[f2[-1]]) <= phi:
                    candidate = f1 + (f2[-1],)
                    candidates.append(candidate)
                    for j in range(len(candidate)):
                        subset = candidate[:j] + candidate[j+1:]
                        if (candidate[0] in subset or MIS[candidate[1]] == MIS[candidate[0]]) and subset not in frequent_itemsets:
                            candidates.remove(candidate)
                            break
    return candidates
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
    level2_candidates = generate_level2_candidates(L, phi, MIS, support_count)
    print("Level 2 Candidates:", level2_candidates)
    frequent_itemsets = [(20,), (30,), (40,), (50,), (60,), (70,), (80,), (90,), (100,), (120,), (140,)]
    k = 3
    candidates = generate_MSCandidates(frequent_itemsets, phi, support_count, k, MIS)
    print("Candidates:", candidates)