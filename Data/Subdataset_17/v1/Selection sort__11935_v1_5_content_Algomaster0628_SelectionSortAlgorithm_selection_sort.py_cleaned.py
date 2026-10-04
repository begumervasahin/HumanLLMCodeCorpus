def selection_sort(num_list):
    sorted_list = []
    step = 1
    while len(num_list) > 0:
        min_value = num_list[0]
        for number in num_list:
            if number < min_value:
                min_value = number
        print(f'\nStep {step}')
        print('Remaining list:', num_list)
        print('Sorted list:', sorted_list)
        sorted_list.append(min_value)
        num_list.remove(min_value)
        step += 1
    print('\nFinish:')
    print('Final sorted list:', sorted_list)
if __name__ == "__main__":
    numbers = [2, 1, 5, 3, 4, 7, 6, 9, 8, 10]
    selection_sort(numbers)