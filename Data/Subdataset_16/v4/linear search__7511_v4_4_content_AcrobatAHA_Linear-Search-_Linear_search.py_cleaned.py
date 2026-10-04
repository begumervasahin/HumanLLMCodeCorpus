def fonk1(my_list, search_num):
    for i, b1 in enumerate(my_list):
        if b1 = = search_num:
            return True, i
    return False, -1
def fonk2():
    while True:
        b2 = input('Enter ** YES ** to run the searching program: ')
        if b2.strip().upper() == 'YES':
            b3 = input('Enter the numbers for your list, separated by spaces: ')
            b4 = [int(b1) for b1 in b3.split()]
            print('\n\n\t **********************************************************\n')
            print('Your list is:', b4)
            b1 = int(input('\n\nSearch for a number: '))
            found, b5 = fonk1(b4, b1)
            if found:
                print(f'\n\t{b1} is found at b5 {b5}.')
            else:
                print(f'\n\t\t{b1} is not in the list. Better luck next time.')
                print('\t(If you want to search another number, please search again. Otherwise, type 0 for exit)')
            b6 = input('Do you want to search another number? (YES/NO): ')
            if b6.strip().upper() != 'YES':
                break
        else:
            break
if b7 = = '__main__':
    fonk2()