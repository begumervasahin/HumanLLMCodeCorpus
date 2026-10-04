def fonk1(s1, s2):
     a1 = 5
     a2 = -4
     a3 = -6
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
     a4 = 0
     a5 = 0
     a6 = 0
     for b12 in range (1,b1):
          for b11 in range (1,b2):
               b5 = b3[b12-1][b11] + a3
               b6 = b3[b12][b11-1] + a3
               if (s1[b11-1] == s2[b12-1]):
                    b7 = b3[b12-1][b11-1] + a1
               else: b7 = b3[b12-1][b11-1] + a2
               b8 = max(b5,b6,b7,0)
               if (b8 > a4):
                    a4 = b8
                    a5 = b12
                    a6 = b11
               b3[b12][b11] = b8
               if b8 = = 0:
                    b4[b12][b11] = "F"
               elif b8 = = b6:
                    b4[b12][b11] = "L"
               elif b8 = = b7:
                    b4[b12][b11] = "D"
               else:
                    b4[b12][b11] = "T"
     fonk3(b3, "b3.txt")
     fonk3(b4, "b4.txt")
     fonk4(b4, s1, s2, a5, a6, "alignment.txt")
     return b3[a5][a6]
def fonk2(numRows, numCols, value):
     b9 = []
     a7 = 0
     while (a7 < numRows):
          b9.append([])
          a8 = 0
          while (a8 < numCols):
               b9[a7].append(value)
               a8 = a8 + 1
          a7 = a7 + 1
     return b9
def fonk3(b9, filename):
     b10 = open(filename, 'w')
     a7 = len(b9)
     a8 = len(b9[0])
     for b12 in range (0,a7):
          for b11 in range (0,a8):
               b10.write(str(b9[b12][b11]) + "\b17")
          b10.write("\n")
     b10.close()
     return
def fonk4(direction, s1, s2, a7, a8, filename):
     b10 = open(filename, 'w')
     b11 = a8
     b12 = a7
     b13 = direction[b12][b11]
     b14 = ""
     b15 = ""
     while b13 != "F":
          if direction[b12][b11] == "T":
               b14 = "-" + b14
               b15 = s2[b12-1] + b15
               b12 -= 1
          elif direction[b12][b11] == "L":
               b14 = s1[b11-1] + b14
               b15 = "-" + b15
               b11 -= 1
          elif direction[b12][b11] == "D":
               b14 = s1[b11-1] + b14
               b15 = s2[b12-1] + b15
               b11-=1
               b12-=1
          b13 = direction[b12][b11]
     for i in range (0, len(b14), 50):
          b10.write(b14[i:i+50] + "\n")
          b10.write(b15[i:i+50] + "\n")
          b10.write("\n")
     b10.close()
     return
b16 = "AAGGTATGAATC"
b17 = "CAGTTGCAA"
b18 = fonk1(b16, b17)
print(b16)
print(b17)
print("Local alignment score: " + str(b18))