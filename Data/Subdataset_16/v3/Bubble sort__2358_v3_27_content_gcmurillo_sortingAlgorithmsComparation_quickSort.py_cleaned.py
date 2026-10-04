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
def fonk4(conf_function, output_file_prefix):
    b6 = conf_function('QuickSort')
    a1 = 0
    b7 = f'{output_file_prefix}.txt'
    b8 = 'tiempoQuick.txt'
    with open(b7, 'a') as result_file, open(b8, 'a') as time_file:
        for array in b6:
            b9 = time()
            fonk1(array)
            b10 = time() - b9
            result_file.write(str(array) + '\n')
            a1 += b10
        time_file.write(f'{output_file_prefix}: {a1}\n')
def fonk5():
    b11 = [
        (configuraciones.confA, 'ordenadoAQuickSort'),
        (configuraciones.confB, 'ordenadoBQuickSort'),
        (configuraciones.confC, 'ordenadoCQuickSort'),
        (configuraciones.confD, 'ordenadoDQuickSort'),
        (configuraciones.confE, 'ordenadoEQuickSort'),
        (configuraciones.confF, 'ordenadoFQuickSort')
    ]
    for conf_function, output_file_prefix in b11:
        fonk4(conf_function, output_file_prefix)
if b12 = = "__main__":
    fonk5()