import sys
import pandas as pd
def intersect(l1, l2):
    return list(set(l1) & set(l2))
def issubset(subset, superset):
    return all(elem in superset for elem in subset)
def diff(l1, l2):
    return list(set(l1) - set(l2))
def eclat(P, minsupport, F, frequent_sets):
    if len(P) == 1:
        frequent_sets.append(P[0])
    for i in range(len(P)):
        F.append(P[i])
        Pa = []
        for j in range(i + 1, len(P)):
            Xab = list(set(P[i][0] + P[j][0]))
            Tab = intersect(P[i][1], P[j][1])
            if len(Tab) >= minsupport:
                Pa.append((Xab, Tab, len(Xab)))
        if Pa:
            eclat(Pa, minsupport, F, frequent_sets)
        else:
            if len(P) != 1:
                frequent_sets.append(P[i])
def declat(Q, minsupport, IF, infrequent_sets):
    if len(Q) == 1:
        infrequent_sets.append(Q[0])
    for i in range(len(Q)):
        IF.append(Q[i])
        Qa = []
        for j in range(i + 1, len(Q)):
            Xab = list(set(Q[i][0] + Q[j][0]))
            Dab = diff(Q[j][2], Q[i][2])
            Sab = Q[i][1] - len(Dab)
            if Sab >= minsupport:
                Qa.append((Xab, Sab, Dab, len(Xab)))
        if Qa:
            declat(Qa, minsupport, IF, infrequent_sets)
        else:
            if len(Q) != 1:
                infrequent_sets.append(Q[i])
def load_database(file_path):
    database = pd.read_csv(file_path, header=None)
    itemsets = ["TID"] + [f"i{col}" for col in range(1, len(database.columns))]
    database.columns = itemsets
    return database, itemsets
def generate_initial_sets(database, itemsets, minsupport):
    P, Q = [], []
    row_count = database["TID"].count()
    T = list(range(1, row_count + 1))
    database.drop(columns=["TID"], inplace=True)
    itemsets.remove("TID")
    for col_name in itemsets:
        tmp = [index + 1 for index in range(row_count) if database[col_name][index] == 1]
        diff_index = diff(T, tmp)
        if len(tmp) >= minsupport:
            P.append((col_name, tmp, 1))
            Q.append((col_name, len(tmp), diff_index, 1))
    return P, Q
def main():
    minsupport = int(input('Enter minsupport: '))
    database, itemsets = load_database('./db.csv')
    P, Q = generate_initial_sets(database, itemsets, minsupport)
    print("\nECLAT Algorithm")
    F, frequent_sets = [], []
    eclat(P, minsupport, F, frequent_sets)
    frequent_sets = sorted(frequent_sets, key=lambda x: x[2], reverse=True)
    print("Frequent Itemsets || Transaction IDs where present")
    for itemset, transactions, _ in frequent_sets:
        print(''.join(itemset), "=>", transactions)
    print("\nMaximal Frequent Sets || Transaction IDs where present")
    maximal_frequent_sets = [f for f in frequent_sets if all(not issubset(f[0], m[0]) for m in frequent_sets if m != f)]
    for itemset, transactions, _ in maximal_frequent_sets:
        print(''.join(itemset), "=>", transactions)
    print("\nDECLAT Algorithm")
    IF, infrequent_sets = [], []
    declat(Q, minsupport, IF, infrequent_sets)
    infrequent_sets = sorted(infrequent_sets, key=lambda x: x[3], reverse=True)
    print("Infrequent Itemsets || Support of Itemsets")
    for itemset, support, _, _ in infrequent_sets:
        print(''.join(itemset), "=>", support)
    print("\nMaximal Infrequent Sets || Transaction IDs where present")
    maximal_infrequent_sets = [f for f in infrequent_sets if all(not issubset(f[0], m[0]) for m in infrequent_sets if m != f)]
    for itemset, support, _, _ in maximal_infrequent_sets:
        print(''.join(itemset), "=>", support)
if __name__ == '__main__':
    main()