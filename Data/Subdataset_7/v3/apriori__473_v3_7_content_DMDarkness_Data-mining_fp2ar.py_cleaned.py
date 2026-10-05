
def fonk1(b6, b8, b9, length, temp, base):
    if length < 1:
        if b8.count(temp) == 0:
            temp.sort()
            b6.sort()
            b8.append(temp)
            b9.append(b6)
    else:
        for i in range(base, len(b6)):
            fonk1(b6[0:i] + b6[i+1:], b8, b9, length-1, temp + [b6[i]], i)
def fonk2(frequent_itemsets, dataset_size, min_confidence, min_lift):
    b1 = []
    b2 = len(frequent_itemsets)
    b3 = {}
    for i in range(b2):
        b4 = frequent_itemsets[i][0:-1]
        b4.sort()
        b3[tuple(b4)] = frequent_itemsets[i][-1]
    for i in range(b2):
        b5 = int((len(frequent_itemsets[i]) - 1) / 2)
        b6 = frequent_itemsets[i][0:-1]
        b7 = frequent_itemsets[i][-1]
        b8 = []
        b9 = []
        for j in range(1, b5 + 1):
            fonk1(b6, b8, b9, j, [], 0)
        for j in range(len(b8)):
            if b8.count(b9[j]) != 0:
                b8[j] = [-1, -9]
                b9[j] = [-2, -5]
            b10 = b8[j]
            b11 = b9[j]
            b10.sort()
            b11.sort()
            if tuple(b10) in b3 and tuple(b11) in b3:
                b12 = b3[tuple(b10)]
                b13 = b3[tuple(b11)]
                if b7 * dataset_size / (b12 * b13) > min_lift:
                    if b7 / b12 > min_confidence:
                        b14 = [b10, b11, b7, b7 / b12, b7 * dataset_size / (b12 * b13)]
                        b1.append(b14)
                    if b7 / b13 > min_confidence:
                        b14 = [b11, b10, b7, b7 / b13, b7 * dataset_size / (b12 * b13)]
                        b1.append(b14)
    return b1