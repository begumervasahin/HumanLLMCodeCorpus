
def longest_subsequence_Onlogn(arr):
  if len(arr) < 2:
    return arr
  M = [None for _ in range(len(arr))]
  P = [None for _ in range(len(arr))]
  L = 1
  M[0] = 0
  results = []
  for i in range(1,len(arr)):
    if arr[i] > arr[M[L-1]]:
      j = L
    else:
      lo=0
      hi=L-1
      while lo+1<hi:
        mid=(lo+hi)
        if arr[i]>arr[M[mid]]:
          lo=mid+1
        else:
          hi=mid
      j=lo
    P[i]=M[j-1]
    M[j]=i
    L=max(L,j+1)
  k = M[L-1]
  for _ in range(L):
    results.append(arr[k])
    k=P[k]
  return results[::-1]
arr = [30,10,20,50,40,60]
print(longest_subsequence_Onlogn(arr))
def longest_subsequence_On2(arr):
  mem = [[] for _ in range(len(arr))]
  best = []
  for i in range(len(arr)):
    cond = False
    for j in range(i):
      if arr[i] > mem[j][-1]:
        cond = True
        mem[i] = mem[j] + [arr[i]]
        best = max(mem[i], best, key=len)
    if cond is False:
      mem[i].append(arr[i])
  return best
print(longest_subsequence_On2([80,90,91,81,82,83,74,85]))