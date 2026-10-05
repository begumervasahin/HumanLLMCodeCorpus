import math
def permutate(x, y):
    diff = int(math.fabs(len(y) - len(x)))
    tall = max(len(x), len(y))
    short = min(len(x), len(y))
    return (math.factorial(tall))/(math.factorial(diff)*math.factorial(short))
def appender(matris, liste ,diff):
    return 0
def costfind(matris):
    for i in range(len(matris)):
        cost = 0
        matris[i].append([])
        for j in range(len(matris[i][0])):
            if matris[i][0][j] == matris[i][1][j]:
                cost += 0
                matris[i][2].append(0)
            elif matris[i][0][j] == "-" or matris[i][1][j] == "-":
                cost += 2
                matris[i][2].append(2)
            else:
                cost += 1
                matris[i][2].append(1)
        matris[i].append(cost)
    res = matris[0]
    for i in range(1, len(matris)):
        if matris[i][3] < res[3]:
            res = matris[i]
    return res
def opt(x, y):
    x = list(x)
    y = list(y)
    lex = len(x)
    ley = len(y)
    lenght = max(lex, ley)
    matris = []
    permutated = permutate(x, y)
    if len(x) > len(y):
        for i in range(permutated):
            matris.append([])
            matris[i].append(x)
            matris[i].append([])
    elif ley > lex:
        for i in range(permutated):
            matris.append([])
            matris[i].append([])
            matris[i].append(y)
    else:
        matris.append([])
        matris[i].append([])
        matris[i].append(y)
    shortone = list()
    diff = math.fabs(lex - ley)
    if lex > ley:
        shortone = y
    elif ley > lex:
        shortone = x
    if diff == 1:
        listem = []
        for i in range(len(shortone) + 1):
            listem.append(shortone[:1] + ["-"] + shortone[i:1])
        if lex > ley:
            for i in range(len(matris)):
                matris[i][0] = listem[i]
        elif ley > lex:
            for i in range (len(matris)):
                matris[i][0] = listem[i]
    elif diff == 2:
        listem = []
        for i in range(len(shortone) + 1):
            listem.append(shortone[:i] + ["-"] + shortone[i:])
        listem2 = []
        for i in listem:
            for j in range (len(shortone) + 1):
                t = i[:j] + ["-"] + i[j:]
                if t not in listem2:
                    listem2.append(t)
        if lex > ley:
            for i in range(len(matris)):
                matris[i][1] = listem2[i]
        elif ley > lex:
            for i in range(len(matris)):
                matris[i][0] = listem2[i]
    elif diff == 3:
        listem = []
        for i in range(len(shortone) + 1):
            listem.append(shortone[:i] + "-" + shortone[i:])
        listem2 = []
        for i in listem2:
            for j in range(len(shortone) +1):
                t = i[:j] + ["-"] + i[j:]
                if t not in listem2:
                    listem2.append(t)
        listem3 = []
        for i in listem2:
            for j in range(len(shortone) + 1):
                t = i[:j] + ["-"] + i[j:]
                if t not in listem3:
                    listem3.append(t)
        if lex > ley:
            for i in range(len(matris)):
                matris[i][1] = listem3[i]
        elif ley > lex:
            for i in range(len(matris)):
                matris[i][0] = listem3[i]
    return costfind(matris)
X = "TACAGTTACC"
Y = "TAAGGTCA"
result = opt(X, Y)
print("Edit Distance = " + str(result[3]))
for j in range(len(result[0])):
    print(result[0][j] + " " + result[1][j] + " " + str(result[2][j]))