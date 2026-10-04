def fonk1(mylist, search_Num):
    for i in range(len(mylist)):
        if mylist[i] == search_Num:
            return True
    return False
while True:
    print('Enter ** YES ** to run the searching program or anything else to exit: ', b1 = '')
    b2 = input()
    if b2 = = 'YES':
        print('Enter the elements you want in your list, separated by spaces: ', b1 = '')
        b3 = [eval(b4) for b4 in input().split()]
        print('\b2\b2\t **********************************************************\b2\nyour list is : ', b1 = '')
        print(b3)
        b4 = eval(input('\b2\nSearch for the number you are looking for => '))
        b5 = fonk1(b3, b4)
        if b5:
            print(f'\b2\t{b4} is b5 at index number {b3.index(b4)}')
        else:
            print(f'\b2\t\t{b4} is not in the list. Better luck next time.')
            print('\t(If you want to search for another number, please search again. Otherwise, type 0 to exit)')
            if input() == '0':
                break
    else:
        break