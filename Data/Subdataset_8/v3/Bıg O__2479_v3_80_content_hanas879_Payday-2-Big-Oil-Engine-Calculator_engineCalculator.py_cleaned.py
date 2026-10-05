import os
from time import sleep
def clear_console():
    os.system("cls" if os.name == "nt" else "clear")
def handle_engine_function(nozzle):
    if nozzle == "2":
        print("Engine with 2 nozzles")
    elif nozzle == "3":
        print("Engine with 3 nozzles")
    else:
        print("Sorry, I can't understand that")
def handle_pressure_function(nozzle, pressure):
    if nozzle == "3":
        print("Now it's time to check the pressure:")
        if pressure == "1":
            print("Pressure is less than")
        elif pressure == "2":
            print("Pressure is greater than")
        else:
            print("Sorry, I can't understand that")
    else:
        print("Sorry, I can't understand that")
def main():
    clear_console()
    content = input("What is the content? (He, N, or D): ").lower().replace(" ", "")
    clear_console()
    if content == "he":
        nozzle = input("How many nozzles?: ")
        clear_console()
        handle_engine_function(nozzle)
    elif content == "n" or content == "d":
        nozzle = input("How many nozzles?: ")
        clear_console()
        if nozzle in {"1", "2"}:
            handle_engine_function(nozzle)
        elif nozzle == "3":
            pressure = input("Type 1 for '<', or 2 for '>': ")
            clear_console()
            handle_pressure_function(nozzle, pressure)
        else:
            print("Sorry, I can't understand that")
    else:
        print("Something went wrong! Please try again")
    sleep(3)
if __name__ == "__main__":
    main()