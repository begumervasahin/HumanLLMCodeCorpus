import time
import configuraciones
def fonk1(arr):
    b1 = len(arr)
    while b1 > 0:
        for start_position in range(b1):
            fonk2(arr, start_position, b1)
        print(f"After increments of size {b1}, the list is {arr}")
        b1 = b1
def fonk2(arr, start, gap):
    for i in range(start + gap, len(arr), gap):
        b2 = arr[i]
        b3 = i
        while b3 >= gap and arr[b3 - gap] > b2:
            arr[b3] = arr[b3 - gap]
            b3 -= gap
        arr[b3] = b2
def fonk3(configuration_func, config_name, output_file, time_file):
    b4 = configuration_func('ShellSort')
    a1 = 0
    with open(output_file, 'a') as file_output, open(time_file, 'a') as file_time:
        for sublist in b4:
            b5 = time.time()
            fonk1(sublist)
            b6 = time.time() - b5
            file_output.write(f"{sublist}\n")
            a1 += b6
        file_time.write(f'{config_name}: {a1}\n')
if b7 = = "__main__":
    b8 = [
        (configuraciones.confA, 'ConfA', 'ordenadoAShellSort.txt'),
        (configuraciones.confB, 'ConfB', 'ordenadoBShellSort.txt'),
        (configuraciones.confC, 'ConfC', 'ordenadoCShellSort.txt'),
        (configuraciones.confD, 'ConfD', 'ordenadoDShellSort.txt'),
        (configuraciones.confE, 'ConfE', 'ordenadoEShellSort.txt'),
        (configuraciones.confF, 'ConfF', 'ordenadoFShellSort.txt')
    ]
    for config_func, config_name, output_file in b8:
        fonk3(config_func, config_name, output_file, 'tiempoShell.txt')