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
b4 = configuraciones.confA('ShellSort')
b5 = open('ordenadoAShellSort.txt', 'a')
b6 = open('tiempoShell.txt', 'a')
a1 = 0
for i in b4:
    b7 = time()
    fonk1(i)
    b8 = time() - b7
    b5.write(str(i) + '\n')
    a1 += b8
b6.write('ConfA: ' + str(a1) + '\n')
b5.close()
b4 = configuraciones.confB('ShellSort')
b5 = open('ordenadoBShellSort.txt', 'a')
a1 = 0
for i in b4:
    b7 = time()
    fonk1(i)
    b8 = time() - b7
    b5.write(str(i) + '\n')
    a1 += b8
b6.write('ConfB: ' + str(a1) + '\n')
b5.close()
b4 = configuraciones.confC('ShellSort')
b5 = open('ordenadoCShellSort.txt', 'a')
a1 = 0
for i in b4:
    b7 = time()
    fonk1(i)
    b8 = time() - b7
    b5.write(str(i) + '\n')
    a1 += b8
b6.write('ConfC: ' + str(a1) + '\n')
b5.close()
b4 = configuraciones.confD('ShellSort')
b5 = open('ordenadoDShellSort.txt', 'a')
a1 = 0
for i in b4:
    b7 = time()
    fonk1(i)
    b8 = time() - b7
    b5.write(str(i) + '\n')
    a1 += b8
b6.write('ConfD: ' + str(a1) + '\n')
b5.close()
b4 = configuraciones.confE('ShellSort')
b5 = open('ordenadoEShellSort.txt', 'a')
a1 = 0
for i in b4:
    b7 = time()
    fonk1(i)
    b8 = time() - b7
    b5.write(str(i) + '\n')
    a1 += b8
b6.write('ConfE: ' + str(a1) + '\n')
b5.close()
b4 = configuraciones.confF('ShellSort')
b5 = open('ordenadoFShellSort.txt', 'a')
a1 = 0
for i in b4:
    b7 = time()
    fonk1(i)
    b8 = time() - b7
    b5.write(str(i) + '\n')
    a1 += b8
b6.write('ConfF: ' + str(a1) + '\n')
b5.close()