import re
from operator import itemgetter
def fonk1(MIS):
    return sorted(MIS.items(), b1 = itemgetter(1))
def fonk2(MIS):
    return list(MIS.keys())
def fonk3(M, MIS, support_count):
    b2 = []
    b3 = True
    b4 = None
    for item, mis_val in M:
        if support_count[item] >= MIS[item] and b3:
            b2.append(item)
            b4 = MIS[item]
            b3 = False
        elif not b3:
            if support_count[item] >= b4:
                b2.append(item)
    return b2
def fonk4(F, cannot_be_together):
    b5 = [[] for _ in range(len(F))]
    for level, f_level in enumerate(F):
        for itemset in f_level:
            if not any(set(pair).issubset(itemset) for pair in cannot_be_together):
                b5[level].append(itemset)
    return b5
def fonk5(F, must_have):
    b5 = [[] for _ in range(len(F))]
    for level, f_level in enumerate(F):
        for itemset in f_level:
            if any(must in itemset for must in must_have):
                b5[level].append(itemset)
    return b5