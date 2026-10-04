
def get_subsets(pat, sub1, sub2, L, temp, base):
    if L < 1:
        if temp not in sub1:
            temp.sort()
            pat.sort()
            sub1.append(temp)
            sub2.append(pat)
    else:
        for i in range(base, len(pat)):
            get_subsets(pat[:i] + pat[i+1:], sub1, sub2, L-1, temp + [pat[i]], i)
def generate_association_rules(fi, N, min_conf, min_lift):
    rules = []
    fi_num = len(fi)
    fi_dict = {}
    for i in range(fi_num):
        pattern = tuple(sorted(fi[i][:-1]))
        fi_dict[pattern] = fi[i][-1]
    for i in range(fi_num):
        pattern = fi[i][:-1]
        support = fi[i][-1]
        subset_len = int((len(pattern) - 1) / 2)
        sub1, sub2 = [], []
        for j in range(1, subset_len + 1):
            get_subsets(pattern, sub1, sub2, j, [], 0)
        for j in range(len(sub1)):
            if sub1[j] in sub2:
                sub1[j] = [-1, -9]
                sub2[j] = [-2, -5]
            pat1, pat2 = sorted(sub1[j]), sorted(sub2[j])
            if tuple(pat1) in fi_dict and tuple(pat2) in fi_dict:
                sup1, sup2, sup3 = support, fi_dict[tuple(pat1)], fi_dict[tuple(pat2)]
                if (sup1 * N) / (sup2 * sup3) > min_lift:
                    if sup1 / sup2 > min_conf:
                        rules.append([pat1, pat2, sup1, sup1 / sup2, (sup1 * N) / (sup2 * sup3)])
                    if sup1 / sup3 > min_conf:
                        rules.append([pat2, pat1, sup1, sup1 / sup3, (sup1 * N) / (sup2 * sup3)])
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
        print(f"Rule: {rule[0]} -> {rule[1]}, Support: {rule[2]}, Confidence: {rule[3]}, Lift: {rule[4]}")