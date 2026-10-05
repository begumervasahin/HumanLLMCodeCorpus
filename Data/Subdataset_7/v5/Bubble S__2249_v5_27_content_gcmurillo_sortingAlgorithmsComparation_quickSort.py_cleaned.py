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
            alist[b3], alist[b4] = alist[b4], alist[b3]
    alist[first], alist[b4] = alist[b4], alist[first]
    return b4
def fonk4(b9, file_prefix):
    a1 = 0
    with open('tiempoQuick.txt', 'a') as archivo_tiempo:
        for conf_name, conf_func in b9:
            b6 = conf_func('QuickSort')
            with open(f'ordenado{file_prefix}{conf_name}.txt', 'a') as archivo:
                a2 = 0
                for i in b6:
                    b7 = time()
                    fonk1(i)
                    b8 = time() - b7
                    archivo.write(str(i) + '\n')
                    a2 += b8
                archivo_tiempo.write(f'{conf_name}: {a2}\n')
                a1 += a2
        archivo_tiempo.write(f'Total Execution Time: {a1}\n')
b9 = [
    ('A', configuraciones.confA),
    ('B', configuraciones.confB),
    ('C', configuraciones.confC),
    ('D', configuraciones.confD),
    ('E', configuraciones.confE),
    ('F', configuraciones.confF)
]
fonk4(b9, 'QuickSort')