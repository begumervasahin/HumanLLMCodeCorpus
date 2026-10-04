b1 = [0,2,100,0,120,11]
for countOne in range(0, len(b1) - 1 ):
  b2 = b1[countOne]
  b3 = countOne
  for countTwo in range(countOne + 1,len(b1)):
    if b1[countTwo] > b2:
      b2 = b1[countTwo]
      b3 = countTwo
  if b3 != countOne:
    b4 = b1[countOne]
    b1[countOne] = b2
    b1[b3] = b4
print(b1)