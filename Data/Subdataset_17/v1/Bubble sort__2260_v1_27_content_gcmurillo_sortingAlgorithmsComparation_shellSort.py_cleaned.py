import time
import configuraciones
def shell_sort(alist):
    sublist_count = len(alist)
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(alist, start_position, sublist_count)
        print("After increments of size", sublist_count, "The list is", alist)
        sublist_count = sublist_count
def gap_insertion_sort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):
        current_value = alist[i]
        position = i
        while position >= gap and alist[position - gap] > current_value:
            alist[position] = alist[position - gap]
            position = position - gap
        alist[position] = current_value
def sort_and_record(config_function, config_name):
    arreglo = config_function('ShellSort')
    archivo = open(f'ordenado{config_name}ShellSort.txt', 'a')
    total_time = 0
    for i in arreglo:
        start_time = time.time()
        shell_sort(i)
        elapsed_time = time.time() - start_time
        archivo.write(str(i) + '\n')
        total_time += elapsed_time
    archivo.close()
    return total_time
def main():
    archivo_tiempo = open('tiempoShell.txt', 'a')
    configurations = [
        (configuraciones.confA, 'A'),
        (configuraciones.confB, 'B'),
        (configuraciones.confC, 'C'),
        (configuraciones.confD, 'D'),
        (configuraciones.confE, 'E'),
        (configuraciones.confF, 'F')
    ]
    for config_function, config_name in configurations:
        total_time = sort_and_record(config_function, config_name)
        archivo_tiempo.write(f'Conf{config_name}: {total_time}\n')
    archivo_tiempo.close()
if __name__ == "__main__":
    main()