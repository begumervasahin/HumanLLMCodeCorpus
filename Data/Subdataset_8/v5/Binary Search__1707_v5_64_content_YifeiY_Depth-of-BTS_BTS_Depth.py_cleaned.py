from random import shuffle
import csv
class TreeNode:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
class BinarySearchTree:
    def __init__(self):
        self.root = None
    def insert(self, x):
        self.root = self._recursive_insert(self.root, x)
    def _recursive_insert(self, current, x):
        if current is None:
            return TreeNode(x)
        elif current.value > x:
            current.left = self._recursive_insert(current.left, x)
        else:
            current.right = self._recursive_insert(current.right, x)
        return current
    def height(self, tree=None):
        if tree is None:
            tree = self.root
        if tree is None:
            return 0
        return max(self.height(tree.left), self.height(tree.right)) + 1
def generate_random_array(n):
    array = [i for i in range(n)]
    shuffle(array)
    return array
def build_binary_search_tree(arr):
    tree = BinarySearchTree()
    for num in arr:
        tree.insert(num)
    return tree
def main():
    print("n is the number of vertices in the Binary Search Tree.")
    print("h is the corresponding average height of 500 randomly generated samples.\n")
    results = [["number of nodes", "height"]]
    trials = 500
    print("Generating results...")
    for n in range(100, 1001, 100):
        height_sum = 0
        for _ in range(trials):
            arr = generate_random_array(n)
            bst = build_binary_search_tree(arr)
            height_sum += bst.height()
        average_height = height_sum / trials
        results.append([n, average_height])
        print(f"n = {results[-1][0]}, h = {results[-1][1]:.3f}")
    with open("results.csv", "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(results)
if __name__ == "__main__":
    main()