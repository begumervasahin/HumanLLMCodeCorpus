import os
def read_file(filepath):
    neighbors = {}
    with open(filepath, 'r') as infile:
        for line_number, line in enumerate(infile):
            line = line.strip()
            if line_number == 0:
                try:
                    no_of_neighbors = int(line)
                except ValueError:
                    print(f"Invalid number of neighbors: {line}")
                    return {}
            else:
                words = line.split()
                if len(words) != 3:
                    print(f"Invalid line format: {line}")
                    continue
                neighbor, weight, port = words[0], words[1], words[2]
                try:
                    weight = float(weight)
                    port = int(port)
                except ValueError:
                    print(f"Invalid weight or port in line: {line}")
                    continue
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