'''
Counting sort -- time taken as a function of size  ==> size & list range  i.e. O(n + k)
Find the range of the numbers ... largest - smallest.
Normalize the data, by shifting the smallest number to 0.
create a list (count) based on frequency of occurances of the numbers.
update the list (count) as cumulative. (i.e. A[x] += A[x-1] where x=1..n-1
scan original list right to left; from it, get key of count list, decrement count index ...
update output list with key at index provided by count
'''
def counting_sort(A, verbose=0, desc=0):
    import common as c
    largest = c.maximum(A)[0]
    smallest = c.minimum(A)[0]
    if(smallest):
        A = [x-smallest for x in A]
    if(verbose): print("normalized = ", A)
    count = [0 for x in range(largest - smallest + 1)]
    n = len(A)
    for i in range(n):
        count[A[i]] += 1
    for i in range(1, len(count)):
        count[i] += count[i-1]
        if(verbose == 2): print("  sub: ", i, " :: ", count[i], count[i-1])
    B = [0 for x in range(n)]
    for i in range(n-1, -1, -1):
        count[A[i]] -= 1
        B[count[A[i]]] = A[i]
        if(verbose): print("iter
    if(smallest):
        B = [x + smallest for x in B]
    if(desc): B = B[::-1]
    return(B)