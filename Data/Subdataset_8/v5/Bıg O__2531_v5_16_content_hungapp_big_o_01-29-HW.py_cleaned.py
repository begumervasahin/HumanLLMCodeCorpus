def check_condition(a, b, k, m):
    if a[k - 1] < b[-m]:
        return "YES"
    else:
        return "NO"
def find_min_a_max_b_index(a, b):
    min_value, max_value = min(a), max(b)
    for i, (x, y) in enumerate(zip(a, b)):
        if x == min_value and y == max_value:
            return i + 1
    return -1
def calculate_final_lists(a, b):
    n = len(a)
    final_1 = [False] * n
    final_2 = [False] * n
    i = j = 0
    chosen = 0
    while chosen < n:
        if a[i] < b[j]:
            final_1[i] = True
            i += 1
        else:
            final_2[j] = True
            j += 1
        chosen += 1
    return final_1, final_2
def print_final_lists(final_1, final_2, n):
    for i in range(n):
        print(1 if final_1[i] or i < n
    print()
    for i in range(n):
        print(1 if final_2[i] or i < n
def calculate_ways(n, m, a):
    count = [0] * (m + 1)
    for genre in a:
        count[genre] += 1
    ways = 0
    for i in range(1, m):
        for j in range(i + 1, m + 1):
            ways += count[i] * count[j]
    return ways
na, nb = map(int, input().split())
k, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(check_condition(a, b, k, m))
print(find_min_a_max_b_index(a, b))
final_1, final_2 = calculate_final_lists(a, b)
print_final_lists(final_1, final_2, na)
n, m = map(int, input().split())
a = list(map(int, input().split()))
print(calculate_ways(n, m, a))