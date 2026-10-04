import random
import csv
class Tree:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
    def insert(self, x):
        if self.value is None:
            self.value = x
        elif x < self.value:
            if self.left is None:
                self.left = Tree(x)
            else:
                self.left.insert(x)
        else:
            if self.right is None:
                self.right = Tree(x)
            else:
                self.right.insert(x)
    def height(self):
        if self.value is None:
            return 0
        left_height = self.left.height() if self.left else 0
        right_height = self.right.height() if self.right else 0
        return max(left_height, right_height) + 1
def generate_random_array(n):
    array = list(range(n))
    random.shuffle(array)
    return array
def build_tree(arr):
    tree = Tree()
    for value in arr:
        tree.insert(value)
    return tree
def calculate_average_height(n, trials):
    total_height = 0
    for _ in range(trials):
        arr = generate_random_array(n)
        tree = build_tree(arr)
        total_height += tree.height()
    return total_height / trials
def main():
    print("n is the number of vertices in the Binary Search Tree")
    print("h is the corresponding average height of 500 randomly generated samples\n")
    results = [["Number of Nodes", "Average Height"]]
    trials = 500
    print("Generating results...")
    for n in range(100, 1001, 100):
        average_height = calculate_average_height(n, trials)
        results.append([n, round(average_height, 3)])
        print(f"n = {n:4d}, h = {average_height:.3f}")
    with open("results.csv", "w", newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(results)
if __name__ == "__main__":
    main()