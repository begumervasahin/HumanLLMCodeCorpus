def linearSearch(mylist, search_Num):
    for i in range(len(mylist)):
        if mylist[i] == search_Num:
            return True
    return False
while True:
    print('Enter ** YES ** to run the searching program or anything else to exit: ', end='')
    n = input()
    if n == 'YES':
        print('Enter the elements you want in your list, separated by spaces: ', end='')
        li = [eval(num) for num in input().split()]
        print('\n\n\t **********************************************************\n\nyour list is : ', end='')
        print(li)
        num = eval(input('\n\nSearch for the number you are looking for => '))
        found = linearSearch(li, num)
        if found:
            print(f'\n\t{num} is found at index number {li.index(num)}')
        else:
            print(f'\n\t\t{num} is not in the list. Better luck next time.')
            print('\t(If you want to search for another number, please search again. Otherwise, type 0 to exit)')
            if input() == '0':
                break
    else:
        break