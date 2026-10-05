from time import time
import configuraciones
def shell_sort_algorithm(alist):
    sublist_count = len(alist)
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(alist, start_position, sublist_count)
        print("After increments of size", sublist_count, "The list is", alist)
        sublist_count
def gap_insertion_sort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):
        current_value = alist[i]
        position = i
        while position >= gap and alist[position - gap] > current_value:
            alist[position] = alist[position - gap]
            position -= gap
        alist[position] = current_value
def run_and_measure(configurations, file_prefix):
    archivo_tiempo = open('tiempoShell.txt', 'a')
    total = 0
    for conf_name, conf_function in configurations.items():
        arreglo = conf_function('ShellSort')
        archivo = open(f'{file_prefix}{conf_name}ShellSort.txt', 'a')
        for i in arreglo:
            start_time = time()
            shell_sort_algorithm(i)
            elapsed_time = time() - start_time
            archivo.write(str(i) + '\n')
            total += elapsed_time
        archivo_tiempo.write(f'{conf_name}: {total}\n')
        archivo.close()
    archivo_tiempo.close()
if __name__ == "__main__":
    configurations = {
        'A': configuraciones.confA,
        'B': configuraciones.confB,
        'C': configuraciones.confC,
        'D': configuraciones.confD,
        'E': configuraciones.confE,
        'F': configuraciones.confF
    }
    run_and_measure(configurations, 'ordenado')