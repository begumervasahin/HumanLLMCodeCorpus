
def SSort(a):
  b = []
  c = list(a)
  while(len(c) > 0):
    smallest = c[0]
    for x in c:
      if(x < smallest):
        smallest = x
    b.append(smallest)
    c.remove(smallest)
  return b