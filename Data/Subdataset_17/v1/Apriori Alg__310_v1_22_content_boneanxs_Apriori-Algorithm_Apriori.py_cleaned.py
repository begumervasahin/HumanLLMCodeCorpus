import itertools
def getSubSet(S):
    subLens = len(S) - 1
    return [list(i) for i in itertools.combinations(S, subLens)]
def isSubSetExist(tar, L):
    tar_sets = [set(i[0]) for i in tar]
    for i in L:
        for j in tar_sets:
            if j < set(i):
                return 0
    return 1
def Apriori(tar, thr, le):
    curFrequ = {}
    for key in tar.keys():
        items = tar[key]
        for item in items:
            if item not in curFrequ:
                curFrequ[item] = 1
            else:
                curFrequ[item] += 1
    tarLen = len(tar)
    keys = list(curFrequ.keys())
    for key in keys:
        curFrequ[key] = curFrequ[key] / tarLen
        if curFrequ[key] < thr:
            del curFrequ[key]
    curFrequ = [[key, curFrequ[key]] for key in curFrequ]
    if le == 1:
        return curFrequ
    tempLe = 2
    while tempLe <= le:
        tempList = []
        for i in range(len(curFrequ)):
            for j in range(i + 1, len(curFrequ)):
                if tempLe == 2:
                    temp = [curFrequ[i][0], curFrequ[j][0]]
                else:
                    temp = list(set(curFrequ[i][0]) | set(curFrequ[j][0]))
                if len(temp) != tempLe:
                    continue
                temp.sort()
                if isSubSetExist(curFrequ, getSubSet(temp)) == 1:
                    if temp not in tempList:
                        tempList.append(temp)
        curFrequ = []
        for item in tempList:
            tempLen = sum(1 for key in tar if set(item) <= set(tar[key]))
            tempLen /= tarLen
            if tempLen >= thr:
                curFrequ.append([item, tempLen])
        tempLe += 1
    return curFrequ
if __name__ == "__main__":
    transactions = {
        0: ['A', 'B', 'C'],
        1: ['A', 'C'],
        2: ['A', 'D'],
        3: ['B', 'C'],
        4: ['A', 'B', 'C', 'D']
    }
    threshold = 0.5
    max_length = 3
    frequent_itemsets = Apriori(transactions, threshold, max_length)
    print("Frequent Itemsets:")
    for itemset in frequent_itemsets:
        print(f"Itemset: {itemset[0]}, Support: {itemset[1]:.2f}")