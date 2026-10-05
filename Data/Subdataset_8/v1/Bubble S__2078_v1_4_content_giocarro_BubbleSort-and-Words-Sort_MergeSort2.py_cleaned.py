a = [0, 9, 1, 4, 6, 7, 2, 1, 8, 7, 7, 4, 3, 5, 6, 1, 7, 8, 0, 3]
l = len(a)
li = l
x = 0
while li % 2 == 0:
    li = li / 2
    x = x + 1
p = 2 ** x
tamis = l / p
inters = l / tamis
print('Numero de intervalos =', inters, '\nTamano intervalo =', tamis, '\nLongitud de lista =', l, '\n', a)
s = 0
g = 1
for h in range(s, l, tamis):
    for k in range(s, g * li - 1):
        b = []
        print('b =', b, '\ng =', g)
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
        a = []
        a = list(b)
        print('a =', a, '\nb =', b, '\nk =', k, '\ni =', i, '\nj =', j, '\nh =', h, '\ng * li - 1 =', g * li - 1)
    g = g + 1
    s = s + li