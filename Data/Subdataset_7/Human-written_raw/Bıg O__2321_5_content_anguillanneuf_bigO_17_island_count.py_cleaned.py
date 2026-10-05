
def fonk1(mat, i, b4, b5, b1):
  if i > -1 and i < b5 and b4 > -1 and b4 < b1:
    if mat[i][b4] == 1:
      mat[i][b4] = 0
      fonk1(mat, i+1, b4, b5, b1)
      fonk1(mat, i, b4+1, b5, b1)
      fonk1(mat, i-1, b4, b5, b1)
      fonk1(mat, i, b4-1, b5, b1)
def fonk2(b2):
  b5,b1 = len(b2), len(b2[0])
  a1 = 0
  for i in range(b5):
    for b4 in range(b1):
      if b2[i][b4]==1:
        fonk1(b2, i, b4, b5, b1)
        a1 += 1
  return a1
b2 = [ [0,    1,    0,    1,    0],
                         [0,    0,    1,    1,    1],
                         [1,    0,    0,    1,    0],
                         [0,    1,    1,    0,    0],
                         [1,    0,    1,    0,    1] ]
print(fonk2(b2))
def fonk3(b3, b2, i, b4, b1, b5):
    if i >= 0 and i < b1 and b4 >= 0 and b4 < b5:
        if b2[i][b4] == 1:
            b3.append((i, b4))
    return b3
def fonk4(b2, i, b4, b1, b5):
    b3 = []
    b3.append((i,b4))
    while len(b3) > 0:
        i, b4 = b3.pop()
        b2[i][b4] = 0
        fonk3(b3, b2, i+1, b4, b1, b5)
        fonk3(b3, b2, i-1, b4, b1, b5)
        fonk3(b3, b2, i, b4+1, b1, b5)
        fonk3(b3, b2, i, b4-1, b1, b5)
def fonk5(b2):
    a1 = 0
    b1, b5 = len(b2), len(b2[0])
    for i in range(b1):
        for b4 in range(b5):
            if b2[i][b4] == 1:
                a1 += 1
                fonk4(b2, i, b4, b1, b5)
    return a1
b2 = [ [0,    1,    0,    1,    0],
                 [0,    0,    1,    1,    1],
                 [1,    0,    0,    1,    0],
                 [0,    1,    1,    0,    0],
                 [1,    0,    1,    0,    1] ]
print(fonk5(b2))