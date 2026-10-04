import csv
from random import shuffle
class Tree:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
    def insert(self, x):
        if self.value is None:
            self.value = x
        else:
            self._insert_recursive(self, x)
    @staticmethod
    def _insert_recursive(current, x):
        if current is None:
            return Tree(x)
        elif x < current.value:
            current.left = Tree._insert_recursive(current.left, x)
        else:
            current.right = Tree._insert_recursive(current.right, x)
        return current
    def height(self):
        if self.value is None:
            return 0
        return self._calculate_height(self)
    @staticmethod
    def _calculate_height(node):
        if node is None:
            return 0
        return max(Tree._calculate_height(node.left), Tree._calculate_height(node.right)) + 1
def generate_random_array(n):
    array = list(range(n))
    shuffle(array)
    return array
def build_tree(arr):
    tree = Tree()
    for value in arr:
        tree.insert(value)
    return tree
def calculate_average_height(n, trials=500):
    total_height = 0
    for _ in range(trials):
        arr = generate_random_array(n)
        tree = build_tree(arr)
        total_height += tree.height()
    return total_height / trials
def save_results_to_csv(results, filename="results.csv"):
    with open(filename, "w+", newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(results)
def main():
    print("n is the number of nodes in the Binary Search Tree")
    print("h is the corresponding average height of 500 randomly generated samples\n")
    results = [["Number of Nodes", "Average Height"]]
    print("Generating results...")
    for n in range(100, 1001, 100):
        average_height = calculate_average_height(n)
        results.append([n, average_height])
        print(f"n = {n:4d}, h = {average_height:.3f}")
    save_results_to_csv(results)
if __name__ == "__main__":
    main()