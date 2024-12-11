from Prims import Prims
def fonk1():
    print("MST Theory:")
    print("Choose 1 for Prims")
    print("Choose 2 for Kruskals*")
    print("\nChoose 9 to exit.")
def fonk2():
    return input("Please make a b4: ")
def fonk3():
    b1 = input("Please enter the filename of your graph file: ")
    b2 = input("Choose a starting vertex: ")
    b3 = input("Would you like the graph to be drawn for you? (Y/N) ").lower()
    if b3 = = "y":
        Prims(b1, int(b2), True)
    elif b3 = = "n":
        Prims(b1, int(b2), False)
    else:
        print("You didn't choose yes or no. Going back to the main menu...")
def fonk4():
    while True:
        fonk1()
        b4 = fonk2()
        if b4 = = "1":
            fonk3()
        elif b4 = = "2":
            print("*Kruskals is not available right now.")
        elif b4 = = "9":
            print("Thank you. Goodbye!")
            break
        else:
            print("Not a valid b4!")
if b5 = = "__main__":
    fonk4()