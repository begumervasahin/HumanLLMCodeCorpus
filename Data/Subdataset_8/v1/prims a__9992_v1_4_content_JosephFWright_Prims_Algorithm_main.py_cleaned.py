from Prims import Prims
def main():
    choice = '0'
    while choice == '0':
        print("MST Theory:")
        print("Choose 1 for Prims")
        print("Choose 2 for Kruskals*")
        print("\nChoose 9 to exit.")
        choice = input("Please make a choice: ")
        if choice == "1":
            submenu()
        elif choice == "2":
            print("*Kruskals is not available right now.")
            choice = '0'
        elif choice == "9":
            print("Thank you. Goodbye!")
            quit()
        else:
            print("Not a valid choice!")
            choice = '0'
def submenu():
    file = input("Please enter the filename of your graph file: ")
    start = input("Choose a starting vertex: ")
    graph = input("Would you like the graph to be drawn for you? (Y/N) ")
    if graph.lower() == "y":
        Prims(str(file), int(start), True)
    elif graph.lower() == "n":
        Prims(str(file), int(start), False)
    else:
        print("You didn't choose yes or no. Going back to main menu...")
    main()
if __name__ == "__main__":
    main()