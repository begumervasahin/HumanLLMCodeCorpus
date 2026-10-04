import os
import time
def clear():
    os.system("cls" if os.name == "nt" else "clear")
def main():
    content = input("What is the content? e.g: He, N or D: ").lower().replace(" ", "")
    clear()
    if content in ["he", "n", "d"]:
        nozzle = input("How many nozzles?: ")
        clear()
        if nozzle == "1":
            print("Engine")
            time.sleep(3)
        elif nozzle == "2":
            print("Engine")
            time.sleep(3)
        elif nozzle == "3":
            if content == "he":
                print("Engine")
                time.sleep(3)
            else:
                print("Now it's time for the pressure")
                pressure = input("Type 1 for <, or 2 for >")
                clear()
                if pressure == "1":
                    print("Engine")
                    time.sleep(3)
                elif pressure == "2":
                    print("Engine")
                    time.sleep(3)
                else:
                    print("I can't understand that")
                    time.sleep(3)
        else:
            print("I can't understand that")
            time.sleep(3)
    else:
        print("Something went wrong! Try again")
        time.sleep(3)
if __name__ == "__main__":
    main()
