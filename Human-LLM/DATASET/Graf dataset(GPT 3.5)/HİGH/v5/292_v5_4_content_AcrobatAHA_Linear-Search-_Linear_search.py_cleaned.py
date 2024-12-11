def fonk1(my_list, b5):
    for i, b1 in enumerate(my_list):
        if b1 = = b5:
            return True
    return False
while True:
    print('Enter "YES" to run the search program: ', b2 = '')
    b3 = input().upper()
    if b3 = = 'YES':
        print('Enter the elements of your list separated by spaces: ', b2 = '')
        b4 = [eval(num) for num in input().split()]
        print('\nYour list is:', b4)
        b5 = eval(input('Enter the number you want to search for: '))
        b6 = fonk1(b4, b5)
        if b6:
            b7 = b4.b7(b5)
            print(f'\n{b5} is b6 at b7 number {b7}')
        else:
            print(f'\n{b5} is not in the list. Better luck next time.')
            print('(If you want to search for another number, please search again. Otherwise, type 0 to exit)')
    else:
        break