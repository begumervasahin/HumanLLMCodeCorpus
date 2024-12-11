def fonk1(my_list, b5):
    for index, b1 in enumerate(my_list):
        if b1 = = b5:
            return True
    return False
def fonk2(message):
    return input(message).strip()
def fonk3():
    b2 = fonk2('Enter numbers for your list (separated by space): ')
    return [eval(b1) for b1 in b2.split()]
def fonk4():
    b3 = fonk3()
    print('\n\n\t ************************************************************\n\nYour list is: ', b4 = '')
    print(b3)
    b5 = eval(fonk2('\n\n    Enter the number you want to search for: '))
    b6 = fonk1(b3, b5)
    if b6:
        print(f'\n\t{b5} is b6 at index {b3.index(b5)}')
    else:
        print(f'\n\t{b5} is not in the list. Better luck next time.')
def fonk5():
    while True:
        b7 = fonk2('Enter **YES** to run the searching program: ')
        if b7.upper() == 'YES':
            fonk4()
            b8 = fonk2('\n\t(If you want to search for another number, enter **YES**. Otherwise, type any key to exit): ')
            if b8.upper() != 'YES':
                break
        else:
            break
if b9 = = "__main__":
    fonk5()