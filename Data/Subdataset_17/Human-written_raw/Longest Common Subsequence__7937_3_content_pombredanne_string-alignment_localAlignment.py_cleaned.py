def localAlignmentScore(s1, s2):
     MATCH = 5
     MISMATCH = -4
     GAP = -6
     NUM_ROWS = len(s2)+1
     NUM_COLS = len(s1)+1
     costs = createTable(NUM_ROWS, NUM_COLS, 0)
     directions = createTable(NUM_ROWS, NUM_COLS, "A")
     for i in range (0,NUM_COLS):
          costs[0][i] = 0
          directions[0][i] = "F"
     for j in range (1, NUM_ROWS):
          costs[j][0] = 0
          directions[j][0] = "F"
     maxValue = 0
     maxRowPos = 0
     maxColPos = 0
     for y in range (1,NUM_ROWS):
          for x in range (1,NUM_COLS):
               valTop = costs[y-1][x] + GAP
               valLeft = costs[y][x-1] + GAP
               if (s1[x-1] == s2[y-1]):
                    valDag = costs[y-1][x-1] + MATCH
               else: valDag = costs[y-1][x-1] + MISMATCH
               val = max(valTop,valLeft,valDag,0)
               if (val > maxValue):
                    maxValue = val
                    maxRowPos = y
                    maxColPos = x
               costs[y][x] = val
               if val == 0:
                    directions[y][x] = "F"
               elif val == valLeft:
                    directions[y][x] = "L"
               elif val == valDag:
                    directions[y][x] = "D"
               else:
                    directions[y][x] = "T"
     printTable(costs, "costs.txt")
     printTable(directions, "directions.txt")
     align(directions, s1, s2, maxRowPos, maxColPos, "alignment.txt")
     return costs[maxRowPos][maxColPos]
def createTable(numRows, numCols, value):
     table = []
     row = 0
     while (row < numRows):
          table.append([])
          col = 0
          while (col < numCols):
               table[row].append(value)
               col = col + 1
          row = row + 1
     return table
def printTable(table, filename):
     file = open(filename, 'w')
     row = len(table)
     col = len(table[0])
     for y in range (0,row):
          for x in range (0,col):
               file.write(str(table[y][x]) + "\t")
          file.write("\n")
     file.close()
     return
def align(direction, s1, s2, row, col, filename):
     file = open(filename, 'w')
     x = col
     y = row
     currentDir = direction[y][x]
     topSeq = ""
     botSeq = ""
     while currentDir != "F":
          if direction[y][x] == "T":
               topSeq = "-" + topSeq
               botSeq =  s2[y-1] + botSeq
               y -= 1
          elif direction[y][x] == "L":
               topSeq = s1[x-1] + topSeq
               botSeq = "-" + botSeq
               x -= 1
          elif direction[y][x] == "D":
               topSeq = s1[x-1] + topSeq
               botSeq = s2[y-1] + botSeq
               x-=1
               y-=1
          currentDir = direction[y][x]
     for i in range (0, len(topSeq), 50):
          file.write(topSeq[i:i+50] + "\n")
          file.write(botSeq[i:i+50] + "\n")
          file.write("\n")
     file.close()
     return
s = "AAGGTATGAATC"
t = "CAGTTGCAA"
optimalScore = localAlignmentScore(s, t)
print(s)
print(t)
print("Local alignment score: " + str(optimalScore))