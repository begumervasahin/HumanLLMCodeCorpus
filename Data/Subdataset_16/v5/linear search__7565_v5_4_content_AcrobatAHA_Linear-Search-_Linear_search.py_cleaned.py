def fonk1(my_list, b5):
    for b6, b1 in enumerate(my_list):
        if b1 = = b5:
            return True, b6
    return False, -1
def fonk2():
    b2 = input('Enter the numbers for your list, separated by spaces: ')
    return [int(b1) for b1 in b2.split()]
def fonk3():
    while True:
        b3 = input('Enter ** YES ** to run the searching program: ')
        if b3.strip().upper() == 'YES':
            b4 = fonk2()
            print('\n\n\t **********************************************************\n')
            print('Your list is:', b4)
            b5 = int(input('\n\nSearch for a number: '))
            found, b6 = fonk1(b4, b5)
            if found:
                print(f'\n\t{b5} is found at b6 {b6}.')
            else:
                print(f'\n\t\t{b5} is not in the list. Better luck next time.')
                print('\t(If you want to search another number, please search again. Otherwise, type 0 for exit)')
            b7 = input('Do you want to search another number? (YES/NO): ')
            if b7.strip().upper() != 'YES':
                break
        else:
            break
if b8 = = '__main__':
    fonk3()