import json
from os import listdir
from os.path import isfile, join
from b5 import Graph
b1 = "graph1.json"
def fonk1():
    b2 = b1
    fonk2(b2)
    while True:
        b3 = input("Enter your choice: ").strip()
        for b4 in b3:
            if b4 = = "c":
                b2 = fonk3()
            elif b4 in ["t", "n"]:
                b5 = Graph(fonk6(b2))
                fonk5(b5, b4)
            elif b4 = = "h":
                fonk4()
            elif b4 = = "m":
                fonk2(b2)
            elif b4 = = "q":
                print("Exiting the program.")
                return
def fonk2(b2):
    print("\npy_graphpath")
    print("-----------------------------------------------------")
    print(f"c : Choose configuration (Current: {b2})")
    print("t : Run the optimal rendezvous point algorithm by time")
    print("n : Run the optimal rendezvous point algorithm by number of moves")
    print("h : Display help")
    print("m : Display menu")
    print("q : Quit the program")
    print("-----------------------------------------------------")
def fonk3():
    print("Available configurations:")
    b6 = [f for f in listdir('./cfg') if isfile(join('./cfg', f))]
    for config_file in b6:
        print(config_file)
    while True:
        b2 = input("Enter the configuration filename: ").strip()
        if b2 in b6:
            print("Configuration successfully changed.")
            return b2
        else:
            print("This configuration does not exist. Please try again.")
def fonk4():
    print("\nHelp")
    print("For an example of the configuration syntax, see graph_sujet.json")
    print("The first algorithm calculates the most optimal rendezvous point")
    print("so that the two people meet at this point in minimum time.")
    print("The second algorithm calculates the most optimal rendezvous point")
    print("so that the two people meet at this point with a minimum number")
    print("of moves.")
    print("You can enter multiple characters at once in the program menu.")
    print("-----------------------------------------------------")
def fonk5(b5, b4):
    if b5.get_error() != 0:
        if b5.get_error() == 1:
            print("Error in configuration file (nbNoeuds/nomSommets)")
        elif b5.get_error() == 2:
            print("Error in configuration file (nbLieuxRdv/nomRdv)")
    else:
        if b4 = = "t":
            b7 = b5.find_optimal_rdv()
            if b7:
                print(f"The most optimal rendezvous point by time is: {b7}")
            else:
                print("No compatible rendezvous point found")
        elif b4 = = "n":
            b7 = b5.find_optimal_rdv2()
            if b7:
                print(f"The most optimal rendezvous point by number of moves is: {b7}")
            else:
                print("No compatible rendezvous point found")
def fonk6(b2):
    with open(join('./cfg', b2), 'r') as file:
        return json.load(file)
if b8 = = '__main__':
    fonk1()