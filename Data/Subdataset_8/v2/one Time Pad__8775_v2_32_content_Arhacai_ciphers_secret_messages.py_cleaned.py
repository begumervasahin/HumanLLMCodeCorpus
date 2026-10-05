import os
from ciphers import Caesar, Atbash, Affine, Keyword
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def show_menu():
    clear_screen()
    print(
        "This is the Secret Messages project for the Treehouse Techdegree.\n\n"
        "These are the current available ciphers:\n\n"
        "- Caesar\n"
        "- Atbash\n"
        "- Affine\n"
        "- Keyword\n\n"
        "Enter QUIT to exit Secret Messages.\n\n"
    )
def get_cipher_or_quit():
    available_ciphers = ['Caesar', 'Atbash', 'Affine', 'Keyword']
    while True:
        cipher = input("Which cipher would you like to use? ").lower().capitalize()
        if cipher == 'Quit':
            return False
        if cipher in available_ciphers:
            module = globals()[cipher]
            pad = get_pad()
            blocks = in_blocks()
            return getattr(module, cipher)(pad, blocks)
        print("Sorry, that's not a valid cipher.\n")
def get_message():
    message = input("What's the message? ")
    return message
def get_option():
    while True:
        try:
            option = input("Are we going to encode or decode? ")
            if option == 'encode' or option == 'decode':
                return option
            else:
                raise ValueError
        except ValueError:
            print("Sorry, you have to enter a valid command.\n")
def get_pad():
    while True:
        pad = (input("Enter a pad number (leave blank for no pad): "))
        if pad == '':
            return pad
        else:
            try:
                return str(int(pad))
            except ValueError:
                print("Sorry, you have to enter a valid numeric key pad\n")
def in_blocks():
    option = input("Encryption in blocks of 5? y/N> ").lower()
    if option == 'y':
        return True
    return False
def show_message(cipher, option, message):
    result = getattr(cipher, option)(message)
    print("\nYour {}d message is: {}".format(option, result))
def cipher_again():
    start = input("\nDo you want to encrypt or decrypt another message [Y/n]")
    if start.lower() != 'n':
        run()
    else:
        print("Thanks for using this Secret Messages project. Bye bye!")
def run():
    show_menu()
    cipher = get_cipher_or_quit()
    if cipher:
        message = get_message()
        option = get_option()
        show_message(cipher, option, message)
        cipher_again()
    else:
        print("Thanks for using this Secret Messages project. Bye bye!")
if __name__ == '__main__':
    run()