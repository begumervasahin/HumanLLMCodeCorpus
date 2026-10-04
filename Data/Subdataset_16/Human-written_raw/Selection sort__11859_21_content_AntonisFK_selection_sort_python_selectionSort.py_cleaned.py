def fonk1(b2):
  for i in xrange(len(b2)):
    b1 = i
    for b in xrange(i+1, len(b2)):
      if b2[b] < b2[b1]:
        b1 = b
    b2[i] , b2[b1] = b2[b1], b2[i]
  print b2
b2 = [5,3,2,10,45,3,1]
fonk1(b2)