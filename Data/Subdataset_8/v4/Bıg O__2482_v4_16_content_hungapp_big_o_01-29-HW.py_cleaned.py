
na, nb = map(int, input().split())
k, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
if a[k - 1] < b[-m]:
    print("YES")
else:
    print("NO")
a = []
b = []
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)
answer = -1
min_value, max_value = min(a), max(b)
for i in range(n):
    if a[i] == min_value and b[i] == max_value:
        answer = i + 1
        break
print(answer)
n = int(input())
a = []
b = []
for i in range(n):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)
final_1 = [False] * n
final_2 = [False] * n
i = j = 0
chosen = 0
while chosen < n:
    if a[i] < b[j]:
        final_1[i] = True
        i += 1
        chosen += 1
    else:
        final_2[j] = True
        j += 1
        chosen += 1
for i in range(n):
    if final_1[i] or i < n
        print(1, end='')
    else:
        print(0, end='')
print()
for i in range(n):
    if final_2[i] or i < n
        print(1, end='')
    else:
        print(0, end='')
n, m = map(int, input().split())
a = list(map(int, input().split()))
count = [0] * (m + 1)
for genre in a:
    count[genre] += 1
ways = 0
for i in range(1, m):
    for j in range(i + 1, m + 1):
        ways += count[i] * count[j]
print(ways)