import sys
HELP_TEXT =
def display_help_and_exit():
    print(HELP_TEXT)
    sys.exit()
def parse_arguments():
    if len(sys.argv) < 4:
        display_help_and_exit()
    min_length = int(sys.argv[1])
    max_length = int(sys.argv[2])
    filename = str(sys.argv[3])
    print_option = str(sys.argv[4]) if len(sys.argv) > 4 else 'n'
    return min_length, max_length, filename, print_option
def read_letters():
    with open('letters.txt', 'r') as file:
        return file.read().strip()
def create_passwords(length, current_password, letters, print_option, file_handle):
    if len(current_password) == length:
        for letter in letters:
            password = current_password + letter + '\n'
            if print_option.lower() == 'y':
                print(password, end='')
            file_handle.write(password)
    elif len(current_password) < length:
        for letter in letters:
            create_passwords(length, current_password + letter, letters, print_option, file_handle)
def main():
    min_length, max_length, filename, print_option = parse_arguments()
    letters = read_letters()
    welcome_message =
    print(welcome_message)
    with open(filename, 'w') as file:
        for length in range(min_length, max_length + 1):
            create_passwords(length, '', letters, print_option, file)
    print('Password List Created Successfully.')
if __name__ == '__main__':
    main()