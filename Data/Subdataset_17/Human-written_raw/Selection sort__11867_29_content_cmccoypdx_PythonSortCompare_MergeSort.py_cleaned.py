def merge(a, l, r):
  i = j = n = 0
  while(i < len(l) and j < len(r)):
    if(l[i] < r[j]):
      a[n] = l[i]
      i += 1
    else:
      a[n] = r[j]
      j += 1
    n += 1
  while(i < len(l)):
    a[n] = l[i]
    i += 1
    n += 1
  while(j < len(r)):
    a[n] = r[j]
    j += 1
    n += 1
  return a
def MSort(a):
  if len(a) > 1:
    m = len(a)
    l = a[:m]
    r = a[m:]
    MSort(l)
    MSort(r)
    a = merge(a, l, r)