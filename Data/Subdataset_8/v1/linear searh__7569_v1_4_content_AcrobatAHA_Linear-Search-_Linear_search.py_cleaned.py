def linear_search(my_list, search_num):
    for i in range(len(my_list)):
        if my_list[i] == search_num:
            return True
    return False
while True:
    print('Enter **YES** to run the searching program: ', end='')
    user_input = input()
    if user_input.upper() == 'YES':
        print('Enter anything you want to see in your list (separated by space): ', end='')
        input_list = [eval(num) for num in input().split()]
        print('\n\n\t **********************************************************\n\nYour list is: ', end='')
        print(input_list)
        search_num = eval(input('\n\n    Enter the number you want to search for: '))
        found = linear_search(input_list, search_num)
        if found:
            print(f'\n\t{search_num} is found at index {input_list.index(search_num)}')
        else:
            print(f'\n\t{search_num} is not in the list. Better luck next time.')
        exit_choice = input('\n\t(If you want to search another thing, enter **YES**. Otherwise, type any key for exit): ')
        if exit_choice.upper() != 'YES':
            break
    else:
        break