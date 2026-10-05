'''
Also known as Bucket Sort
Radix sort -- time taken as a function of size, and number of digits
    ==> O(d (n + b)), where b is the base ... 10 for numbers, 26 for alphabets etc.
Find the largest number and then the number of digits in it. Iterating thru that many times
would result in a sorted list.  In each iteration:
   - find the 'i'th value of the every number in the list
    - (e.g. for 1st run, unit digit, for second run the 10s digit, etc
    - place the number in a 'bucket' marked by the position value  [[ for base 10 ... 0 to 9 ]]
    - generate updated list sequentially reading from bucket 0 thru bucket 9.
'''
def radix_sort(A, verbose=0, desc=0):
    import common as c
    def passes(n, b):
        cnt = 0
        while (n):
            cnt += 1
            n = n
        return (cnt)
    def positional_digit(n, pos, b=10):
        cnt, rem, ok = 0, 0, True
        while (ok):
            cnt += 1
            rem = n % b
            n = n
            if (cnt > pos): ok = False
        return (rem)
    def bucketize(pos, b):
        n = len(A)
        B = [[] for i in range(n)]
        for i in range(n):
            bucket = positional_digit(A[i], pos, b)
            B[bucket].append(A[i])
            if(verbose == 2): print("    B:", i, " :: ", B)
        return ([B[x][y] for x in range(len(B)) for y in range(len(B[x]))])
    b = 10
    smallest = c.minimum(A)[0]
    if(smallest): A = [x - smallest for x in A]
    largest = c.maximum(A)[0]
    iter = passes(largest, b)
    for i in range(iter):
        A = bucketize(i, b)
        if(verbose): print("iter
    if (smallest): A = [x + smallest for x in A]
    if(desc): A = A[::-1]
    return (A)