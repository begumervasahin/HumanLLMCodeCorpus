from time import time
import configuraciones
def shell_sort(arr):
    sublist_count = len(arr)
    while sublist_count > 0:
        for start_position in range(sublist_count):
            insertion_sort_with_gap(arr, start_position, sublist_count)
        print(f"After increments of size {sublist_count}, The list is {arr}")
        sublist_count
def insertion_sort_with_gap(arr, start, gap):
    for i in range(start + gap, len(arr), gap):
        current_value = arr[i]
        position = i
        while position >= gap and arr[position - gap] > current_value:
            arr[position] = arr[position - gap]
            position -= gap
        arr[position] = current_value
def main():
    tiempo_file = open('tiempoShell.txt', 'a')
    for conf_name, conf_func in [('ConfA', configuraciones.confA),
                                 ('ConfB', configuraciones.confB),
                                 ('ConfC', configuraciones.confC),
                                 ('ConfD', configuraciones.confD),
                                 ('ConfE', configuraciones.confE),
                                 ('ConfF', configuraciones.confF)]:
        total_time = 0
        for i, arr in enumerate(conf_func('ShellSort'), start=1):
            start_time = time()
            shell_sort(arr)
            elapsed_time = time() - start_time
            with open(f'ordenado{conf_name}ShellSort.txt', 'a') as archivo:
                archivo.write(f'{arr}\n')
            total_time += elapsed_time
            tiempo_file.write(f'{conf_name} Config {i}: {elapsed_time:.6f} seconds\n')
        tiempo_file.write(f'Total time for {conf_name}: {total_time:.6f} seconds\n')
    tiempo_file.close()
if __name__ == '__main__':
    main()