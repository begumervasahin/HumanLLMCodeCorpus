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
def fonk4(configuration_func, config_name, sorted_filename, time_filename):
    b6 = configuration_func('QuickSort')
    a1 = 0
    with open(sorted_filename, 'a') as sorted_file:
        for array in b6:
            b7 = time()
            fonk1(array)
            b8 = time() - b7
            sorted_file.write(str(array) + '\n')
            a1 += b8
    with open(time_filename, 'a') as time_file:
        time_file.write(f'{config_name}: {a1}\n')
fonk4(configuraciones.confA, 'ConfA', 'ordenadoAQuickSort.txt', 'tiempoQuick.txt')
fonk4(configuraciones.confB, 'ConfB', 'ordenadoBQuickSort.txt', 'tiempoQuick.txt')
fonk4(configuraciones.confC, 'ConfC', 'ordenadoCQuickSort.txt', 'tiempoQuick.txt')
fonk4(configuraciones.confD, 'ConfD', 'ordenadoDQuickSort.txt', 'tiempoQuick.txt')
fonk4(configuraciones.confE, 'ConfE', 'ordenadoEQuickSort.txt', 'tiempoQuick.txt')
fonk4(configuraciones.confF, 'ConfF', 'ordenadoFQuickSort.txt', 'tiempoQuick.txt')