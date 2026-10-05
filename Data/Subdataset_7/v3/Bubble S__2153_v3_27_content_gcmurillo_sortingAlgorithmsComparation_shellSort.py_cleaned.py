from time import time
import configuraciones
def fonk1(arr):
    b1 = len(arr)
    while b1 > 0:
        for start_position in range(b1):
            fonk2(arr, start_position, b1)
        print(f"After increments of size {b1}, The list is {arr}")
        b1
def fonk2(arr, b5, gap):
    for i in range(b5 + gap, len(arr), gap):
        b2 = arr[i]
        b3 = i
        while b3 >= gap and arr[b3 - gap] > b2:
            arr[b3] = arr[b3 - gap]
            b3 -= gap
        arr[b3] = b2
def fonk3():
    b4 = open('tiempoShell.txt', 'a')
    for conf_name, conf_func in [('ConfA', configuraciones.confA),
                                 ('ConfB', configuraciones.confB),
                                 ('ConfC', configuraciones.confC),
                                 ('ConfD', configuraciones.confD),
                                 ('ConfE', configuraciones.confE),
                                 ('ConfF', configuraciones.confF)]:
        a1 = 0
        for i, arr in enumerate(conf_func('ShellSort'), b5 = 1):
            b6 = time()
            fonk1(arr)
            b7 = time() - b6
            with open(f'ordenado{conf_name}ShellSort.txt', 'a') as archivo:
                archivo.write(f'{arr}\n')
            a1 += b7
            b4.write(f'{conf_name} Config {i}: {b7:.6f} seconds\n')
        b4.write(f'Total time for {conf_name}: {a1:.6f} seconds\n')
    b4.close()
if b8 = = '__main__':
    fonk3()