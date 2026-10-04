import math
def permutate(x, y):
    diff = abs(len(y) - len(x))
    tall = max(len(x), len(y))
    short = min(len(x), len(y))
    return math.factorial(tall) / (math.factorial(diff) * math.factorial(short))
def appender(matrix, lst, diff):
    return 0
def cost_find(matrix):
    for row in matrix:
        cost = 0
        row.append([])
        for i in range(len(row[0])):
            if row[0][i] == row[1][i]:
                cost += 0
                row[2].append(0)
            elif row[0][i] == "-" or row[1][i] == "-":
                cost += 2
                row[2].append(2)
            else:
                cost += 1
                row[2].append(1)
        row.append(cost)
        try:
            if row[3] < res[3]:
                res = row
        except UnboundLocalError:
            res = row
    return res
def opt(x, y):
    x = list(x)
    y = list(y)
    lex = len(x)
    ley = len(y)
    length = max(lex, ley)
    matrix = []
    permutated = permutate(x, y)
    if lex > ley:
        for _ in range(permutated):
            matrix.append([x, []])
    elif ley > lex:
        for _ in range(permutated):
            matrix.append([[], y])
    else:
        matrix.append([[], y])
    shortone = y if lex > ley else x
    diff = abs(lex - ley)
    if diff == 1:
        permutations = [shortone[:i] + ["-"] + shortone[i:] for i in range(len(shortone) + 1)]
        for i in range(len(matrix)):
            if lex > ley:
                matrix[i][1] = permutations[i]
            else:
                matrix[i][0] = permutations[i]
    elif diff == 2:
        listem = [shortone[:i] + ["-"] + shortone[i:] for i in range(len(shortone) + 1)]
        listem2 = [i[:j] + ["-"] + i[j:] for i in listem for j in range(len(shortone) + 1) if i[:j] + ["-"] + i[j:] not in listem]
        for i in range(len(matrix)):
            if lex > ley:
                matrix[i][1] = listem2[i]
            else:
                matrix[i][0] = listem2[i]
    elif diff == 3:
        listem = [shortone[:i] + ["-"] + shortone[i:] for i in range(len(shortone) + 1)]
        listem2 = [i[:j] + ["-"] + i[j:] for i in listem for j in range(len(shortone) + 1) if i[:j] + ["-"] + i[j:] not in listem]
        listem3 = [i[:j] + ["-"] + i[j:] for i in listem2 for j in range(len(shortone) + 1) if i[:j] + ["-"] + i[j:] not in listem2]
        for i in range(len(matrix)):
            if lex > ley:
                matrix[i][1] = listem3[i]
            else:
                matrix[i][0] = listem3[i]
    return cost_find(matrix)
X = "TACAGTTACC"
Y = "TAAGGTCA"
result = opt(X, Y)
print("Edit Distance =", result[3])
for j in range(len(result[0])):
    print(result[0][j], result[1][j], result[2][j])