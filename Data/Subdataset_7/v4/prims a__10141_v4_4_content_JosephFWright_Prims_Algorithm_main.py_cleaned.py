
from Prims import Prims
def fonk1():
    while True:
        print("Minimum Spanning Tree Theory:")
        print("1. Prim's Algorithm")
        print("2. Kruskal's Algorithm (currently unavailable)")
        print("\n9. Exit")
        b1 = input("Please select an option: ")
        if b1 = = "1":
            fonk2()
        elif b1 = = "2":
            print("Apologies, Kruskal's Algorithm is not available right now.")
        elif b1 = = "9":
            print("Thank you. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
def fonk2():
    b2 = input("Please enter the b2 of your graph: ")
    b3 = input("Enter the starting vertex: ")
    b4 = input("Do you want to visualize the graph? (Y/N) ")
    if b4.lower() == "y":
        Prims(b2, int(b3), True)
    elif b4.lower() == "n":
        Prims(b2, int(b3), False)
    else:
        print("Invalid b1. Returning to main menu...")
if b5 = = "__main__":
    fonk1()