import math
from itertools import permutations
def permutate(x, y):
    diff = abs(len(y) - len(x))
    tall = max(len(x), len(y))
    short = min(len(x), len(y))
    return math.factorial(tall)
def appender(matrix, lst, diff):
    return 0
def cost_find(matrix):
    min_cost_row = None
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
        if min_cost_row is None or row[3] < min_cost_row[3]:
            min_cost_row = row
    return min_cost_row
def generate_permutations_with_gaps(seq, num_gaps):
    if num_gaps == 0:
        return [seq]
    permutations_with_gaps = set()
    for positions in permutations(range(len(seq) + num_gaps), num_gaps):
        new_seq = list(seq)
        for pos in sorted(positions):
            new_seq.insert(pos, "-")
        permutations_with_gaps.add(tuple(new_seq))
    return [list(p) for p in permutations_with_gaps]
def opt(x, y):
    x = list(x)
    y = list(y)
    lex, ley = len(x), len(y)
    matrix = []
    if lex > ley:
        matrix = [[x, []] for _ in range(permutate(x, y))]
    elif ley > lex:
        matrix = [[[], y] for _ in range(permutate(x, y))]
    else:
        matrix = [[x, y]]
    shortone = y if lex > ley else x
    diff = abs(lex - ley)
    permutations_with_gaps = generate_permutations_with_gaps(shortone, diff)
    for i in range(len(matrix)):
        if lex > ley:
            matrix[i][1] = permutations_with_gaps[i]
        else:
            matrix[i][0] = permutations_with_gaps[i]
    return cost_find(matrix)
X = "TACAGTTACC"
Y = "TAAGGTCA"
result = opt(X, Y)
print("Edit Distance =", result[3])
for j in range(len(result[0])):
    print(result[0][j], result[1][j], result[2][j])