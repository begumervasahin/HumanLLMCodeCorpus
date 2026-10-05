import os
from ciphers import Caesar, Atbash, Affine, Keyword
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def show_menu():
    clear_screen()
    print(
        "Welcome to the Secret Messages project for the Treehouse Techdegree.\n\n"
        "Available ciphers:\n"
        "- Caesar\n"
        "- Atbash\n"
        "- Affine\n"
        "- Keyword\n\n"
        "Enter 'QUIT' to exit the Secret Messages.\n"
    )
def get_cipher_or_quit():
    available_ciphers = ['Caesar', 'Atbash', 'Affine', 'Keyword']
    while True:
        cipher = input("Which cipher would you like to use? ").capitalize()
        if cipher == 'Quit':
            return False
        if cipher in available_ciphers:
            module = globals()[cipher]
            pad = get_pad()
            blocks = in_blocks()
            return getattr(module, cipher)(pad, blocks)
        print("Sorry, that's not a valid cipher.\n")
def get_message():
    return input("Enter the message: ")
def get_option():
    while True:
        option = input("Do you want to encode or decode the message? ").lower()
        if option in ('encode', 'decode'):
            return option
        print("Sorry, you have to enter 'encode' or 'decode'.\n")
def get_pad():
    while True:
        pad = input("Enter a pad number (leave blank for no pad): ").strip()
        if not pad:
            return pad
        if pad.isdigit():
            return pad
        print("Sorry, you have to enter a valid numeric pad key.\n")
def in_blocks():
    option = input("Encrypt in blocks of 5? [y/N]: ").lower()
    return option == 'y'
def show_message(cipher, option, message):
    result = getattr(cipher, option)(message)
    print("\nYour {}d message is: {}".format(option, result))
def cipher_again():
    start = input("\nDo you want to encrypt or decrypt another message [Y/n]: ").strip()
    if start.lower() != 'n':
        run()
    else:
        print("Thanks for using Secret Messages. Goodbye!")
def run():
    show_menu()
    cipher = get_cipher_or_quit()
    if cipher:
        message = get_message()
        option = get_option()
        show_message(cipher, option, message)
        cipher_again()
    else:
        print("Thanks for using Secret Messages. Goodbye!")
if __name__ == '__main__':
    run()