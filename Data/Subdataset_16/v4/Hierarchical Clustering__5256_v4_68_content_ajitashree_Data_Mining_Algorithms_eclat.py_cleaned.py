import sys
import pandas as pd
def fonk1(list1, list2):
    return list(set(list1) & set(list2))
def fonk2(subset, superset):
    return all(item in superset for item in subset)
def fonk3(list1, list2):
    return list(set(list1) - set(list2))
def fonk4(candidate_sets, b15, all_frequent_sets, b16):
    if len(candidate_sets) == 1:
        b16.append(candidate_sets[0])
    for i in range(len(candidate_sets)):
        all_frequent_sets.append(candidate_sets[i])
        b1 = []
        for j in range(i + 1, len(candidate_sets)):
            b2 = list(set(candidate_sets[i][0] + candidate_sets[j][0]))
            b3 = fonk1(candidate_sets[i][1], candidate_sets[j][1])
            if len(b3) >= b15:
                b1.append((b2, b3, len(b2)))
        if b1:
            fonk4(b1, b15, all_frequent_sets, b16)
        else:
            if len(candidate_sets) != 1:
                b16.append(candidate_sets[i])
def fonk5(candidate_sets, b15, all_infrequent_sets, b18):
    if len(candidate_sets) == 1:
        b18.append(candidate_sets[0])
    for i in range(len(candidate_sets)):
        all_infrequent_sets.append(candidate_sets[i])
        b1 = []
        for j in range(i + 1, len(candidate_sets)):
            b2 = list(set(candidate_sets[i][0] + candidate_sets[j][0]))
            b4 = fonk3(candidate_sets[j][2], candidate_sets[i][2])
            b5 = candidate_sets[i][1] - len(b4)
            if b5 >= b15:
                b1.append((b2, b5, b4, len(b2)))
        if b1:
            fonk5(b1, b15, all_infrequent_sets, b18)
        else:
            if len(candidate_sets) != 1:
                b18.append(candidate_sets[i])
def fonk6(file_path):
    b6 = pd.read_csv(file_path, header=None)
    b7 = ["TID"] + [f"i{col}" for col in range(1, len(b6.b8))]
    b6.b8 = b7
    return b6, b7
def fonk7(b6, b7, b15):
    frequent_candidates, b9 = [], []
    b10 = b6["TID"].count()
    b11 = list(range(1, b10 + 1))
    b6.drop(b8 = ["TID"], inplace=True)
    b7.remove("TID")
    for col_name in b7:
        b12 = [index + 1 for index in range(b10) if b6[col_name][index] == 1]
        b4 = fonk3(b11, b12)
        if len(b12) >= b15:
            frequent_candidates.append((col_name, b12, 1))
            b9.append((col_name, len(b12), b4, 1))
    return frequent_candidates, b9
def fonk8(title, b7, key_function, b13 = True):
    b14 = sorted(b7, key=key_function, reverse=True)
    print(f"\n{title}")
    for itemset in b14:
        if b13:
            print(''.join(itemset[0]), "=>", itemset[1])
        else:
            print(''.join(itemset[0]), "=>", itemset[1])
def fonk9():
    b15 = int(input('Enter b15: '))
    b6, b7 = fonk6('./db.csv')
    frequent_candidates, b9 = fonk7(b6, b7, b15)
    print("\nECLAT Algorithm")
    all_frequent_sets, b16 = [], []
    fonk4(frequent_candidates, b15, all_frequent_sets, b16)
    fonk8("Frequent Itemsets || Transaction IDs where present", b16, lambda x: x[2])
    print("\nMaximal Frequent Sets || Transaction IDs where present")
    b17 = [f for f in b16 if all(not fonk2(f[0], m[0]) for m in b16 if m != f)]
    fonk8("Maximal Frequent Sets || Transaction IDs where present", b17, lambda x: x[2])
    print("\nDECLAT Algorithm")
    all_infrequent_sets, b18 = [], []
    fonk5(b9, b15, all_infrequent_sets, b18)
    fonk8("Infrequent Itemsets || Support of Itemsets", b18, lambda x: x[3], b13 = False)
    print("\nMaximal Infrequent Sets || Transaction IDs where present")
    b19 = [f for f in b18 if all(not fonk2(f[0], m[0]) for m in b18 if m != f)]
    fonk8("Maximal Infrequent Sets || Transaction IDs where present", b19, lambda x: x[3], b13 = False)
if b20 = = '__main__':
    fonk9()