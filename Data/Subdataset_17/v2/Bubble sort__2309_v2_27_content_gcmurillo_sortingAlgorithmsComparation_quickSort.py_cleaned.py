from time import time
import configuraciones
def quick_sort(alist):
    def quick_sort_helper(alist, first, last):
        if first < last:
            split_point = partition(alist, first, last)
            quick_sort_helper(alist, first, split_point - 1)
            quick_sort_helper(alist, split_point + 1, last)
    def partition(alist, first, last):
        pivot_value = alist[first]
        left_mark = first + 1
        right_mark = last
        done = False
        while not done:
            while left_mark <= right_mark and alist[left_mark] <= pivot_value:
                left_mark += 1
            while alist[right_mark] >= pivot_value and right_mark >= left_mark:
                right_mark -= 1
            if right_mark < left_mark:
                done = True
            else:
                alist[left_mark], alist[right_mark] = alist[right_mark], alist[left_mark]
        alist[first], alist[right_mark] = alist[right_mark], alist[first]
        return right_mark
    quick_sort_helper(alist, 0, len(alist) - 1)
def process_configuration(conf_function, output_file_prefix):
    arrays = conf_function('QuickSort')
    total_time = 0
    with open(f'{output_file_prefix}.txt', 'a') as result_file, open('tiempoQuick.txt', 'a') as time_file:
        for array in arrays:
            start_time = time()
            quick_sort(array)
            elapsed_time = time() - start_time
            result_file.write(str(array) + '\n')
            total_time += elapsed_time
        time_file.write(f'{output_file_prefix}: {total_time}\n')
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