import random
def quicksort(l):
    n = len(l)
    if n > 1:
        pivot_index = random.randint(0,n-1)
        pivot = l[pivot_index]
        print ("Pivoting", l[pivot_index], "in", l)
        left = []
        right = []
        pivot_clones = [pivot]
        for i in range(n):
            if i == pivot_index:
                pass
            elif l[i] < pivot:
               left.append(l[i])
            elif l[i] > pivot:
                right.append(l[i])
            else:
                pivot_clones.append(l[i])
        print ("Left becomes", left, "; right becomes", right)
        return quicksort(left) + pivot_clones + quicksort(right)
    return l
print("Result", quicksort(l))