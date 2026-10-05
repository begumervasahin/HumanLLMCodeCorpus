import sys
import kruskals
import prims
import global_functions as glb
def print_usage():
    print("USAGE: main.py [\"file.txt\"] [algo] where p = Prims, k = Kruskals")
    sys.exit()
def main():
    if len(sys.argv) < 3:
        print_usage()
    file_name = sys.argv[1]
    delimiter = ' '
    algorithm = sys.argv[2]
    if algorithm == 'p':
        prims.read_graph(file_name, delimiter)
        graph, total_distance = prims.prims()
        glb.print_pretty()
        print(f"Total Distance: {total_distance}")
    elif algorithm == 'k':
        kruskals.read_graph(file_name, delimiter)
        graph, total_distance = kruskals.kruskals()
        glb.print_pretty()
        print(f"Total Distance: {total_distance}")
    else:
        print_usage()
if __name__ == "__main__":
    main()