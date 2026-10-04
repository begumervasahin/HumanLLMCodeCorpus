import os
def read_file(filename):
    filepath = os.path.join("C:\\", filename)
    neighbors = {}
    with open(filepath, 'r') as infile:
        for counter, line in enumerate(infile):
            if counter == 0:
                no_of_neighbors = int(line.strip())
            else:
                words = line.split()
                neighbor = words[0]
                weight = float(words[1])
                port = int(words[2])
                neighbors[neighbor] = {'cost': weight, 'port': port}
    return neighbors
def main():
    filename = "input.txt"
    neighbors = read_file(filename)
    print("Neighbors:")
    for neighbor, details in neighbors.items():
        print(f"{neighbor}: cost={details['cost']}, port={details['port']}")
if __name__ == "__main__":
    main()