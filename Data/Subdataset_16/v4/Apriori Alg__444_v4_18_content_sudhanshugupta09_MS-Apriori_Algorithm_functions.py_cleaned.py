
import re
from operator import itemgetter
def fonk1(MIS):
    return sorted(MIS.items(), b1 = itemgetter(1))
def fonk2(I, MIS):
    I.extend(MIS.keys())
def fonk3(M, L, MIS, support_count):
    b2 = True
    for item, mis_val in M:
        if support_count[item] >= MIS[item] and b2:
            L.append(item)
            b3 = MIS[item]
            b2 = False
        elif not b2:
            if support_count[item] >= b3:
                L.append(item)
def fonk4(F, cannot_be_together):
    b4 = [[], [], [], [], []]
    a1 = 0
    for f in F:
        if len(f) > 0:
            for s in f:
                if a1 > 0:
                    for c in cannot_be_together:
                        if not set(c).issubset(s):
                            b4[a1].append(s)
                else:
                    b4[a1].append(s)
            a1 += 1
    return b4
def fonk5(F, must_have):
    b5 = [[], [], [], [], []]
    a1 = 0
    for f in F:
        if len(f) > 0:
            b6 = set()
            for s in f:
                for must in must_have:
                    if a1 > 1:
                        if must in s:
                            b6.add(s)
                    else:
                        if s in must_have:
                            b6.add(s)
            b5[a1].extend(list(b6))
        a1 += 1
    return b5