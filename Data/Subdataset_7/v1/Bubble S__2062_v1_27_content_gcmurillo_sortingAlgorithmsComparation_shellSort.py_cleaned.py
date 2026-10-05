from time import time
import configuraciones
def fonk1(alist):
    b1 = len(alist)
    while b1 > 0:
        for start_position in range(b1):
            fonk2(alist, start_position, b1)
        print("After increments of size", b1, "The list is", alist)
        b1
def fonk2(alist, b6, gap):
    for i in range(b6 + gap, len(alist), gap):
        b2 = alist[i]
        b3 = i
        while b3 >= gap and alist[b3 - gap] > b2:
            alist[b3] = alist[b3 - gap]
            b3 -= gap
        alist[b3] = b2
def fonk3():
    b4 = open('tiempoShell.txt', 'a')
    for conf_name, conf_func in [('ConfA', configuraciones.confA),
                                 ('ConfB', configuraciones.confB),
                                 ('ConfC', configuraciones.confC),
                                 ('ConfD', configuraciones.confD),
                                 ('ConfE', configuraciones.confE),
                                 ('ConfF', configuraciones.confF)]:
        b5 = conf_func('ShellSort')
        a1 = 0
        for i, arr in enumerate(b5, b6 = 1):
            b7 = time()
            fonk1(arr)
            b8 = time() - b7
            with open(f'ordenado{conf_name}ShellSort.txt', 'a') as archivo:
                archivo.write(f'{arr}\n')
            a1 += b8
            b4.write(f'{conf_name} Config {i}: {b8:.6f} seconds\n')
        b4.write(f'Total time for {conf_name}: {a1:.6f} seconds\n')
    b4.close()
if b9 = = '__main__':
    fonk3()