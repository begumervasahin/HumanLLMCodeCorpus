import time
class InversionCounter:
    def __init__(self):
        self.count = 0
def split_array(array):
    mid = len(array)
    return array[:mid], array[mid:]
def count_split_inversions(left_half, right_half, inversion_counter):
    left_half.sort()
    right_half.sort()
    i, j = 0, 0
    left_size = len(left_half)
    right_size = len(right_half)
    while i < left_size:
        while j < right_size and left_half[i] > right_half[j]:
            inversion_counter.count += left_size - i
            j += 1
        i += 1
def merge_sort_and_count_inversions(array, inversion_counter):
    if len(array) > 1:
        left_half, right_half = split_array(array)
        merge_sort_and_count_inversions(left_half, inversion_counter)
        merge_sort_and_count_inversions(right_half, inversion_counter)
        count_split_inversions(left_half, right_half, inversion_counter)
def count_inversions(array):
    inversion_counter = InversionCounter()
    merge_sort_and_count_inversions(array, inversion_counter)
    return inversion_counter.count
def get_current_time():
    return int(time.time())
def convert_seconds_to_minutes_and_seconds(seconds):
    return divmod(seconds, 60)
def display_test_results(test_name, actual_inversions, expected_inversions, start_time):
    end_time = get_current_time()
    elapsed_seconds = end_time - start_time
    minutes, seconds = convert_seconds_to_minutes_and_seconds(elapsed_seconds)
    status = 'PASS' if actual_inversions == expected_inversions else 'FAIL'
    print(f"\n{test_name} - Number of inversions: {actual_inversions} | Expected: {expected_inversions} | Status: {status}")
    print(f"{test_name} - Total time: {minutes} minutes {seconds} seconds\n")
def main():
    test_cases = [
        ('TC2_1', 'TC2_1_length_441_answer_46768', 46768),
        ('TC2_2', 'TC2_2_length_18_answer_77', 77)
    ]
    for test_name, module_name, expected_inversions in test_cases:
        module = __import__(module_name, fromlist=['arr'])
        array = module.arr
        start_time = get_current_time()
        actual_inversions = count_inversions(array)
        display_test_results(test_name, actual_inversions, expected_inversions, start_time)
if __name__ == '__main__':
    main()