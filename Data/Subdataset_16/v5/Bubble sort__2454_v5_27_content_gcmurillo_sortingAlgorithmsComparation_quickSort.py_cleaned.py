from time import time
import configuraciones
def fonk1(alist):
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
    fonk2(alist, 0, len(alist) - 1)
def fonk4(configuration_func, config_name, sorted_filename, b10):
    b6 = configuration_func('QuickSort')
    a1 = 0
    with open(sorted_filename, 'a') as sorted_file:
        for array in b6:
            b7 = time()
            fonk1(array)
            b8 = time() - b7
            sorted_file.write(str(array) + '\n')
            a1 += b8
    with open(b10, 'a') as time_file:
        time_file.write(f'{config_name}: {a1}\n')
def fonk5():
    b9 = [
        (configuraciones.confA, 'ConfA', 'ordenadoAQuickSort.txt'),
        (configuraciones.confB, 'ConfB', 'ordenadoBQuickSort.txt'),
        (configuraciones.confC, 'ConfC', 'ordenadoCQuickSort.txt'),
        (configuraciones.confD, 'ConfD', 'ordenadoDQuickSort.txt'),
        (configuraciones.confE, 'ConfE', 'ordenadoEQuickSort.txt'),
        (configuraciones.confF, 'ConfF', 'ordenadoFQuickSort.txt')
    ]
    b10 = 'tiempoQuick.txt'
    for config_func, config_name, sorted_filename in b9:
        fonk4(config_func, config_name, sorted_filename, b10)
if b11 = = "__main__":
    fonk5()