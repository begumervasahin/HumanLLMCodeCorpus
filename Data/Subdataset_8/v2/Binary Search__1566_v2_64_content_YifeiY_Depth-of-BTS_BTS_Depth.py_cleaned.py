from random import shuffle
import csv
class TreeNode:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    def insert(self, x):
        self.recursive_insert(x)
    def recursive_insert(self, x):
        if self.value is None:
            self.value = x
            self.left = None
            self.right = None
        elif self.value > x:
            if self.left is None:
                self.left = TreeNode(x, None, None)
            else:
                self.left.recursive_insert(x)
        else:
            if self.right is None:
                self.right = TreeNode(x, None, None)
            else:
                self.right.recursive_insert(x)
    def height(self):
        return self.calculate_height(self)
    def calculate_height(self, node):
        if node is None:
            return 0
        return max(self.calculate_height(node.left), self.calculate_height(node.right)) + 1
def generate_random_array(n):
    array = [i for i in range(n)]
    shuffle(array)
    return array
def build_tree(arr):
    tree = TreeNode()
    for element in arr:
        tree.insert(element)
    return tree
def main():
    print("n is the number of vertices in the Binary Search Tree\nh is the corresponding average height of 500 randomly generated samples\n")
    results = [["number of nodes", "height"]]
    trials = 500
    print("Generating results.....")
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