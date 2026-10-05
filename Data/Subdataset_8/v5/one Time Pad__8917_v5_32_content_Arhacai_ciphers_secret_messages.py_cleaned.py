import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def show_menu():
    clear_screen()
    print(
        "Welcome to the Secret Messages project for the Treehouse Techdegree.\n\n"
        "Available ciphers:\n\n"
        "- Caesar\n"
        "- Atbash\n"
        "- Affine\n"
        "- Keyword\n\n"
        "Type 'QUIT' to exit Secret Messages.\n\n"
    )
def get_cipher_or_quit():
    available_ciphers = ['Caesar', 'Atbash', 'Affine', 'Keyword']
    cipher_module = __import__('ciphers')
    while True:
        cipher_choice = input("Which cipher would you like to use? ").lower().capitalize()
        if cipher_choice == 'Quit':
            return False
        if cipher_choice in available_ciphers:
            pad = get_pad()
            blocks = in_blocks()
            return getattr(cipher_module, cipher_choice)(pad, blocks)
        print("Sorry, that's not a valid cipher.\n")
def get_message():
    return input("Enter the message: ")
def get_option():
    while True:
        option = input("Do you want to encode or decode? ").lower()
        if option in ('encode', 'decode'):
            return option
        else:
            print("Sorry, please enter a valid option.\n")
def get_pad():
    while True:
        pad = input("Enter a pad number (leave blank for no pad): ")
        if not pad:
            return pad
        try:
            return str(int(pad))
        except ValueError:
            print("Sorry, please enter a valid numeric pad key.\n")
def in_blocks():
    option = input("Encrypt in blocks of 5? (y/N): ").lower()
    return option == 'y'
def show_message(cipher, option, message):
    result = getattr(cipher, option)(message)
    print("\nYour {}d message is: {}".format(option, result))
def cipher_again():
    again = input("\nDo you want to encrypt or decrypt another message? (Y/n): ")
    if again.lower() != 'n':
        run()
    else:
        print("Thanks for using the Secret Messages project. Goodbye!")
def run():
    show_menu()
    cipher = get_cipher_or_quit()
    if cipher:
        message = get_message()
        option = get_option()
        show_message(cipher, option, message)
        cipher_again()
    else:
        print("Thanks for using the Secret Messages project. Goodbye!")
if __name__ == '__main__':
    run()