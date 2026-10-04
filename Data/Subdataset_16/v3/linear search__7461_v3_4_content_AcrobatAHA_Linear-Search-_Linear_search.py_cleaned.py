def fonk1(b3, b4):
    return b4 in b3
def fonk2(prompt):
    return input(prompt)
def fonk3():
    while True:
        b1 = fonk2('Enter ** YES ** to run the searching program or anything else to exit: ')
        if b1.upper() == 'YES':
            b2 = fonk2('Enter the b2 you want in your list, separated by spaces: ')
            try:
                b3 = [eval(num) for num in b2.split()]
            except Exception as e:
                print(f"Invalid input: {e}")
                continue
            print('\n\n\t**********************************************************\n')
            print('Your list is:', b3)
            try:
                b4 = eval(fonk2('\n\nSearch for the number you are looking for => '))
            except Exception as e:
                print(f"Invalid input: {e}")
                continue
            if fonk1(b3, b4):
                print(f'\n\t{b4} is found at index number {b3.index(b4)}')
            else:
                print(f'\n\t\t{b4} is not in the list. Better luck next time.')
                print('\t(If you want to search for another number, please search again. Otherwise, type 0 to exit)')
                if fonk2('') == '0':
                    break
        else:
            break
if b5 = = '__main__':
    fonk3()