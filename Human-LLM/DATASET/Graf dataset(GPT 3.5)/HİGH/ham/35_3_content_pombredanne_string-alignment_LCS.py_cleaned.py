def fonk1(s1, s2):
     b1 = len(s2)+1
     b2 = len(s1)+1
     b3 = fonk2(b1, b2, 0)
     b4 = fonk2(b1, b2, "A")
     for i in range (0,b2):
          b3[0][i] = 0
          b4[0][i] = "F"
     for j in range (1, b1):
          b3[j][0] = 0
          b4[j][0] = "F"
     a1 = 0
     a2 = 0
     a3 = 0
     for b12 in range (1,b1):
          for b11 in range (1,b2):
               b5 = b3[b12-1][b11]
               b6 = b3[b12][b11-1]
               if (s1[b11-1] == s2[b12-1]):
                    b7 = b3[b12-1][b11-1] + 1
               else:
                    b7 = -1
               b8 = max(b5, b6, b7)
               b3[b12][b11] = b8
               if (b8 > a3):
                    a3 = b8
                    a1 = b12
                    a2 = b11
               if (b8 = = b6):
                    b4[b12][b11] = "L"
               elif (b8 = = b7):
                    b4[b12][b11] = "D"
               else:
                    b4[b12][b11] = "T"
     fonk3(b3, "b3.txt")
     fonk3(b4, "b4.txt")
     fonk4(b4, s1, s2, a1, a2, "alignment.txt")
     return b3[a1][a2]
def fonk2(numRows, numCols, value):
     b9 = []
     a4 = 0
     while (a4 < numRows):
          b9.append([])
          a5 = 0
          while (a5 < numCols):
               b9[a4].append(value)
               a5 = a5 + 1
          a4 = a4 + 1
     return b9
def fonk3(b9, filename):
     b10 = open(filename, 'w')
     a4 = len(b9)
     a5 = len(b9[0])
     for b12 in range (0,a4):
          for b11 in range (0,a5):
               b10.write(str(b9[b12][b11]) + "\b16")
          b10.write("\n")
     b10.close()
     return
def fonk4(direction, s1, s2, a4, a5, filename):
     b10 = open(filename, 'w')
     b11 = a5
     b12 = a4
     b13 = direction[b12][b11]
     b14 = ""
     while b13 != "F":
          if direction[b12][b11] == "T":
               b12 -= 1
          elif direction[b12][b11] == "L":
               b11 -= 1
          elif direction[b12][b11] == "D":
               b14 = s1[b11-1] + b14
               b11-=1
               b12-=1
          b13 = direction[b12][b11]
     for i in range (0, len(b14), 50):
          b10.write(b14[i:i+50] + "\n")
     b10.close()
     return
b15 = "AGCGTCTA"
b16 = "TGCATCTCG"
b17 = fonk1(b15, b16)
print(b15)
print(b16)
print("LCS Score: " + str(b17))