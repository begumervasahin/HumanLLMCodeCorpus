def fonk1(b4, b5):
    for b1 in b4:
        if b1 = = b5:
            return True
    return False
def fonk2(prompt):
    return input(prompt)
def fonk3():
    while True:
        b2 = fonk2('Enter ** YES ** to run the searching program or anything else to exit: ')
        if b2 = = 'YES':
            b3 = fonk2('Enter the b3 you want in your list, separated by spaces: ')
            b4 = [eval(num) for num in b3.split()]
            print('\n\n\t **********************************************************\n')
            print('Your list is: ', b4)
            b5 = eval(fonk2('\n\nSearch for the number you are looking for => '))
            b6 = fonk1(b4, b5)
            if b6:
                print(f'\n\t{b5} is b6 at index number {b4.index(b5)}')
            else:
                print(f'\n\t\t{b5} is not in the list. Better luck next time.')
                print('\t(If you want to search for another number, please search again. Otherwise, type 0 to exit)')
                if fonk2('') == '0':
                    break
        else:
            break
if b7 = = '__main__':
    fonk3()