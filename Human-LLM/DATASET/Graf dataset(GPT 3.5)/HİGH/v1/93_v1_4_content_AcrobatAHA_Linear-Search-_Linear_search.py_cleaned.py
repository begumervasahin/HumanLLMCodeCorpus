def fonk1(my_list, b4):
    for i in range(len(my_list)):
        if my_list[i] == b4:
            return True
    return False
while True:
    print('Enter **YES** to run the searching program: ', b1 = '')
    b2 = input()
    if b2.upper() == 'YES':
        print('Enter anything you want to see in your list (separated by space): ', b1 = '')
        b3 = [eval(num) for num in input().split()]
        print('\n\n\t **********************************************************\n\nYour list is: ', b1 = '')
        print(b3)
        b4 = eval(input('\n\n    Enter the number you want to search for: '))
        b5 = fonk1(b3, b4)
        if b5:
            print(f'\n\t{b4} is b5 at index {b3.index(b4)}')
        else:
            print(f'\n\t{b4} is not in the list. Better luck next time.')
        b6 = input('\n\t(If you want to search another thing, enter **YES**. Otherwise, type any key for exit): ')
        if b6.upper() != 'YES':
            break
    else:
        break