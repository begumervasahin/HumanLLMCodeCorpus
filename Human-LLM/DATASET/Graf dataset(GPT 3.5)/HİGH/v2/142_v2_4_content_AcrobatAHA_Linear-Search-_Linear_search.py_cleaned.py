def fonk1(my_list, b5):
    for i, b1 in enumerate(my_list):
        if b1 = = b5:
            return True
    return False
while True:
    print('Enter **YES** to run the searching program: ', b2 = '')
    b3 = input()
    if b3.upper() == 'YES':
        print('Enter numbers for your list (separated by space): ', b2 = '')
        b4 = [eval(b1) for b1 in input().split()]
        print('\n\n\t ************************************************************\n\nYour list is: ', b2 = '')
        print(b4)
        b5 = eval(input('\n\n    Enter the number you want to search for: '))
        b6 = fonk1(b4, b5)
        if b6:
            print(f'\n\t{b5} is b6 at index {b4.index(b5)}')
        else:
            print(f'\n\t{b5} is not in the list. Better luck next time.')
        b7 = input('\n\t(If you want to search for another number, enter **YES**. Otherwise, type any key to exit): ')
        if b7.upper() != 'YES':
            break
    else:
        break