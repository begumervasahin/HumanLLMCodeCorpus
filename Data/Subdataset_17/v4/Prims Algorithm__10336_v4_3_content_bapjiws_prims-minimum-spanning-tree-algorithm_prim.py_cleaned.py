import heapq
import operator
import time
import argparse
def parse_input_file(filename):
    with open(filename, 'r') as file:
        raw = [list(map(float, line.split())) for line in file.readlines()]
    return raw
def build_adjacency_list(raw):
    min_key = int(min([v[0] for v in raw[1:]] + [v[1] for v in raw[1:]]))
    max_key = int(max([v[0] for v in raw[1:]] + [v[1] for v in raw[1:]]))
    adjacency_list = {k: [(v[2], v[0], v[1]) for v in raw[1:] if v[0] == k or v[1] == k] for k in range(min_key, max_key + 1)}
    return adjacency_list
def get_source_node(raw):
    while True:
        try:
            source = int(input("Source node: "))
            if source in [v[0] for v in raw[1:]] + [v[1] for v in raw[1:]]:
                return source
            else:
                print("No such node, please try again")
        except ValueError:
            print("Invalid input, please enter an integer")
def prim_mst(adjacency_list, source, total_vertices):
    costs = []
    vertices = set()
    new_vertex = source
    vertices.add(float(new_vertex))
    heap = []
    mst_structure = []
    while len(vertices) < total_vertices:
        for item in adjacency_list[new_vertex]:
            heapq.heappush(heap, item)
        while heap:
            extract = heapq.heappop(heap)
            if operator.xor(extract[1] in vertices, extract[2] in vertices):
                break
        else:
            break
        adjacency_list[extract[1]].remove(extract)
        adjacency_list[extract[2]].remove(extract)
        new_vertex = extract[1] if extract[1] not in vertices else extract[2]
        vertices.add(new_vertex)
        mst_structure.append((extract[1], extract[2], extract[0]))
        costs.append(extract[0])
    return sum(costs), mst_structure
def main():
    start = time.process_time()
    parser = argparse.ArgumentParser(description="Implements Prim's minimum spanning tree algorithm.")
    parser.add_argument("-s", help="the structure of the MST", action="store_true")
    parser.add_argument("-t", help="execution time", action="store_true")
    parser.add_argument("filename", help=".txt file to parse")
    args = parser.parse_args()
    raw = parse_input_file(args.filename)
    total_vertices = int(raw[0][0])
    adjacency_list = build_adjacency_list(raw)
    source = get_source_node(raw)
    total_cost, mst_structure = prim_mst(adjacency_list, source, total_vertices)
    print(f"The overall cost of the MST: {total_cost}")
    if args.s:
        print(f"The structure of the MST: {mst_structure}")
    if args.t:
        print(f"--- {time.process_time() - start} seconds ---")
if __name__ == "__main__":
    main()