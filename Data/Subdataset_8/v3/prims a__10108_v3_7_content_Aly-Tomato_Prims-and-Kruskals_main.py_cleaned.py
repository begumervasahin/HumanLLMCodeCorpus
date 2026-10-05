import sys
import kruskals
import prims
import glb
def print_usage():
    print("USAGE: main.py [\"file.txt\"] [algo] where p = prims, k = kruskals")
    sys.exit()
def execute_algorithm(file, delimiter, algorithm):
    if algorithm == 'p':
        prims.read_graph(file, delimiter)
        graph, total_distance = prims.prims()
    elif algorithm == 'k':
        kruskals.read_graph(file, delimiter)
        graph, total_distance = kruskals.kruskals()
    else:
        print_usage()
    glb.print_pretty()
    print(f"Total Distance: {total_distance}")
def main():
    if len(sys.argv) < 3:
        print_usage()
    file_path = sys.argv[1]
    delimiter = ' '
    algorithm = sys.argv[2]
    execute_algorithm(file_path, delimiter, algorithm)
if __name__ == "__main__":
    main()