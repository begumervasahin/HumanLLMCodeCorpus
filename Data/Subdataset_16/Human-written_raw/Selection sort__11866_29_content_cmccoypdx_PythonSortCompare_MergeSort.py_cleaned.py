def fonk1(b5, b3, b4):
  b1 = j = n = 0
  while(b1 < len(b3) and j < len(b4)):
    if(b3[b1] < b4[j]):
      b5[n] = b3[b1]
      b1 += 1
    else:
      b5[n] = b4[j]
      j += 1
    n += 1
  while(b1 < len(b3)):
    b5[n] = b3[b1]
    b1 += 1
    n += 1
  while(j < len(b4)):
    b5[n] = b4[j]
    j += 1
    n += 1
  return b5
def fonk2(b5):
  if len(b5) > 1:
    b2 = len(b5)
    b3 = b5[:b2]
    b4 = b5[b2:]
    fonk2(b3)
    fonk2(b4)
    b5 = fonk1(b5, b3, b4)