from time import sleep
import os
def clear():
    os.system("cls" if os.name == "nt" else "clear")
def main():
    clear()
    content = input("What is the content? e.g: He, N or D: ").lower().replace(" ", "")
    clear()
    if content == "he" or content == "n" or content == "d":
        nozzle = input("How many nozzles?: ")
        clear()
        if nozzle in ["1", "2", "3"]:
            clear()
            print("Engine")
            sleep(3)
        else:
            clear()
            print("I can't understand that")
            sleep(3)
    else:
        clear()
        print("Something went wrong! Try again")
        sleep(3)
if __name__ == "__main__":
    main()