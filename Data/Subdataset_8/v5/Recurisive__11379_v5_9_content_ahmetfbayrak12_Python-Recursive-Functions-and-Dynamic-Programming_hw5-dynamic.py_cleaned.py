import math
def permutate(x, y):
    diff = int(math.fabs(len(y) - len(x)))
    tall = max(len(x), len(y))
    short = min(len(x), len(y))
    return math.factorial(tall) / (math.factorial(diff) * math.factorial(short))
def cost_find(matrix):
    result = matrix[0]
    for i in range(1, len(matrix)):
        if matrix[i][3] < result[3]:
            result = matrix[i]
    return result
def opt(x, y):
    x = list(x)
    y = list(y)
    lex = len(x)
    ley = len(y)
    matrix = []
    permutated = permutate(x, y)
    if lex > ley:
        for i in range(permutated):
            matrix.append([x, []])
    elif ley > lex:
        for i in range(permutated):
            matrix.append([[], y])
    else:
        matrix.append([[], y])
    short_one = y if lex > ley else x
    diff = math.fabs(lex - ley)
    if diff in (1, 2, 3):
        listem = []
        for i in range(len(short_one) + 1):
            if diff == 1:
                listem.append(short_one[:i] + ["-"] + short_one[i:])
            elif diff == 2:
                for j in range(len(short_one) + 1):
                    listem.append(short_one[:i] + ["-"] + short_one[i:j] + ["-"] + short_one[j:])
            elif diff == 3:
                for j in range(len(short_one) + 1):
                    for k in range(len(short_one) + 1):
                        listem.append(short_one[:i] + ["-"] + short_one[i:j] + ["-"] + short_one[j:k] + ["-"] + short_one[k:])
        if lex > ley:
            for i in range(len(matrix)):
                matrix[i][1] = listem[i]
        elif ley > lex:
            for i in range(len(matrix)):
                matrix[i][0] = listem[i]
    return cost_find(matrix)
X = "TACAGTTACC"
Y = "TAAGGTCA"
result = opt(X, Y)
print("Edit Distance =", result[3])
for j in range(len(result[0])):
    print(result[0][j], result[1][j], result[2][j])