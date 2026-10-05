
def fonk1(b8):
  if len(b8) < 2:
    return b8
  b1 = [None for _ in range(len(b8))]
  b2 = [None for _ in range(len(b8))]
  a1 = 1
  b1[0] = 0
  b3 = []
  for i in range(1,len(b8)):
    if b8[i] > b8[b1[a1-1]]:
      b4 = a1
    else:
      a2 = 0
      b5 = a1-1
      while a2+1<b5:
        b6 = (a2+b5)
        if b8[i]>b8[b1[b6]]:
          a2 = b6+1
        else:
          b5 = b6
      b4 = a2
    b2[i]=b1[b4-1]
    b1[b4]=i
    a1 = max(a1,b4+1)
  b7 = b1[a1-1]
  for _ in range(a1):
    b3.append(b8[b7])
    b7 = b2[b7]
  return b3[::-1]
b8 = [30,10,20,50,40,60]
print(fonk1(b8))
def fonk2(b8):
  b9 = [[] for _ in range(len(b8))]
  b10 = []
  for i in range(len(b8)):
    b11 = False
    for b4 in range(i):
      if b8[i] > b9[b4][-1]:
        b11 = True
        b9[i] = b9[b4] + [b8[i]]
        b10 = max(b9[i], b10, key=len)
    if b11 is False:
      b9[i].append(b8[i])
  return b10
print(fonk2([80,90,91,81,82,83,74,85]))