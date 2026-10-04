import os
from time import sleep
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
def get_nozzle_count():
    clear_screen()
    return input("How many nozzles?: ")
def handle_pressure():
    clear_screen()
    print("Now it's time for the pressure")
    print("")
    return input("Type 1 for <, or 2 for >")
def display_engine_message():
    clear_screen()
    print("Engine")
    sleep(3)
def main():
    content = input("What is the content? e.g: He, N or D: ").lower().replace(" ", "")
    clear_screen()
    if content == "he":
        nozzle = get_nozzle_count()
        if nozzle == "2" or nozzle == "3":
            display_engine_message()
        else:
            print("I can't understand that")
            sleep(3)
    elif content == "n":
        nozzle = get_nozzle_count()
        if nozzle in ["1", "2"]:
            display_engine_message()
        elif nozzle == "3":
            pressure = handle_pressure()
            if pressure in ["1", "2"]:
                display_engine_message()
            else:
                print("I can't understand that")
                sleep(3)
        else:
            print("I can't understand that")
            sleep(3)
    elif content == "d":
        nozzle = get_nozzle_count()
        if nozzle in ["1", "2"]:
            display_engine_message()
        elif nozzle == "3":
            pressure = handle_pressure()
            if pressure in ["1", "2"]:
                display_engine_message()
            else:
                print("I can't understand that")
                sleep(3)
        else:
            print("I can't understand that")
            sleep(3)
    else:
        print("Something went wrong! Try again")
        sleep(3)
if __name__ == "__main__":
    main()