from time import time
import configuraciones
def quickSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)
def quickSortHelper(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)
        quickSortHelper(alist, first, splitpoint - 1)
        quickSortHelper(alist, splitpoint + 1, last)
def partition(alist, first, last):
    pivotvalue = alist[first]
    leftmark = first + 1
    rightmark = last
    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark += 1
        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark -= 1
        if rightmark < leftmark:
            done = True
        else:
            alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]
    alist[first], alist[rightmark] = alist[rightmark], alist[first]
    return rightmark
def process_configuration(conf_function, output_file_prefix):
    arreglo = conf_function('QuickSort')
    with open(f'{output_file_prefix}.txt', 'a') as archivo, open('tiempoQuick.txt', 'a') as archivoTiempo:
        total_time = 0
        for i in arreglo:
            start_time = time()
            quickSort(i)
            elapsed_time = time() - start_time
            archivo.write(str(i) + '\n')
            total_time += elapsed_time
        archivoTiempo.write(f'{output_file_prefix}: {total_time}\n')
def main():
    configurations = [
        (configuraciones.confA, 'ordenadoAQuickSort'),
        (configuraciones.confB, 'ordenadoBQuickSort'),
        (configuraciones.confC, 'ordenadoCQuickSort'),
        (configuraciones.confD, 'ordenadoDQuickSort'),
        (configuraciones.confE, 'ordenadoEQuickSort'),
        (configuraciones.confF, 'ordenadoFQuickSort')
    ]
    for conf_function, output_file_prefix in configurations:
        process_configuration(conf_function, output_file_prefix)
if __name__ == "__main__":
    main()