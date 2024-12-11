from time import *
import configuraciones
def fonk1(alist):
   fonk2(alist,0,len(alist)-1)
def fonk2(alist,first,last):
   if first<last:
       b1 = fonk3(alist,first,last)
       fonk2(alist,first,b1-1)
       fonk2(alist,b1+1,last)
def fonk3(alist,first,last):
   b2 = alist[first]
   b3 = first+1
   b4 = last
   b5 = False
   while not b5:
       while b3 <= b4 and alist[b3] <= b2:
           b3 = b3 + 1
       while alist[b4] >= b2 and b4 >= b3:
           b4 = b4 -1
       if b4 < b3:
           b5 = True
       else:
           b6 = alist[b3]
           alist[b3] = alist[b4]
           alist[b4] = b6
   b6 = alist[first]
   alist[first] = alist[b4]
   alist[b4] = b6
   return b4
b7 = configuraciones.confA('QuickSort')
b8 = open('ordenadoAQuickSort.txt', 'a')
b9 = open('tiempoQuick.txt', 'a')
a1 = 0
for i in b7:
    b10 = time()
    fonk1(i)
    b11 = time() - b10
    b8.write(str(i) + '\n')
    a1 = b11 + a1
b9.write('ConfA: ' + str(a1) + '\n')
b8.close()
b7 = configuraciones.confB('QuickSort')
b8 = open('ordenadoBQuickSort.txt', 'a')
a1 = 0
for i in b7:
    b10 = time()
    fonk1(i)
    b11 = time() - b10
    b8.write(str(i) + '\n')
    a1 = b11 + a1
b9.write('ConfB: ' + str(a1) + '\n')
b8.close()
b7 = configuraciones.confC('QuickSort')
b8 = open('ordenadoCQuickSort.txt', 'a')
a1 = 0
for i in b7:
    b10 = time()
    fonk1(i)
    b11 = time() - b10
    b8.write(str(i) + '\n')
    a1 = b11 + a1
b9.write('ConfC: ' + str(a1) + '\n')
b8.close()
b7 = configuraciones.confD('QuickSort')
b8 = open('ordenadoDQuickSort.txt', 'a')
a1 = 0
for i in b7:
    b10 = time()
    fonk1(i)
    b11 = time() - b10
    b8.write(str(i) + '\n')
    a1 = b11 + a1
b9.write('ConfD: ' + str(a1) + '\n')
b8.close()
b7 = configuraciones.confE('QuickSort')
b8 = open('ordenadoEQuickSort.txt', 'a')
a1 = 0
for i in b7:
    b10 = time()
    fonk1(i)
    b11 = time() - b10
    b8.write(str(i) + '\n')
    a1 = b11 + a1
b9.write('ConfE: ' + str(a1) + '\n')
b8.close()
b7 = configuraciones.confF('QuickSort')
b8 = open('ordenadoFQuickSort.txt', 'a')
a1 = 0
for i in b7:
    b10 = time()
    fonk1(i)
    b11 = time() - b10
    b8.write(str(i) + '\n')
    a1 = b11 + a1
b9.write('ConfF: ' + str(a1) + '\n')
b8.close()