from time import time
import configuraciones
def fonk1(alist):
    fonk2(alist, 0, len(alist) - 1)
def fonk2(alist, first, last):
    if first < last:
        b1 = fonk3(alist, first, last)
        fonk2(alist, first, b1 - 1)
        fonk2(alist, b1 + 1, last)
def fonk3(alist, first, last):
    b2 = alist[first]
    b3 = first + 1
    b4 = last
    b5 = False
    while not b5:
        while b3 <= b4 and alist[b3] <= b2:
            b3 += 1
        while alist[b4] >= b2 and b4 >= b3:
            b4 -= 1
        if b4 < b3:
            b5 = True
        else:
            b6 = alist[b3]
            alist[b3] = alist[b4]
            alist[b4] = b6
    b6 = alist[first]
    alist[first] = alist[b4]
    alist[b4] = b6
    return b4
b7 = open('tiempoQuick.txt', 'a')
def fonk4(b12, file_prefix):
    a1 = 0
    for conf_name, conf_func in b12:
        b8 = conf_func('QuickSort')
        b9 = open(f'ordenado{file_prefix}{conf_name}.txt', 'a')
        a2 = 0
        for i in b8:
            b10 = time()
            fonk1(i)
            b11 = time() - b10
            b9.write(str(i) + '\n')
            a2 += b11
        b7.write(f'{conf_name}: {a2}\n')
        b9.close()
        a1 += a2
    return a1
b12 = [
    ('A', configuraciones.confA),
    ('B', configuraciones.confB),
    ('C', configuraciones.confC),
    ('D', configuraciones.confD),
    ('E', configuraciones.confE),
    ('F', configuraciones.confF)
]
b13 = fonk4(b12, 'QuickSort')
b7.write(f'Total Execution Time: {b13}\n')
b7.close()