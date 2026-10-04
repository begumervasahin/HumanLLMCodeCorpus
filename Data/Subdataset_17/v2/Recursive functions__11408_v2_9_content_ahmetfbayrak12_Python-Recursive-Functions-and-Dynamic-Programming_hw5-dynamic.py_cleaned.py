import math
def permutate(x, y):
    diff = abs(len(y) - len(x))
    tall = max(len(x), len(y))
    short = min(len(x), len(y))
    return math.factorial(tall)
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
            if matrix[i][3] < res[3]:
                res = matrix[i]
        except UnboundLocalError:
            res = matrix[i]
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
        matrix.append([x, y])
    shortone = y if lex > ley else x
    diff = abs(lex - ley)
    combinations = []
    def generate_combinations(lst, diff):
        if diff == 0:
            return [lst]
        combinations = []
        for i in range(len(lst) + 1):
            new_comb = lst[:i] + ["-"] + lst[i:]
            combinations += generate_combinations(new_comb, diff - 1)
        return combinations
    listem = generate_combinations(shortone, diff)
    if lex > ley:
        for i in range(len(matrix)):
            matrix[i][1] = listem[i]
    else:
        for i in range(len(matrix)):
            matrix[i][0] = listem[i]
    return cost_find(matrix)
X = "TACAGTTACC"
Y = "TAAGGTCA"
result = opt(X, Y)
print("Edit Distance =", result[3])
for j in range(len(result[0])):
    print(result[0][j], result[1][j], result[2][j])