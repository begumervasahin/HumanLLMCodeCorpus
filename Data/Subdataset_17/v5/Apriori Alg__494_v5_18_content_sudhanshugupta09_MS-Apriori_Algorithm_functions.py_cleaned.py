import re
from operator import itemgetter
def calculate_M(MIS):
    return sorted(MIS.items(), key=itemgetter(1))
def create_list_of_items(MIS):
    return list(MIS.keys())
def init_pass(M, MIS, support_count):
    L = []
    conf_flag = True
    min_mis_required = None
    for item, mis_val in M:
        if support_count[item] >= MIS[item] and conf_flag:
            L.append(item)
            min_mis_required = MIS[item]
            conf_flag = False
        elif not conf_flag:
            if support_count[item] >= min_mis_required:
                L.append(item)
    return L
def filter_cannot_be_together(F, cannot_be_together):
    filtered_F = [[] for _ in range(len(F))]
    for level, f_level in enumerate(F):
        for itemset in f_level:
            if not any(set(pair).issubset(itemset) for pair in cannot_be_together):
                filtered_F[level].append(itemset)
    return filtered_F
def filter_must_have(F, must_have):
    filtered_F = [[] for _ in range(len(F))]
    for level, f_level in enumerate(F):
        for itemset in f_level:
            if any(must in itemset for must in must_have):
                filtered_F[level].append(itemset)
    return filtered_F