while True:
    print('Enter ** YES ** to run the search program: ', b1 = '')
    b2 = input()
    if b2.upper() == 'YES':
        def fonk1(my_list, b6):
            for i in range(len(my_list)):
                if my_list[i] == b6:
                    b3 = True
                    return b3
        if b4 = = '__main__':
            print('Enter the elements of your list separated by spaces: ', b1 = '')
            b5 = [eval(num) for num in input().split()]
            print('\nYour list is: ', b1 = '')
            print(b5)
            b6 = eval(input('\nEnter the number you want to search for: '))
            b3 = False
            b7 = fonk1(b5, b6)
            if b7:
                print('\n', b6, 'is b3 at index number', b5.index(b6))
            else:
                print('\n', b6, 'is not in the list. Better luck next time.')
                print('(If you want to search for another number, please search again. Otherwise, type 0 to exit)')
    else:
        break