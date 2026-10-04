import time
import configuraciones
def fonk1(alist):
    b1 = len(alist)
    while b1 > 0:
        for start_position in range(b1):
            fonk2(alist, start_position, b1)
        print("After increments of size", b1, "The list is", alist)
        b1 = b1
def fonk2(alist, start, gap):
    for i in range(start + gap, len(alist), gap):
        b2 = alist[i]
        b3 = i
        while b3 >= gap and alist[b3 - gap] > b2:
            alist[b3] = alist[b3 - gap]
            b3 = b3 - gap
        alist[b3] = b2
def fonk3(config_function, config_name):
    b4 = config_function('ShellSort')
    b5 = open(f'ordenado{config_name}ShellSort.txt', 'a')
    a1 = 0
    for i in b4:
        b6 = time.time()
        fonk1(i)
        b7 = time.time() - b6
        b5.write(str(i) + '\n')
        a1 += b7
    b5.close()
    return a1
def fonk4():
    b8 = open('tiempoShell.txt', 'a')
    b9 = [
        (configuraciones.confA, 'A'),
        (configuraciones.confB, 'B'),
        (configuraciones.confC, 'C'),
        (configuraciones.confD, 'D'),
        (configuraciones.confE, 'E'),
        (configuraciones.confF, 'F')
    ]
    for config_function, config_name in b9:
        a1 = fonk3(config_function, config_name)
        b8.write(f'Conf{config_name}: {a1}\n')
    b8.close()
if b10 = = "__main__":
    fonk4()