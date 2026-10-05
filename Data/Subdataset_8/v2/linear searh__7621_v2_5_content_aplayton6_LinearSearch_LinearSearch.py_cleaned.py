def linear_search(alist, key):
    for i, value in enumerate(alist):
        if value == key:
            return i
    return -1
user_input = input('Enter a list of numbers separated by spaces: ')
user_list = [int(x) for x in user_input.split()]
search_key = int(input('Enter the number to search for: '))
result_index = linear_search(user_list, search_key)
if result_index < 0:
    print(f'{search_key} was not found in the list.')
else:
    print(f'{search_key} was found at index {result_index}.')