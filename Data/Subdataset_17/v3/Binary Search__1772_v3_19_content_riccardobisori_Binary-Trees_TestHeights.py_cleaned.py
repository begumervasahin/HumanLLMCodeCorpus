import random
import sys
import pickle
import ABR
import RB
sys.setrecursionlimit(4400)
def load_test_parameters(filename):
    with open(filename, "rb") as file:
        return pickle.load(file)
def save_results(filename, data):
    with open(filename, "wb") as file:
        pickle.dump(data, file)
def test_heights():
    test_parameters = load_test_parameters("tests.p")
    bst_heights = test_bst_heights(test_parameters)
    rbt_random_heights, rbt_ordered_heights = test_rbt_heights(test_parameters)
    save_results("resultHeightABR.p", bst_heights)
    save_results("resultHeightRB_random.p", rbt_random_heights)
    save_results("resultHeightRB_ordered.p", rbt_ordered_heights)
def test_bst_heights(test_params):
    elements, range_values = test_params
    random_heights = []
    print("\n" + "=" * 100)
    print("Average heights of Binary Search Trees (BST) with random elements. 3 executions per test.")
    print("Columns: Ranges [20, 200, 1000, 10000000].")
    print("Rows: Elements [10, 50, 500, 1000, 10000, 50000]")
    print("=" * 100 + "\n")
    for num_elements in elements:
        avg_heights_for_ranges = []
        for max_value in range_values:
            heights = []
            for _ in range(3):
                bst = ABR.BinarySearchTree()
                for _ in range(num_elements):
                    bst.insert(random.randint(0, max_value))
                heights.append(bst.getHeight(bst.root))
            avg_heights_for_ranges.append(sum(heights) / len(heights))
        random_heights.append(avg_heights_for_ranges)
        print(avg_heights_for_ranges)
    return random_heights
def test_rbt_heights(test_params):
    elements, range_values = test_params
    random_heights = []
    ordered_heights = []
    print("\n" + "=" * 100)
    print("Average heights of Red-Black Trees (RBT) with random elements. 10 executions per test.")
    print("Columns: Ranges [20, 200, 1000, 10000000].")
    print("Rows: Elements [10, 50, 500, 1000, 10000, 50000]")
    print("=" * 100 + "\n")
    for num_elements in elements:
        avg_heights_for_ranges = []
        for max_value in range_values:
            heights = []
            for _ in range(10):
                rbt = RB.RedBlackTree()
                for _ in range(num_elements):
                    rbt.insert(random.randint(0, max_value))
                heights.append(rbt.getHeight(rbt.root))
            avg_heights_for_ranges.append(sum(heights) / len(heights))
        random_heights.append(avg_heights_for_ranges)
        print(avg_heights_for_ranges)
    print("\n" + "=" * 100)
    print("Average heights of Red-Black Trees (RBT) with ordered elements. 5 executions per test.")
    print("Columns: Ranges [20, 200, 1000, 10000000].")
    print("Rows: Elements [10, 50, 500, 1000, 10000, 50000]")
    print("=" * 100 + "\n")
    for num_elements in elements:
        avg_heights_for_ranges = []
        for _ in range(len(range_values)):
            heights = []
            for _ in range(5):
                rbt = RB.RedBlackTree()
                for k in range(num_elements):
                    rbt.insert(k)
                heights.append(rbt.getHeight(rbt.root))
            avg_heights_for_ranges.append(sum(heights) / len(heights))
        ordered_heights.append(avg_heights_for_ranges)
        print(avg_heights_for_ranges)
    return random_heights, ordered_heights
if __name__ == "__main__":
    test_heights()