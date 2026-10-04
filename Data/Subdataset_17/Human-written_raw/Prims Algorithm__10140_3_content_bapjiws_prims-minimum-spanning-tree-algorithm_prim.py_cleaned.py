import heapq
import operator
import time
import argparse
def main():
    start = time.process_time()
    parser = argparse.ArgumentParser(description="Implements Prim's minimum spanning tree algorithm.")
    parser.add_argument("-s", help="the structure of the MST", action="store_true")
    parser.add_argument("-t", help="execution time", action="store_true")
    parser.add_argument("filename", help=".txt file to parse")
    args = parser.parse_args()
    with open(args.filename, 'r') as file:
        raw = [ list(map(float, i.split())) for i in file.readlines() ]
    minKey = int(min([v[0] for v in raw[1:]] + [v[1] for v in raw[1:]]))
    maxKey = int(max([v[0] for v in raw[1:]] + [v[1] for v in raw[1:]]))
    ht = { k: [ (v[2], v[0], v[1]) for v in raw[1:] if v[0] == k or v[1] == k ] for k in range(minKey, maxKey + 1) }
    while True:
        source = int(input("Source node: "))
        if source not in [v[0] for v in raw[1:]] + [v[1] for v in raw[1:]]:
            print("No such node, please try again")
            continue
        else:
            break
    costs = []
    vertices = set()
    newVertex = source
    vertices.add(float(newVertex))
    check = []
    structure = []
    while len(vertices) < int(raw[0][0]):
        for item in ht[newVertex]:
            heapq.heappush(check, item)
        while True:
            extract = heapq.heappop(check)
            if not operator.xor(extract[1] in vertices, extract[2] in vertices ):
                continue
            break
        ht[extract[1]].remove(extract)
        ht[extract[2]].remove(extract)
        if extract[1] not in vertices:
            newVertex = extract[1]
            vertices.add(newVertex)
            structure.append((extract[2], extract[1], extract[0]))
        if extract[2] not in vertices:
            newVertex = extract[2]
            vertices.add(extract[2])
            structure.append((extract[1], extract[2], extract[0]))
        costs.append(extract[0])
    print("The overall cost of the MST: {}".format(sum(costs)))
    if args.s:
        print("The structure of the MST: {}".format(structure))
    if args.t:
        print("--- {} seconds ---".format(time.process_time() - start))
if __name__ == "__main__":
    main()