
def fonk1(a):
  b1 = []
  b2 = list(a)
  while(len(b2) > 0):
    b3 = b2[0]
    for x in b2:
      if(x < b3):
        b3 = x
    b1.append(b3)
    b2.remove(b3)
  return b1