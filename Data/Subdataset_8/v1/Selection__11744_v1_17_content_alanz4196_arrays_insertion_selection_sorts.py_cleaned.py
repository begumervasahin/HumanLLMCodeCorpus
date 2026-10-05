import time
import random
def selection_sort(arr):
    for k in range(len(arr) - 1):
        min_idx = k
        for n in range(k + 1, len(arr)):
            if arr[n] < arr[min_idx]:
                min_idx = n
        arr[k], arr[min_idx] = arr[min_idx], arr[k]
    return arr
def insertion_sort(arr):
    for k in range(1, len(arr)):
        cur = arr[k]
        j = k
        while j > 0 and arr[j - 1] > cur:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = cur
    return arr
if __name__ == '__main__':
    min_val = 0
    max_val = 100
    length = int(input('How many values should be generated? '))
    arr_sel_inc = list(range(1, length + 1))
    arr_sel_dec = list(range(length, 0, -1))
    arr_sel_ran = [random.randint(min_val, max_val) for _ in range(length)]
    arr_ins_inc = arr_sel_inc.copy()
    arr_ins_dec = arr_sel_dec.copy()
    arr_ins_ran = arr_sel_ran.copy()
    array_arrays = [arr_sel_inc, arr_sel_dec, arr_sel_ran, arr_ins_inc, arr_ins_dec, arr_ins_ran]
    array_times = [[] for _ in range(6)]
    for idx, arr in enumerate(array_arrays):
        for _ in range(5):
            temp_arr = arr.copy()
            start_time = time.perf_counter()
            if idx < 3:
                selection_sort(temp_arr)
            else:
                insertion_sort(temp_arr)
            end_time = time.perf_counter()
            array_times[idx].append(end_time - start_time)
    average_times = [sum(times) / 5 for times in array_times]
    print(f'{length}-Val Increasing Selection: {average_times[0]:.20f}')
    print(f'{length}-Val Decreasing Selection: {average_times[1]:.20f}')
    print(f'{length}-Val Random Selection:     {average_times[2]:.20f}')
    print(f'{length}-Val Increasing Insertion: {average_times[3]:.20f}')
    print(f'{length}-Val Decreasing Insertion: {average_times[4]:.20f}')
    print(f'{length}-Val Random Insertion:     {average_times[5]:.20f}')