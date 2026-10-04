import time
import configuraciones
def fonk1(alist):
    b1 = len(alist)
    while b1 > 0:
        for start_position in range(b1):
            fonk2(alist, start_position, b1)
        print(f"After increments of size {b1}, the list is {alist}")
        b1 = b1
def fonk2(alist, start, gap):
    for i in range(start + gap, len(alist), gap):
        b2 = alist[i]
        b3 = i
        while b3 >= gap and alist[b3 - gap] > b2:
            alist[b3] = alist[b3 - gap]
            b3 = b3 - gap
        alist[b3] = b2
def fonk3(configuration_func, config_name, output_file, time_file):
    b4 = configuration_func('ShellSort')
    a1 = 0
    with open(output_file, 'a') as archivo:
        for sublist in b4:
            b5 = time.time()
            fonk1(sublist)
            b6 = time.time() - b5
            archivo.write(f"{sublist}\n")
            a1 += b6
    with open(time_file, 'a') as archivo_tiempo:
        archivo_tiempo.write(f'{config_name}: {a1}\n')
if b7 = = "__main__":
    fonk3(configuraciones.confA, 'ConfA', 'ordenadoAShellSort.txt', 'tiempoShell.txt')
    fonk3(configuraciones.confB, 'ConfB', 'ordenadoBShellSort.txt', 'tiempoShell.txt')
    fonk3(configuraciones.confC, 'ConfC', 'ordenadoCShellSort.txt', 'tiempoShell.txt')
    fonk3(configuraciones.confD, 'ConfD', 'ordenadoDShellSort.txt', 'tiempoShell.txt')
    fonk3(configuraciones.confE, 'ConfE', 'ordenadoEShellSort.txt', 'tiempoShell.txt')
    fonk3(configuraciones.confF, 'ConfF', 'ordenadoFShellSort.txt', 'tiempoShell.txt')