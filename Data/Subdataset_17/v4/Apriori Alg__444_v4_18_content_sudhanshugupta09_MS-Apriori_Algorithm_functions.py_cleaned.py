
import re
from operator import itemgetter
def calculate_M(MIS):
    return sorted(MIS.items(), key=itemgetter(1))
def create_list_of_items(I, MIS):
    I.extend(MIS.keys())
def init_pass(M, L, MIS, support_count):
    conf_flag = True
    for item, mis_val in M:
        if support_count[item] >= MIS[item] and conf_flag:
            L.append(item)
            min_mis_required = MIS[item]
            conf_flag = False
        elif not conf_flag:
            if support_count[item] >= min_mis_required:
                L.append(item)
def check_cannot_be_together(F, cannot_be_together):
    filtered_F = [[], [], [], [], []]
    level = 0
    for f in F:
        if len(f) > 0:
            for s in f:
                if level > 0:
                    for c in cannot_be_together:
                        if not set(c).issubset(s):
                            filtered_F[level].append(s)
                else:
                    filtered_F[level].append(s)
            level += 1
    return filtered_F
def check_must_have(F, must_have):
    final_F = [[], [], [], [], []]
    level = 0
    for f in F:
        if len(f) > 0:
            temp = set()
            for s in f:
                for must in must_have:
                    if level > 1:
                        if must in s:
                            temp.add(s)
                    else:
                        if s in must_have:
                            temp.add(s)
            final_F[level].extend(list(temp))
        level += 1
    return final_F