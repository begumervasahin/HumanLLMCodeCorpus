def fonk1(L, phi, MIS, support_count):
    b1 = []
    for i, l in enumerate(L):
        if support_count[l] >= MIS[l]:
            for h in L[i + 1:]:
                if support_count[h] >= MIS[l] and abs(support_count[h] - support_count[l]) <= phi:
                    b1.append((l, h))
    return b1
def fonk2(F, phi, support_count, k, MIS):
    b1 = []
    for f1 in F:
        for f2 in F:
            if f1 != f2 and f1[:-1] == f2[:-1] and f1[-1] < f2[-1] and abs(support_count[f1[-1]] - support_count[f2[-1]]) <= phi:
                b2 = f1 + (f2[-1],)
                b1.append(b2)
                for i in range(len(b2)):
                    b3 = b2[:i] + b2[i + 1:]
                    if b2[0] in b3 or MIS[b2[1]] == MIS[b2[0]]:
                        if b3 not in F:
                            b1.remove(b2)
                            break
    return b1