def linear_search(my_list, search_num):
    for i, element in enumerate(my_list):
        if element == search_num:
            return True
    return False
while True:
    print('Enter "YES" to run the search program: ', end='')
    user_input = input().upper()
    if user_input == 'YES':
        print('Enter the elements of your list separated by spaces: ', end='')
        user_list = [eval(num) for num in input().split()]
        print('\nYour list is:', user_list)
        search_num = eval(input('Enter the number you want to search for: '))
        found = linear_search(user_list, search_num)
        if found:
            index = user_list.index(search_num)
            print(f'\n{search_num} is found at index number {index}')
        else:
            print(f'\n{search_num} is not in the list. Better luck next time.')
            print('(If you want to search for another number, please search again. Otherwise, type 0 to exit)')
    else:
        break