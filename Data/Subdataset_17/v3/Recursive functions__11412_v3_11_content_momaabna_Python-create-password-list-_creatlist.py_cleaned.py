import sys
HELP_TEXT =
def display_help_and_exit():
    print(HELP_TEXT)
    sys.exit()
def parse_arguments():
    if len(sys.argv) < 4:
        display_help_and_exit()
    try:
        min_length = int(sys.argv[1])
        max_length = int(sys.argv[2])
    except ValueError:
        display_help_and_exit()
    filename = sys.argv[3]
    print_option = sys.argv[4].lower() if len(sys.argv) > 4 else 'n'
    return min_length, max_length, filename, print_option
def read_letters():
    try:
        with open('letters.txt', 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        print("Error: 'letters.txt' not found.")
        sys.exit(1)
def create_passwords(length, current_password, letters, print_option, file_handle):
    if len(current_password) == length:
        for letter in letters:
            password = current_password + letter
            if print_option == 'y':
                print(password)
            file_handle.write(password + '\n')
    else:
        for letter in letters:
            create_passwords(length, current_password + letter, letters, print_option, file_handle)
def main():
    min_length, max_length, filename, print_option = parse_arguments()
    letters = read_letters()
    print()
    with open(filename, 'w') as file:
        for length in range(min_length, max_length + 1):
            create_passwords(length, '', letters, print_option, file)
    print('Password List Created Successfully.')
if __name__ == '__main__':
    main()