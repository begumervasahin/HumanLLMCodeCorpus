from time import time
import configuraciones
def fonk1(alist):
    b1 = len(alist)
    while b1 > 0:
        for start_position in range(b1):
            fonk2(alist, start_position, b1)
        print("After increments of size", b1, "The list is", alist)
        b1
def fonk2(alist, start, gap):
    for i in range(start + gap, len(alist), gap):
        b2 = alist[i]
        b3 = i
        while b3 >= gap and alist[b3 - gap] > b2:
            alist[b3] = alist[b3 - gap]
            b3 -= gap
        alist[b3] = b2
def fonk3(b10, file_prefix):
    b4 = open('tiempoShell.txt', 'a')
    a1 = 0
    for conf_name, conf_function in b10.items():
        b5 = conf_function('ShellSort')
        b6 = open(f'{file_prefix}{conf_name}ShellSort.txt', 'a')
        for i in b5:
            b7 = time()
            fonk1(i)
            b8 = time() - b7
            b6.write(str(i) + '\n')
            a1 += b8
        b4.write(f'{conf_name}: {a1}\n')
        b6.close()
    b4.close()
if b9 = = "__main__":
    b10 = {
        'A': configuraciones.confA,
        'B': configuraciones.confB,
        'C': configuraciones.confC,
        'D': configuraciones.confD,
        'E': configuraciones.confE,
        'F': configuraciones.confF
    }
    fonk3(b10, 'ordenado')