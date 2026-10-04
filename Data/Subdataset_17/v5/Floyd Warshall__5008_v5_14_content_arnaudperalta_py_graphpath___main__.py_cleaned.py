import json
from os import listdir
from os.path import isfile, join
from graph import Graph
DEFAULT_CONFIG = "graph1.json"
def run_project():
    config = DEFAULT_CONFIG
    display_menu(config)
    while True:
        user_input = input("Enter your choice: ").strip()
        for command in user_input:
            if command == "c":
                config = choose_config()
            elif command in ["t", "n"]:
                graph = Graph(load_config(config))
                execute_algorithm(graph, command)
            elif command == "h":
                display_help()
            elif command == "m":
                display_menu(config)
            elif command == "q":
                print("Exiting the program.")
                return
def display_menu(config):
    print("\npy_graphpath")
    print("-----------------------------------------------------")
    print(f"c : Choose configuration (Current: {config})")
    print("t : Run the optimal rendezvous point algorithm by time")
    print("n : Run the optimal rendezvous point algorithm by number of moves")
    print("h : Display help")
    print("m : Display menu")
    print("q : Quit the program")
    print("-----------------------------------------------------")
def choose_config():
    print("Available configurations:")
    config_files = [f for f in listdir('./cfg') if isfile(join('./cfg', f))]
    for config_file in config_files:
        print(config_file)
    while True:
        config = input("Enter the configuration filename: ").strip()
        if config in config_files:
            print("Configuration successfully changed.")
            return config
        else:
            print("This configuration does not exist. Please try again.")
def display_help():
    print("\nHelp")
    print("For an example of the configuration syntax, see graph_sujet.json.")
    print("The first algorithm calculates the most optimal rendezvous point")
    print("so that the two people meet at this point in minimum time.")
    print("The second algorithm calculates the most optimal rendezvous point")
    print("so that the two people meet at this point with a minimum number")
    print("of moves.")
    print("You can enter multiple characters at once in the program menu.")
    print("-----------------------------------------------------")
def execute_algorithm(graph, command):
    if graph.get_error() != 0:
        error_message = {
            1: "Error in configuration file (nbNoeuds/nomSommets)",
            2: "Error in configuration file (nbLieuxRdv/nomRdv)"
        }
        print(error_message.get(graph.get_error(), "Unknown error"))
    else:
        if command == "t":
            result = graph.find_optimal_rdv()
            if result:
                print(f"The most optimal rendezvous point by time is: {result}")
            else:
                print("No compatible rendezvous point found")
        elif command == "n":
            result = graph.find_optimal_rdv2()
            if result:
                print(f"The most optimal rendezvous point by number of moves is: {result}")
            else:
                print("No compatible rendezvous point found")
def load_config(config):
    config_path = join('./cfg', config)
    with open(config_path, 'r') as file:
        return json.load(file)
if __name__ == '__main__':
    run_project()