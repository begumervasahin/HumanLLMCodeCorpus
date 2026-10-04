import time
class Shifts:
    def __init__(self):
        self.inversions = 0
def split_array(arr):
    mid = len(arr)
    left_half = arr[:mid]
    right_half = arr[mid:]
    return left_half, right_half
def count_inversions(left_half, right_half, shifts):
    left_half.sort()
    right_half.sort()
    i, j = 0, 0
    left_size = len(left_half)
    right_size = len(right_half)
    while i < left_size:
        while j < right_size and left_half[i] > right_half[j]:
            shifts.inversions += left_size - i
            j += 1
        i += 1
def merge_sort(arr, shifts):
    if len(arr) > 1:
        left_half, right_half = split_array(arr)
        merge_sort(left_half, shifts)
        merge_sort(right_half, shifts)
        count_inversions(left_half, right_half, shifts)
def count_array_inversions(arr):
    shifts = Shifts()
    merge_sort(arr, shifts)
    return shifts.inversions
def get_current_time():
    return int(time.time())
def convert_seconds_to_minutes(seconds):
    return divmod(seconds, 60)
def display_test_results(test_name, inversions, expected, start_time):
    end_time = get_current_time()
    elapsed_seconds = end_time - start_time
    minutes, seconds = convert_seconds_to_minutes(elapsed_seconds)
    status = 'PASS' if inversions == expected else 'FAIL'
    print(f"\n{test_name} - Number of inversions: {inversions} | Expected: {expected} | Status: {status}")
    print(f"{test_name} - Total time: {minutes} minutes {seconds} seconds\n")
def main():
    test_cases = [
        ('TC2_1', 'TC2_1_length_441_answer_46768', 46768),
        ('TC2_2', 'TC2_2_length_18_answer_77', 77)
    ]
    for test_name, module_name, expected in test_cases:
        module = __import__(module_name, fromlist=['arr'])
        arr = module.arr
        start_time = get_current_time()
        inversions = count_array_inversions(arr)
        display_test_results(test_name, inversions, expected, start_time)
if __name__ == '__main__':
    main()