import random
def fonk1(a,l,r):
  b1 = a[l]
  b2 = l
  b3 = r + 1
  while(b2 < b3):
    b2 += 1
    b3 -= 1
    while(b2 < len(a) and a[b2] < b1):
      b2 += 1
    while(b3 > 0 and a[b3] > b1):
      b3 -= 1
    if(b2 < len(a) and b3 > 0):
      a[b2], a[b3] = a[b3], a[b2]
  if(b2 < len(a) and b3 > 0):
    a[b2], a[b3] = a[b3], a[b2]
  a[l], a[b3] = a[b3], a[l]
  return b3
def fonk2(a,l,r):
  if(l < r):
    b4 = fonk1(a,l,r)
    fonk2(a,l,b4-1)
    fonk2(a,b4+1,r)
def fonk3(a):
  fonk2(a, 0, len(a)-1)