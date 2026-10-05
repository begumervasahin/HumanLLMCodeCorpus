
from Prims import Prims
def main():
    while True:
        print_menu()
        choice = input("Please select an option: ")
        if choice == "1":
            run_prim()
        elif choice == "2":
            print("Apologies, Kruskal's Algorithm is not available right now.")
        elif choice == "9":
            print("Thank you. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
def print_menu():
    print("Minimum Spanning Tree Theory:")
    print("1. Prim's Algorithm")
    print("2. Kruskal's Algorithm (currently unavailable)")
    print("\n9. Exit")
def run_prim():
    filename = input("Please enter the filename of your graph: ")
    start_vertex = input("Enter the starting vertex: ")
    draw_graph = input("Do you want to visualize the graph? (Y/N) ")
    if draw_graph.lower() == "y":
        Prims(filename, int(start_vertex), True)
    elif draw_graph.lower() == "n":
        Prims(filename, int(start_vertex), False)
    else:
        print("Invalid choice. Returning to main menu...")
if __name__ == "__main__":
    main()