import sys
def print_usage():
    usage =
    print(usage)
def create_passwords(length, current_password, letters, output_file, print_on_screen):
    if len(current_password) == length:
        for letter in letters:
            new_password = current_password + letter + '\n'
            if print_on_screen:
                print(new_password, end='')
            output_file.write(new_password)
    else:
        for letter in letters:
            new_password = current_password + letter
            create_passwords(length, new_password, letters, output_file, print_on_screen)
def main():
    if len(sys.argv) < 4:
        print_usage()
        sys.exit(1)
    try:
        min_length = int(sys.argv[1])
        max_length = int(sys.argv[2])
        filename = sys.argv[3]
        print_on_screen = len(sys.argv) > 4 and sys.argv[4].lower() == 'y'
    except ValueError:
        print("Min and Max should be integers.")
        print_usage()
        sys.exit(1)
    with open('letters.txt', 'r') as f:
        letters = f.read().strip()
    with open(filename, 'w') as output_file:
        print("Welcome to Password List Creator")
        print("Author: Mohammed Mahmood")
        print("Start creating list...")
        for length in range(min_length, max_length + 1):
            create_passwords(length, '', letters, output_file, print_on_screen)
    print("Password List Created Successfully.")
if __name__ == '__main__':
    main()