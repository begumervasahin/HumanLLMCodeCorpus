import os
import time
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
def get_input(prompt):
    user_input = input(prompt).strip().lower().replace(" ", "")
    clear_screen()
    return user_input
def handle_nozzle_selection(content):
    nozzle = get_input("How many nozzles?: ")
    if nozzle in ["1", "2"]:
        print("Engine")
        time.sleep(3)
    elif nozzle == "3":
        if content == "he":
            print("Engine")
            time.sleep(3)
        else:
            handle_pressure_selection()
    else:
        print("Invalid number of nozzles.")
        time.sleep(3)
def handle_pressure_selection():
    pressure = get_input("Type 1 for <, or 2 for >: ")
    if pressure in ["1", "2"]:
        print("Engine")
        time.sleep(3)
    else:
        print("Invalid input for pressure.")
        time.sleep(3)
def main():
    content = get_input("What is the content? e.g: He, N or D: ")
    if content in ["he", "n", "d"]:
        handle_nozzle_selection(content)
    else:
        print("Invalid content input! Try again.")
        time.sleep(3)
if __name__ == "__main__":
    main()
