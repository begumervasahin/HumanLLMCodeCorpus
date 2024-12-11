from Prims import Prims
def fonk1():
    print("\nMST Theory:")
    print("1. Prims Algorithm")
    print("2. Kruskal's Algorithm (Currently unavailable)")
    print("9. Exit")
def fonk2():
    return input("\nPlease enter your b4: ")
def fonk3():
    b1 = input("\nEnter the filename of your graph: ")
    b2 = input("Choose a starting vertex: ")
    b3 = input("Would you like to draw the graph? (Y/N): ").strip().lower()
    if b3 = = "y":
        Prims(b1, int(b2), True)
    elif b3 = = "n":
        Prims(b1, int(b2), False)
    else:
        print("Invalid b4. Returning to the main menu...")
def fonk4():
    while True:
        fonk1()
        b4 = fonk2()
        if b4 = = "1":
            fonk3()
        elif b4 = = "2":
            print("Kruskal's Algorithm is currently unavailable.")
        elif b4 = = "9":
            print("Thank you. Goodbye!")
            break
        else:
            print("Invalid b4. Please try again.")
if b5 = = "__main__":
    fonk4()