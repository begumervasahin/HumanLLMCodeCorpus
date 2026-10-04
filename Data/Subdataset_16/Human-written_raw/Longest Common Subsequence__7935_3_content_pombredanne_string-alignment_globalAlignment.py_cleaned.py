def fonk1(s1, s2):
     a1 = 5
     a2 = -4
     a3 = -6
     b1 = len(s2)+1
     b2 = len(s1)+1
     b3 = fonk2(b1, b2, 0)
     b4 = fonk2(b1, b2, "A")
     a4 = 0
     for i in range (0,b2):
          b3[0][i] = a4
          b4[0][i] = "L"
          a4 -= 6
     a4 = -6
     for j in range (1, b1):
          b3[j][0] = a4
          b4[j][0] = "T"
          a4 -= 6
     b4 [0][0] = 'F'
     for b11 in range (1,b1):
          for b10 in range (1,b2):
               b5 = b3[b11-1][b10] + a3
               b6 = b3[b11][b10-1] + a3
               if (s1[b10-1] == s2[b11-1]):
                    b7 = b3[b11-1][b10-1] + a1
               else: b7 = b3[b11-1][b10-1] + a2
               a4 = max(b5,b6,b7)
               b3[b11][b10] = a4
               if (a4 = = b6):
                    b4[b11][b10] = "L"
               elif (a4 = = b7):
                    b4[b11][b10] = "D"
               else:
                    b4[b11][b10] = "T"
     fonk4(b4, s1, s2, "alignment.txt")
     return b3[b1-1][b2-1]
def fonk2(numRows, numCols, value):
     b8 = []
     a5 = 0
     while (a5 < numRows):
          b8.append([])
          a6 = 0
          while (a6 < numCols):
               b8[a5].append(value)
               a6 = a6 + 1
          a5 = a5 + 1
     return b8
def fonk3(b8, filename):
     b9 = open(filename, 'w')
     a5 = len(b8)
     a6 = len(b8[0])
     for b11 in range (0,a5):
          for b10 in range (0,a6):
               b9.write(str(b8[b11][b10]) + "\b16")
          b9.write("\n")
     b9.close()
     return
def fonk4(direction, s1, s2, filename):
     b9 = open(filename, 'w')
     a5 = len(direction)
     a6 = len(direction[0])
     b10 = a6 - 1
     b11 = a5 -  1
     b12 = direction[b11][b10]
     b13 = ""
     b14 = ""
     while b12 != "F":
          if direction[b11][b10] == "T":
               b13 = "-" + b13
               b14 = s2[b11-1] + b14
               b11 -= 1
          elif direction[b11][b10] == "L":
               b13 = s1[b10-1] + b13
               b14 = "-" + b14
               b10 -= 1
          elif direction[b11][b10] == "D":
               b13 = s1[b10-1] + b13
               b14 = s2[b11-1] + b14
               b10-=1
               b11-=1
          b12 = direction[b11][b10]
     for i in range (0, len(b13), 50):
          b9.write(b13[i:i+50] + "\n")
          b9.write(b14[i:i+50] + "\n")
          b9.write("\n")
     b9.close()
     return
b15 = "AGCGTCTA"
b16 = "TGCATCTCG"
b17 = fonk1(b15, b16)
print(b15)
print(b16)
print("Global alignment score: " + str(b17))