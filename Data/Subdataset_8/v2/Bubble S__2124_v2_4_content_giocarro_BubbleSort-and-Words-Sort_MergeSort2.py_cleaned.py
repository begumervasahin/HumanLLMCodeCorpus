
a = [0, 9, 1, 4, 6, 7, 2, 1, 8, 7, 7, 4, 3, 5, 6, 1, 7, 8, 0, 3]
l = len(a)
x = 0
li = l
while li % 2 == 0:
    li = li / 2
    x = x + 1
p = 2 ** x
tamis = l / p
inters = l / tamis
print('Number of intervals =', inters, '\nInterval size =', tamis, '\nLength of list =', l, '\nList:', a)
s = 0
g = 1
for h in range(s, l, int(tamis)):
    for k in range(s, g * li - 1):
        b = []
        n = 0
        m = 0
        for i in range(s, g * li - 1):
            for j in range(s, g * li):
                if i >= n:
                    if i < j:
                        if a[i] <= a[j]:
                            b.append(a[i])
                            n = j
                            if j == li - 1:
                                b.append(a[j])
                            else:
                                break
                        else:
                            b.append(a[j])
                            if j == li - 1:
                                m = m + 1
                                b.append(a[i])
                                break
                else:
                    break
            if m > 0:
                break
        a = list(b)
    g = g + 1
    s = s + li