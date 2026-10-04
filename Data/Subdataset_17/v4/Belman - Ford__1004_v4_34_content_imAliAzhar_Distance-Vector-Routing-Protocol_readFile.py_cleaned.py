import os
def read_file(filename):
    filepath = os.path.join("C:\\", filename)
    neighbors = {}
    with open(filepath, 'r') as infile:
        for counter, line in enumerate(infile):
            line = line.strip()
            if counter == 0:
                no_of_neighbors = int(line)
            else:
                words = line.split()
                neighbor = words[0]
                weight = float(words[1])
                port = int(words[2])
                neighbors[neighbor] = {'cost': weight, 'port': port}
    return neighbors
def print_neighbors(neighbors):
    print("Neighbors:")
    for neighbor, details in neighbors.items():
        print(f"{neighbor}: cost={details['cost']}, port={details['port']}")
def main():
    filename = "input.txt"
    filepath = os.path.join("C:\\", filename)
    if not os.path.isfile(filepath):
        print(f"File {filepath} does not exist.")
        return
    neighbors = read_file(filepath)
    print_neighbors(neighbors)
if __name__ == "__main__":
    main()