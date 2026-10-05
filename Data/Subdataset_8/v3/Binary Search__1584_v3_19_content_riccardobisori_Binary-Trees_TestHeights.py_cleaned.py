import random
import ABR
import RB
import sys
import pickle
sys.setrecursionlimit(4400)
def test_heights():
    test_data = load_test_data()
    result_abr = test_height_abr(test_data)
    result_rb = test_height_rb(test_data)
    save_results(result_abr, "result_height_abr.p")
    save_results(result_rb, "result_height_rb.p")
def load_test_data():
    return pickle.load(open("tests.p", "rb"))
def test_height_abr(test_data):
    elements, range_elements = test_data
    print_header("Average heights of Binary Search Trees for random elements. 3 executions.")
    result_random_height_abr = []
    for p in elements:
        average_heights = []
        for i in range_elements:
            heights = []
            for _ in range(3):
                height = calculate_abr_height(p, i)
                heights.append(height)
            average_height = sum(heights) / len(heights)
            average_heights.append(average_height)
        result_random_height_abr.append(average_heights)
        print(average_heights)
    return result_random_height_abr
def calculate_abr_height(p, i):
    abr_tree = ABR.BinarySearchTree()
    for _ in range(p):
        abr_tree.insert(random.randint(0, i))
    return abr_tree.get_height(abr_tree.root)
def test_height_rb(test_data):
    elements, range_elements = test_data
    print_header("Average heights of Red-Black Trees for random elements. 10 executions.")
    result_random_height_rb = []
    result_ordered_height_rb = []
    for p in elements:
        random_heights = []
        ordered_heights = []
        for i in range_elements:
            random_heights = []
            for _ in range(10):
                height = calculate_rb_height(p, i)
                random_heights.append(height)
            random_average_height = sum(random_heights) / len(random_heights)
            result_random_height_rb.append(random_average_height)
        print(result_random_height_rb)
    print_header("Average heights of Red-Black Trees for ordered elements. 5 executions.")
    for p in elements:
        for _ in range(len(range_elements)):
            ordered_heights = []
            for _ in range(5):
                height = calculate_rb_height(p)
                ordered_heights.append(height)
            ordered_average_height = sum(ordered_heights) / len(ordered_heights)
            result_ordered_height_rb.append(ordered_average_height)
        print(result_ordered_height_rb)
    return result_random_height_rb, result_ordered_height_rb
def calculate_rb_height(p, i=None):
    rb_tree = RB.RedBlackTree()
    if i:
        for _ in range(p):
            rb_tree.insert(random.randint(0, i))
    else:
        for k in range(p):
            rb_tree.insert(k)
    return rb_tree.get_height(rb_tree.root)
def print_header(header_text):
    print("\n" + "=" * 100)
    print(header_text)
    print("Columns: ranges [20, 200, 1000, 10000000].")
    print("Lines: elements [10, 50, 500, 1000, 10000, 50000]")
    print("=" * 100 + "\n")
def save_results(results, file_name):
    pickle.dump(results, open(file_name, "wb"))
if __name__ == "__main__":
    test_heights()