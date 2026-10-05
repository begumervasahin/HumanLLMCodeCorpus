import sys
if len(sys.argv) <= 4:
    print("Usage : creatlist.py Min Max filename [p]")
    print("Min : length of minimum password")
    print("Max : length of maximum password")
    print("p : y for print on screen")
    print("Example : creatlist.py 5 8 passwords.txt y")
    exit()
min_length = int(sys.argv[1])
max_length = int(sys.argv[2])
print_screen = str(sys.argv[4])
filename = str(sys.argv[3])
with open('letters.txt', 'r') as f:
    letters = f.read().split('\n')[0]
with open(filename, 'w') as f_out:
    def create_password(length, password=''):
        if len(password) == length:
            for letter in letters:
                new_password = password + str(letter) + '\n'
                if print_screen.lower() == 'y':
                    print(new_password)
                f_out.write(new_password)
        elif len(password) < length:
            for letter in letters:
                new_password = password + str(letter)
                create_password(length, new_password)
    print("Welcome to the Passlist Creator from rw-sec.com")
    print("Author: Mohammed Mahmood")
    print("Starting list creation:")
    for length in range(min_length, max_length):
        create_password(length, '')
print('Password List Created Successfully.')