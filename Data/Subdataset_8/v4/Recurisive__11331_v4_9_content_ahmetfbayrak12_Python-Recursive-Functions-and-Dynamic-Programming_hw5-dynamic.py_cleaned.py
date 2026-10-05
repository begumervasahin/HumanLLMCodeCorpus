import math
def permutate(x, y):
    diff = int(math.fabs(len(y) - len(x)))
    tall = max(len(x), len(y))
    short = min(len(x), len(y))
    return (math.factorial(tall)) / (math.factorial(diff) * math.factorial(short))
def appender(matrix, liste, diff):
    return 0
def cost_find(matrix):
    for i in range(len(matrix)):
        cost = 0
        matrix[i].append([])
        for j in range(len(matrix[i][0])):
            if matrix[i][0][j] == matrix[i][1][j]:
                cost += 0
                matrix[i][2].append(0)
            elif matrix[i][0][j] == "-" or matrix[i][1][j] == "-":
                cost += 2
                matrix[i][2].append(2)
            else:
                cost += 1
                matrix[i][2].append(1)
        matrix[i].append(cost)
        try:
            if matrix[i][3] < result[3]:
                result = matrix[i]
        except UnboundLocalError:
            result = matrix[i]
    return result
def opt(x, y):
    x = list(x)
    y = list(y)
    lex = len(x)
    ley = len(y)
    length = max(lex, ley)
    matrix = []
    permutated = permutate(x, y)
    if lex > ley:
        for i in range(permutated):
            matrix.append([])
            matrix[i].append(x)
            matrix[i].append([])
    elif ley > lex:
        for i in range(permutated):
            matrix.append([])
            matrix[i].append([])
            matrix[i].append(y)
    else:
        matrix.append([])
        matrix[i].append([])
        matrix[i].append(y)
    short_one = list()
    diff = math.fabs(lex - ley)
    if lex > ley:
        short_one = y
    elif ley > lex:
        short_one = x
    if diff == 1:
        listem = []
        for i in range(len(short_one) + 1):
            listem.append(short_one[:1] + ["-"] + short_one[i:1])
        if lex > ley:
            for i in range(len(matrix)):
                matrix[i][0] = listem[i]
        elif ley > lex:
            for i in range(len(matrix)):
                matrix[i][0] = listem[i]
    elif diff == 2:
        listem = []
        for i in range(len(short_one) + 1):
            listem.append(short_one[:i] + ["-"] + short_one[i:])
        listem2 = []
        for i in listem:
            for j in range(len(short_one) + 1):
                t = i[:j] + ["-"] + i[j:]
                if t not in listem2:
                    listem2.append(t)
        if lex > ley:
            for i in range(len(matrix)):
                matrix[i][1] = listem2[i]
        elif ley > lex:
            for i in range(len(matrix)):
                matrix[i][0] = listem2[i]
    elif diff == 3:
        listem = []
        for i in range(len(short_one) + 1):
            listem.append(short_one[:i] + "-" + short_one[i:])
        listem2 = []
        for i in listem2:
            for j in range(len(short_one) +1):
                t = i[:j] + ["-"] + i[j:]
                if t not in listem2:
                    listem2.append(t)
        listem3 = []
        for i in listem2:
            for j in range(len(short_one) + 1):
                t = i[:j] + ["-"] + i[j:]
                if t not in listem3:
                    listem3.append(t)
        if lex > ley:
            for i in range(len(matrix)):
                matrix[i][1] = listem3[i]
        elif ley > lex:
            for i in range(len(matrix)):
                matrix[i][0] = listem3[i]
    return cost_find(matrix)
X = "TACAGTTACC"
Y = "TAAGGTCA"
result = opt(X, Y)
print("Edit Distance = " + str(result[3]))
for j in range(len(result[0])):
    print(result[0][j] + " " + result[1][j] + " " + str(result[2][j])))