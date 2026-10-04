def fonk1(n):
  b1 = []
  for b2 in range(0, n+1):
    if fonk2(b2):
      b1.append(b2)
  return b1
def fonk2(x):
  if x < 2:
    return False
  for b2 in range(2, x):
    if x % b2 = = 0:
      return False
  return True
if b3 = = '__main__':
  print(fonk1(100))