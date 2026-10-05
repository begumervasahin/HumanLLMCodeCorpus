from random import shuffle
import csv
class TreeNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
    def insert(self, x):
        if self.value is None:
            self.value = x
        elif self.value > x:
            if self.left is None:
                self.left = TreeNode(x)
            else:
                self.left.insert(x)
        else:
            if self.right is None:
                self.right = TreeNode(x)
            else:
                self.right.insert(x)
    def height(self):
        return self._calculate_height(self)
    def _calculate_height(self, node):
        if node is None:
            return 0
        return max(self._calculate_height(node.left), self._calculate_height(node.right)) + 1
def generate_random_array(n):
    array = list(range(n))
    shuffle(array)
    return array
def build_tree(arr):
    tree = TreeNode()
    for element in arr:
        tree.insert(element)
    return tree
def main():
    print("n is the number of vertices in the Binary Search Tree")
    print("h is the corresponding average height of 500 randomly generated samples\n")
    results = [["number of nodes", "height"]]
    trials = 500
    print("Generating results...")
    for n in range(100, 1001, 100):
        height_sum = 0
        for _ in range(trials):
            arr = generate_random_array(n)
            tree = build_tree(arr)
            height_sum += tree.height()
        average_height = height_sum / trials
        results.append([n, average_height])
        print(f"n = {results[-1][0]}, h = {results[-1][1]:.3f}")
    with open("results.csv", "w+", newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(results)
if __name__ == "__main__":
    main()