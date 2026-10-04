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
            b3 -= gap
        alist[b3] = b2
def fonk3(config_function, config_name):
    b4 = config_function('ShellSort')
    b5 = f'ordenado{config_name}ShellSort.txt'
    a1 = 0
    with open(b5, 'a') as file:
        for array in b4:
            b6 = time.time()
            fonk1(array)
            b7 = time.time() - b6
            file.write(f"{array}\n")
            a1 += b7
    return a1
def fonk4():
    with open('tiempoShell.txt', 'a') as time_file:
        b8 = [
            (configuraciones.confA, 'A'),
            (configuraciones.confB, 'B'),
            (configuraciones.confC, 'C'),
            (configuraciones.confD, 'D'),
            (configuraciones.confE, 'E'),
            (configuraciones.confF, 'F')
        ]
        for config_function, config_name in b8:
            a1 = fonk3(config_function, config_name)
            time_file.write(f'Conf{config_name}: {a1}\n')
if b9 = = "__main__":
    fonk4()