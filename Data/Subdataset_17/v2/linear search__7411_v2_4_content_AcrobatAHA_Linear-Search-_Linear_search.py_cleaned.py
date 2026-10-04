def linear_search(mylist, search_num):
    for item in mylist:
        if item == search_num:
            return True
    return False
def get_user_input(prompt):
    return input(prompt)
def main():
    while True:
        user_choice = get_user_input('Enter ** YES ** to run the searching program or anything else to exit: ')
        if user_choice == 'YES':
            elements = get_user_input('Enter the elements you want in your list, separated by spaces: ')
            mylist = [eval(num) for num in elements.split()]
            print('\n\n\t **********************************************************\n')
            print('Your list is: ', mylist)
            search_num = eval(get_user_input('\n\nSearch for the number you are looking for => '))
            found = linear_search(mylist, search_num)
            if found:
                print(f'\n\t{search_num} is found at index number {mylist.index(search_num)}')
            else:
                print(f'\n\t\t{search_num} is not in the list. Better luck next time.')
                print('\t(If you want to search for another number, please search again. Otherwise, type 0 to exit)')
                if get_user_input('') == '0':
                    break
        else:
            break
if __name__ == '__main__':
    main()