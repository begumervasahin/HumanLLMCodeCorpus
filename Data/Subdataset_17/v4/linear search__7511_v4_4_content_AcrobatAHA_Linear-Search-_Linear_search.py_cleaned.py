def linear_search(my_list, search_num):
    for i, num in enumerate(my_list):
        if num == search_num:
            return True, i
    return False, -1
def main():
    while True:
        run_program = input('Enter ** YES ** to run the searching program: ')
        if run_program.strip().upper() == 'YES':
            user_input = input('Enter the numbers for your list, separated by spaces: ')
            li = [int(num) for num in user_input.split()]
            print('\n\n\t **********************************************************\n')
            print('Your list is:', li)
            num = int(input('\n\nSearch for a number: '))
            found, index = linear_search(li, num)
            if found:
                print(f'\n\t{num} is found at index {index}.')
            else:
                print(f'\n\t\t{num} is not in the list. Better luck next time.')
                print('\t(If you want to search another number, please search again. Otherwise, type 0 for exit)')
            continue_search = input('Do you want to search another number? (YES/NO): ')
            if continue_search.strip().upper() != 'YES':
                break
        else:
            break
if __name__ == '__main__':
    main()