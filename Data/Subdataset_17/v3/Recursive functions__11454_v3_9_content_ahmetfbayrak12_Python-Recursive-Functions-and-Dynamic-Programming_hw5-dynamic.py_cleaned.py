import math
def permutate(x, y):
    diff = abs(len(y) - len(x))
    tall = max(len(x), len(y))
    short = min(len(x), len(y))
    return math.factorial(tall)
def generate_combinations(lst, diff):
    if diff == 0:
        return [lst]
    combinations = []
    for i in range(len(lst) + 1):
        new_comb = lst[:i] + ["-"] + lst[i:]
        combinations += generate_combinations(new_comb, diff - 1)
    return combinations
def cost_find(matrix):
    res = None
    for row in matrix:
        cost = 0
        row.append([])
        for a, b in zip(row[0], row[1]):
            if a == b:
                row[2].append(0)
            elif a == "-" or b == "-":
                row[2].append(2)
                cost += 2
            else:
                row[2].append(1)
                cost += 1
        row.append(cost)
        if res is None or cost < res[3]:
            res = row
    return res
def opt(x, y):
    x = list(x)
    y = list(y)
    lex, ley = len(x), len(y)
    length = max(lex, ley)
    matrix = []
    permutated = permutate(x, y)
    shortone = y if lex > ley else x
    diff = abs(lex - ley)
    listem = generate_combinations(shortone, diff)
    if lex > ley:
        for _ in range(permutated):
            matrix.append([x, []])
        for i in range(len(matrix)):
            matrix[i][1] = listem[i]
    elif ley > lex:
        for _ in range(permutated):
            matrix.append([[], y])
        for i in range(len(matrix)):
            matrix[i][0] = listem[i]
    else:
        matrix.append([x, y])
    return cost_find(matrix)
X = "TACAGTTACC"
Y = "TAAGGTCA"
result = opt(X, Y)
print("Edit Distance =", result[3])
for j in range(len(result[0])):
    print(result[0][j], result[1][j], result[2][j])