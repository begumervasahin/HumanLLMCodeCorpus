def longest_increasing_subsequence_n_log_n(arr):
    if len(arr) < 2:
        return arr
    M = [None] * len(arr)
    P = [None] * len(arr)
    L = 1
    results = []
    M[0] = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[M[L - 1]]:
            j = L
        else:
            lo, hi = 0, L - 1
            while lo + 1 < hi:
                mid = (lo + hi)
                if arr[i] > arr[M[mid]]:
                    lo = mid + 1
                else:
                    hi = mid
            j = lo
        P[i] = M[j - 1]
        M[j] = i
        L = max(L, j + 1)
    k = M[L - 1]
    for _ in range(L):
        results.append(arr[k])
        k = P[k]
    return results[::-1]
def longest_increasing_subsequence_n_square(arr):
    mem = [[] for _ in range(len(arr))]
    best = []
    for i in range(len(arr)):
        for j in range(i):
            if arr[i] > mem[j][-1]:
                mem[i] = mem[j] + [arr[i]]
                best = max(mem[i], best, key=len)
        if not mem[i]:
            mem[i].append(arr[i])
    return best
arr1 = [30, 10, 20, 50, 40, 60]
arr2 = [80, 90, 91, 81, 82, 83, 74, 85]
print("Longest increasing subsequence (O(n log n)): ", longest_increasing_subsequence_n_log_n(arr1))
print("Longest increasing subsequence (O(n^2)): ", longest_increasing_subsequence_n_square(arr2))