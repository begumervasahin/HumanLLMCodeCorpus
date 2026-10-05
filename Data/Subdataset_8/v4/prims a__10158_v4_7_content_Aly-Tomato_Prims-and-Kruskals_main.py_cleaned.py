import sys
import kruskals
import prims
import global_functions as glb
def usage():
    print("USAGE: main.py [\"file.txt\"] [algo] where p = Prims, k = Kruskals")
    sys.exit()
def main():
    if len(sys.argv) < 3:
        usage()
    file_name = sys.argv[1]
    delimiter = ' '
    algo = sys.argv[2]
    if algo == 'p':
        prims.read_graph(file_name, delimiter)
        graph, total_distance = prims.prims()
        glb.print_pretty()
        print(f"Total Distance: {total_distance}")
    elif algo == 'k':
        kruskals.read_graph(file_name, delimiter)
        graph, total_distance = kruskals.kruskals()
        glb.print_pretty()
        print(f"Total Distance: {total_distance}")
    else:
        usage()
if __name__ == "__main__":
    main()