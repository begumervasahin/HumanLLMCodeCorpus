from time import *
import configuraciones
def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)
def quickSortHelper(alist,first,last):
   if first<last:
       splitpoint = partition(alist,first,last)
       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)
def partition(alist,first,last):
   pivotvalue = alist[first]
   leftmark = first+1
   rightmark = last
   done = False
   while not done:
       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1
       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1
       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp
   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp
   return rightmark
arreglo = configuraciones.confA('QuickSort')
archivo = open('ordenadoAQuickSort.txt', 'a')
archivoTiempo = open('tiempoQuick.txt', 'a')
total = 0
for i in arreglo:
    start_time = time()
    quickSort(i)
    transcurrido = time() - start_time
    archivo.write(str(i) + '\n')
    total = transcurrido + total
archivoTiempo.write('ConfA: ' + str(total) + '\n')
archivo.close()
arreglo = configuraciones.confB('QuickSort')
archivo = open('ordenadoBQuickSort.txt', 'a')
total = 0
for i in arreglo:
    start_time = time()
    quickSort(i)
    transcurrido = time() - start_time
    archivo.write(str(i) + '\n')
    total = transcurrido + total
archivoTiempo.write('ConfB: ' + str(total) + '\n')
archivo.close()
arreglo = configuraciones.confC('QuickSort')
archivo = open('ordenadoCQuickSort.txt', 'a')
total = 0
for i in arreglo:
    start_time = time()
    quickSort(i)
    transcurrido = time() - start_time
    archivo.write(str(i) + '\n')
    total = transcurrido + total
archivoTiempo.write('ConfC: ' + str(total) + '\n')
archivo.close()
arreglo = configuraciones.confD('QuickSort')
archivo = open('ordenadoDQuickSort.txt', 'a')
total = 0
for i in arreglo:
    start_time = time()
    quickSort(i)
    transcurrido = time() - start_time
    archivo.write(str(i) + '\n')
    total = transcurrido + total
archivoTiempo.write('ConfD: ' + str(total) + '\n')
archivo.close()
arreglo = configuraciones.confE('QuickSort')
archivo = open('ordenadoEQuickSort.txt', 'a')
total = 0
for i in arreglo:
    start_time = time()
    quickSort(i)
    transcurrido = time() - start_time
    archivo.write(str(i) + '\n')
    total = transcurrido + total
archivoTiempo.write('ConfE: ' + str(total) + '\n')
archivo.close()
arreglo = configuraciones.confF('QuickSort')
archivo = open('ordenadoFQuickSort.txt', 'a')
total = 0
for i in arreglo:
    start_time = time()
    quickSort(i)
    transcurrido = time() - start_time
    archivo.write(str(i) + '\n')
    total = transcurrido + total
archivoTiempo.write('ConfF: ' + str(total) + '\n')
archivo.close()