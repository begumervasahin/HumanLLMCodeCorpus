def localAlignmentScore(s1, s2):
    MATCH = 5
    MISMATCH = -4
    GAP = -6
    NUM_ROWS = len(s2) + 1
    NUM_COLS = len(s1) + 1
    costs = createTable(NUM_ROWS, NUM_COLS, 0)
    directions = createTable(NUM_ROWS, NUM_COLS, "A")
    initializeTables(costs, directions, NUM_ROWS, NUM_COLS)
    maxValue, maxRowPos, maxColPos = fillTables(costs, directions, s1, s2, MATCH, MISMATCH, GAP, NUM_ROWS, NUM_COLS)
    printTable(costs, "costs.txt")
    printTable(directions, "directions.txt")
    align(directions, s1, s2, maxRowPos, maxColPos, "alignment.txt")
    return costs[maxRowPos][maxColPos]
def createTable(numRows, numCols, value):
    return [[value] * numCols for _ in range(numRows)]
def initializeTables(costs, directions, numRows, numCols):
    for i in range(numCols):
        costs[0][i] = 0
        directions[0][i] = "F"
    for j in range(1, numRows):
        costs[j][0] = 0
        directions[j][0] = "F"
def fillTables(costs, directions, s1, s2, match, mismatch, gap, numRows, numCols):
    maxValue = 0
    maxRowPos = 0
    maxColPos = 0
    for y in range(1, numRows):
        for x in range(1, numCols):
            valTop = costs[y-1][x] + gap
            valLeft = costs[y][x-1] + gap
            valDiag = costs[y-1][x-1] + (match if s1[x-1] == s2[y-1] else mismatch)
            val = max(valTop, valLeft, valDiag, 0)
            if val > maxValue:
                maxValue = val
                maxRowPos = y
                maxColPos = x
            costs[y][x] = val
            directions[y][x] = determineDirection(val, valTop, valLeft, valDiag)
    return maxValue, maxRowPos, maxColPos
def determineDirection(val, valTop, valLeft, valDiag):
    if val == 0:
        return "F"
    elif val == valLeft:
        return "L"
    elif val == valDiag:
        return "D"
    else:
        return "T"
def printTable(table, filename):
    with open(filename, 'w') as file:
        for row in table:
            file.write("\t".join(map(str, row)) + "\n")
def align(directions, s1, s2, row, col, filename):
    with open(filename, 'w') as file:
        x, y = col, row
        topSeq, botSeq = "", ""
        while directions[y][x] != "F":
            if directions[y][x] == "T":
                topSeq = "-" + topSeq
                botSeq = s2[y-1] + botSeq
                y -= 1
            elif directions[y][x] == "L":
                topSeq = s1[x-1] + topSeq
                botSeq = "-" + botSeq
                x -= 1
            elif directions[y][x] == "D":
                topSeq = s1[x-1] + topSeq
                botSeq = s2[y-1] + botSeq
                x -= 1
                y -= 1
        for i in range(0, len(topSeq), 50):
            file.write(topSeq[i:i+50] + "\n")
            file.write(botSeq[i:i+50] + "\n")
            file.write("\n")
if __name__ == "__main__":
    s = "AAGGTATGAATC"
    t = "CAGTTGCAA"
    optimalScore = localAlignmentScore(s, t)
    print(s)
    print(t)
    print(f"Local alignment score: {optimalScore}")