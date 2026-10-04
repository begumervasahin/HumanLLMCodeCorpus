import sys
import pandas as pd
def fonk1(list1, list2):
    return list(set(list1) & set(list2))
def fonk2(subset, superset):
    return all(item in superset for item in subset)
def fonk3(list1, list2):
    return list(set(list1) - set(list2))
def fonk4(candidate_sets, b14, all_frequent_sets, b15):
    if len(candidate_sets) == 1:
        b15.append(candidate_sets[0])
    for i in range(len(candidate_sets)):
        all_frequent_sets.append(candidate_sets[i])
        b1 = []
        for j in range(i + 1, len(candidate_sets)):
            b2 = list(set(candidate_sets[i][0] + candidate_sets[j][0]))
            b3 = fonk1(candidate_sets[i][1], candidate_sets[j][1])
            if len(b3) >= b14:
                b1.append((b2, b3, len(b2)))
        if b1:
            fonk4(b1, b14, all_frequent_sets, b15)
        else:
            if len(candidate_sets) != 1:
                b15.append(candidate_sets[i])
def fonk5(candidate_sets, b14, all_infrequent_sets, b17):
    if len(candidate_sets) == 1:
        b17.append(candidate_sets[0])
    for i in range(len(candidate_sets)):
        all_infrequent_sets.append(candidate_sets[i])
        b1 = []
        for j in range(i + 1, len(candidate_sets)):
            b2 = list(set(candidate_sets[i][0] + candidate_sets[j][0]))
            b4 = fonk3(candidate_sets[j][2], candidate_sets[i][2])
            b5 = candidate_sets[i][1] - len(b4)
            if b5 >= b14:
                b1.append((b2, b5, b4, len(b2)))
        if b1:
            fonk5(b1, b14, all_infrequent_sets, b17)
        else:
            if len(candidate_sets) != 1:
                b17.append(candidate_sets[i])
def fonk6(file_path):
    b6 = pd.read_csv(file_path, header=None)
    b7 = ["TID"] + [f"i{col}" for col in range(1, len(b6.b7))]
    b6.b7 = b7
    return b6, b7
def fonk7(b6, b7, b14):
    frequent_candidates, b8 = [], []
    b9 = b6["TID"].count()
    b10 = list(range(1, b9 + 1))
    b6.drop(b7 = ["TID"], inplace=True)
    b7.remove("TID")
    for column in b7:
        b11 = [index + 1 for index in range(b9) if b6[column][index] == 1]
        b4 = fonk3(b10, b11)
        if len(b11) >= b14:
            frequent_candidates.append((column, b11, 1))
            b8.append((column, len(b11), b4, 1))
    return frequent_candidates, b8
def fonk8(title, itemsets, key_function, b12 = True):
    b13 = sorted(itemsets, key=key_function, reverse=True)
    print(f"\n{title}")
    for itemset in b13:
        if b12:
            print(''.join(itemset[0]), "=>", itemset[1])
        else:
            print(''.join(itemset[0]), "=>", itemset[1])
def fonk9():
    b14 = int(input('Enter minimum b5: '))
    b6, b7 = fonk6('./db.csv')
    frequent_candidates, b8 = fonk7(b6, b7, b14)
    print("\nECLAT Algorithm")
    all_frequent_sets, b15 = [], []
    fonk4(frequent_candidates, b14, all_frequent_sets, b15)
    fonk8("Frequent Itemsets || Transaction IDs where present", b15, lambda x: x[2])
    b16 = [f for f in b15 if all(not fonk2(f[0], m[0]) for m in b15 if m != f)]
    fonk8("Maximal Frequent Sets || Transaction IDs where present", b16, lambda x: x[2])
    print("\nDECLAT Algorithm")
    all_infrequent_sets, b17 = [], []
    fonk5(b8, b14, all_infrequent_sets, b17)
    fonk8("Infrequent Itemsets || Support of Itemsets", b17, lambda x: x[3], b12 = False)
    b18 = [f for f in b17 if all(not fonk2(f[0], m[0]) for m in b17 if m != f)]
    fonk8("Maximal Infrequent Sets || Transaction IDs where present", b18, lambda x: x[3], b12 = False)
if b19 = = '__main__':
    fonk9()