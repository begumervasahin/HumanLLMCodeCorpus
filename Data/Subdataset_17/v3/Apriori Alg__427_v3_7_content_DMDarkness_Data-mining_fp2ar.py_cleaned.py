
def get_subsets(pat, L, base=0, temp=None):
    if temp is None:
        temp = []
    if L < 1:
        sub1, sub2 = [sorted(temp)], [sorted(pat)]
    else:
        sub1, sub2 = [], []
        for i in range(base, len(pat)):
            t1, t2 = get_subsets(pat[:i] + pat[i+1:], L-1, i, temp + [pat[i]])
            sub1.extend(t1)
            sub2.extend(t2)
    return sub1, sub2
def generate_association_rules(fi, N, min_conf, min_lift):
    rules = []
    fi_dict = {tuple(sorted(itemset[:-1])): itemset[-1] for itemset in fi}
    for itemset in fi:
        pattern = itemset[:-1]
        support = itemset[-1]
        subset_len = int((len(pattern) - 1) / 2)
        for L in range(1, subset_len + 1):
            sub1, sub2 = get_subsets(pattern, L)
            for s1, s2 in zip(sub1, sub2):
                if s1 in sub2:
                    s1, s2 = [-1, -9], [-2, -5]
                pat1, pat2 = tuple(sorted(s1)), tuple(sorted(s2))
                if pat1 in fi_dict and pat2 in fi_dict:
                    sup1, sup2, sup3 = support, fi_dict[pat1], fi_dict[pat2]
                    lift = (sup1 * N) / (sup2 * sup3)
                    conf1, conf2 = sup1 / sup2, sup1 / sup3
                    if lift > min_lift:
                        if conf1 > min_conf:
                            rules.append([list(pat1), list(pat2), sup1, conf1, lift])
                        if conf2 > min_conf:
                            rules.append([list(pat2), list(pat1), sup1, conf2, lift])
    return rules
if __name__ == "__main__":
    frequent_itemsets = [
        [['A'], 0.5],
        [['B'], 0.6],
        [['A', 'B'], 0.3],
        [['A', 'C'], 0.2],
        [['B', 'C'], 0.25],
        [['A', 'B', 'C'], 0.1]
    ]
    total_transactions = 1000
    min_confidence = 0.7
    min_lift = 1.2
    rules = generate_association_rules(frequent_itemsets, total_transactions, min_confidence, min_lift)
    for rule in rules:
        print(f"Rule: {rule[0]} -> {rule[1]}, Support: {rule[2]:.4f}, Confidence: {rule[3]:.4f}, Lift: {rule[4]:.4f}")