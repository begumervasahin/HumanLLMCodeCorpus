def linear_search(lst, target):
    for index, value in enumerate(lst):
        if value == target:
            return index
    return -1
def get_user_list():
    user_input = input('Enter a list of numbers separated by spaces: ')
    return [int(x) for x in user_input.split()]
def main():
    user_list = get_user_list()
    search_target = int(input('Enter the number to search for: '))
    result_index = linear_search(user_list, search_target)
    if result_index < 0:
        print('{} was not found in the list.'.format(search_target))
    else:
        print('{} was found at index {}.'.format(search_target, result_index))
if __name__ == "__main__":
    main()