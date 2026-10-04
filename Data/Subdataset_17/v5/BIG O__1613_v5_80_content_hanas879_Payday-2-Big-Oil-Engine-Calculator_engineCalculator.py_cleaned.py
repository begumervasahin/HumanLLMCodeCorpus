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
    return input("Type 1 for <, or 2 for >: ")
def display_engine_message():
    clear_screen()
    print("Engine")
    sleep(3)
def process_nozzles_and_pressure(nozzle):
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
def main():
    content = input("What is the content? e.g: He, N or D: ").lower().replace(" ", "")
    clear_screen()
    if content in ["he", "n", "d"]:
        nozzle = get_nozzle_count()
        process_nozzles_and_pressure(nozzle)
    else:
        print("Something went wrong! Try again")
        sleep(3)
if __name__ == "__main__":
    main()