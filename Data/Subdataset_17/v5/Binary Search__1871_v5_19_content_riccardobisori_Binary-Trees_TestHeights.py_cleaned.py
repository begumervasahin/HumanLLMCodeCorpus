import random
import sys
import pickle
import ABR
import RB
sys.setrecursionlimit(4400)
def test_heights():
    elements, ranges = load_test_data("tests.p")
    result_ABR = test_height_ABR(elements, ranges)
    save_results(result_ABR, "resultHeightABR.p")
    result_RB = test_height_RB(elements, ranges)
    save_results(result_RB, "resultHeightRB.p")
def load_test_data(filename):
    with open(filename, "rb") as file:
        test_data = pickle.load(file)
    return test_data
def save_results(data, filename):
    with open(filename, "wb") as file:
        pickle.dump(data, file)
def test_height_ABR(elements, ranges):
    result_heights = []
    print_test_header("Binary Search Trees (ABR)", elements, ranges, trials=3)
    for num_elements in elements:
        average_heights = []
        for range_limit in ranges:
            heights = [
                measure_tree_height(ABR.BinarySearchTree(), num_elements, range_limit)
                for _ in range(3)
            ]
            average_heights.append(calculate_average(heights))
        result_heights.append(average_heights)
        print(average_heights)
    return result_heights
def test_height_RB(elements, ranges):
    result_random_heights = []
    result_ordered_heights = []
    print_test_header("Red-Black Trees (RB)", elements, ranges, trials=10, test_type="random")
    result_random_heights = perform_height_tests(RB.RedBlackTree, elements, ranges, trials=10, random_elements=True)
    print_test_header("Red-Black Trees (RB)", elements, ranges, trials=5, test_type="ordered")
    result_ordered_heights = perform_height_tests(RB.RedBlackTree, elements, ranges, trials=5, random_elements=False)
    return result_random_heights, result_ordered_heights
def print_test_header(tree_type, elements, ranges, trials, test_type="random"):
    """
    Print the header for the test results.
    Args:
        tree_type (str): The type of tree being tested (e.g., "Binary Search Trees").
        elements (list): List of numbers of elements to insert into the trees.
        ranges (list): List of range limits for generating random elements.
        trials (int): Number of trials performed for each test.
        test_type (str): The type of test being performed ("random" or "ordered").
    """
    print("\n", "=" * 100)
    print(f"Average heights of {tree_type} for {test_type} elements. {trials} executions.")
    print(f"Columns: ranges {ranges}.")
    print(f"Lines: elements {elements}.")
    print("=" * 100, "\n")
def measure_tree_height(tree, num_elements, range_limit, random_elements=True):
    if random_elements:
        elements = (random.randint(0, range_limit) for _ in range(num_elements))
    else:
        elements = range(num_elements)
    for element in elements:
        tree.insert(element)
    return tree.getHeight(tree.root)
def perform_height_tests(tree_class, elements, ranges, trials, random_elements=True):
    result_heights = []
    for num_elements in elements:
        average_heights = []
        for range_limit in ranges:
            heights = [
                measure_tree_height(tree_class(), num_elements, range_limit, random_elements)
                for _ in range(trials)
            ]
            average_heights.append(calculate_average(heights))
        result_heights.append(average_heights)
        print(average_heights)
    return result_heights
def calculate_average(heights):
    return sum(heights) / len(heights)
if __name__ == "__main__":
    test_heights()