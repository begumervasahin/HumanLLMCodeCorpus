def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1
user_input = input('Enter a list of numbers separated by spaces: ')
user_list = user_input.split()
user_list = [int(x) for x in user_list]
search_target = int(input('Enter the number to search for: '))
result_index = linear_search(user_list, search_target)
if result_index < 0:
    print('{} was not found in the list.'.format(search_target))
else:
    print('{} was found at index {}.'.format(search_target, result_index))