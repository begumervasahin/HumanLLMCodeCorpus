
from Prims import Prims
def fonk1():
    b1 = '0'
    while b1 = ='0':
        print("MST Theory:")
        print("Choose 1 for Prims")
        print("Choose 2 for Kruskals*")
        print("\nChoose 9 to exit.")
        b1 = input("Please make a b1: ")
    if b1 = = "1":
        fonk2()
    elif b1 = = "2":
        print("*Kruskals is not available right now.")
    elif b1 = = "9":
        print("Thank you. Goodbye!")
        quit()
    else:
        print("Not a valid b1!")
        fonk1()
def fonk2():
     b2 = input("Please enter the filename of your b4 b2: ")
     b3 = input("Choose a starting vertex: ")
     b4 = input("Would you like the b4 to be drawn for you? (Y/N) ")
     if b4 = = "Y" or b4 == "y":
         Prims(str(b2), int(b3), True)
     elif b4 = = "N" or b4 == "n":
         Prims(str(b2), int(b3), False)
     else:
         print("You didn't choose yes or no. Going back to main menu...")
         fonk1()
     fonk1()
fonk1()