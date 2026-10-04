def selection_sort(num_list):
    sorted_list = []
    step = 1
    while num_list:
        min_value = min(num_list)
        print(f'\nStep {step}')
        print('Remaining list:', num_list)
        print('Sorted list:', sorted_list)
        sorted_list.append(min_value)
        num_list.remove(min_value)
        step += 1
    print('\nFinish:')
    print('Final sorted list:', sorted_list)
def main():
    numbers = [2, 1, 5, 3, 4, 7, 6, 9, 8, 10]
    print("Original list:", numbers)
    selection_sort(numbers)
if __name__ == "__main__":
    main()