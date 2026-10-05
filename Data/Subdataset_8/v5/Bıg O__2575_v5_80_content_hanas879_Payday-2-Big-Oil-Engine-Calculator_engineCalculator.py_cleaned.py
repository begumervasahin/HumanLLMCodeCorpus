from time import sleep
import os
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
def get_user_content():
    clear_screen()
    return input("What is the content? (Enter 'He', 'N', or 'D'): ").lower().replace(" ", "")
def get_user_nozzles():
    clear_screen()
    return input("How many nozzles? (Enter 1, 2, or 3): ")
def print_engine_message():
    clear_screen()
    print("Engine")
    sleep(3)
def print_error_message():
    clear_screen()
    print("I can't understand that")
    sleep(3)
def print_try_again_message():
    """
    Function to print "Try again" message.
    """
    clear_screen()
    print("Something went wrong! Try again")
    sleep(3)
def main():
    content = get_user_content()
    if content in ["he", "n", "d"]:
        nozzle = get_user_nozzles()
        if nozzle in ["1", "2", "3"]:
            print_engine_message()
        else:
            print_error_message()
    else:
        print_try_again_message()
if __name__ == "__main__":
    main()