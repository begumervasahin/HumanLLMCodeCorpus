import time
class Shifts:
    def __init__(self):
        self.inversions = 0
def get_halves(array, length):
    mid = length
    left_half, right_half = array[:mid], array[mid:]
    return left_half, right_half
def count_inversions(left_half, left_length, right_half, right_length, shifts):
    left_half.sort()
    right_half.sort()
    i, j = 0, 0
    while i < left_length:
        while j < right_length:
            if left_half[i] > right_half[j]:
                shifts.inversions += left_length - i
                j += 1
            else:
                break
        i += 1
def merge_sort(array, shifts):
    array_length = len(array)
    if array_length > 1:
        left_half, right_half = get_halves(array, array_length)
        left_length, right_length = len(left_half), len(right_half)
        merge_sort(left_half, shifts)
        merge_sort(right_half, shifts)
        count_inversions(left_half, left_length, right_half, right_length, shifts)
def insertion_sort(arr):
    shifts = Shifts()
    merge_sort(arr, shifts)
    return shifts.inversions
def get_time():
    return int(time.time())
def convert_seconds(seconds):
    minutes = seconds
    seconds %= 60
    return minutes, seconds
def test_results(test, inversions, expected, start_time):
    end_time = get_time()
    elapsed_time = end_time - start_time
    minutes, seconds = convert_seconds(elapsed_time)
    if expected == inversions:
        status = 'PASS'
    else:
        status = 'FAIL'
    print('\n')
    print(f"{test} inversions: {inversions}, expected: {expected}, {status}\n")
    print(f"{test} execution time: {minutes} minutes {seconds} seconds")
    print('\n')
def main():
    test_cases = ['TC2_1', 'TC2_2']
    for test in test_cases:
        if test == 'TC2_1':
            from TC2_1_length_441_answer_46768 import arr
            expected = 46768
        elif test == 'TC2_2':
            from TC2_2_length_18_answer_77 import arr
            expected = 77
        start_time = get_time()
        inversions = insertion_sort(arr)
        test_results(test, inversions, expected, start_time)
if __name__ == '__main__':
    main()