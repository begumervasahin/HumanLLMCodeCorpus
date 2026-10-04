import random
import sys
import pickle
import ABR
import RB
sys.setrecursionlimit(4400)
def load_test_parameters(filename):
    with open(filename, "rb") as f:
        return pickle.load(f)
def save_results(filename, data):
    with open(filename, "wb") as f:
        pickle.dump(data, f)
def test_heights():
    test_heights_start = load_test_parameters("tests.p")
    bst_results = test_height_ABR(test_heights_start)
    rbt_random_results, rbt_ordered_results = test_height_RB(test_heights_start)
    save_results("resultHeightABR.p", bst_results)
    save_results("resultHeightRB_random.p", rbt_random_results)
    save_results("resultHeightRB_ordered.p", rbt_ordered_results)
def test_height_ABR(test_params):
    elements, range_elements = test_params
    random_heights = []
    print("\n" + "=" * 100)
    print("Average heights of Binary Search Trees for random elements. 3 executions per test.")
    print("Columns: ranges [20, 200, 1000, 10000000].")
    print("Rows: elements [10, 50, 500, 1000, 10000, 50000]")
    print("=" * 100 + "\n")
    for num_elements in elements:
        avg_heights_for_ranges = []
        for max_val in range_elements:
            heights = []
            for _ in range(3):
                bst = ABR.BinarySearchTree()
                for _ in range(num_elements):
                    bst.insert(random.randint(0, max_val))
                heights.append(bst.getHeight(bst.root))
            avg_heights_for_ranges.append(sum(heights) / len(heights))
        random_heights.append(avg_heights_for_ranges)
        print(avg_heights_for_ranges)
    return random_heights
def test_height_RB(test_params):
    elements, range_elements = test_params
    random_heights = []
    ordered_heights = []
    print("\n" + "=" * 100)
    print("Average heights of Red-Black Trees for random elements. 10 executions per test.")
    print("Columns: ranges [20, 200, 1000, 10000000].")
    print("Rows: elements [10, 50, 500, 1000, 10000, 50000]")
    print("=" * 100 + "\n")
    for num_elements in elements:
        avg_heights_for_ranges = []
        for max_val in range_elements:
            heights = []
            for _ in range(10):
                rbt = RB.RedBlackTree()
                for _ in range(num_elements):
                    rbt.insert(random.randint(0, max_val))
                heights.append(rbt.getHeight(rbt.root))
            avg_heights_for_ranges.append(sum(heights) / len(heights))
        random_heights.append(avg_heights_for_ranges)
        print(avg_heights_for_ranges)
    print("\n" + "=" * 100)
    print("Average heights of Red-Black Trees for ordered elements. 5 executions per test.")
    print("Columns: ranges [20, 200, 1000, 10000000].")
    print("Rows: elements [10, 50, 500, 1000, 10000, 50000]")
    print("=" * 100 + "\n")
    for num_elements in elements:
        avg_heights_for_ranges = []
        for _ in range(len(range_elements)):
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