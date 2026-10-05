import random
import ABR
import RB
import sys
import pickle
sys.setrecursionlimit(4400)
def test_heights():
    test_heights_start = pickle.load(open("tests.p", "rb"))
    result_abr = test_height_abr(test_heights_start)
    result_rb = test_height_rb(test_heights_start)
    pickle.dump(result_abr, open("resultHeightABR.p", "wb"))
    pickle.dump(result_rb, open("resultHeightRB.p", "wb"))
def test_height_abr(test_heights_start):
    elements = test_heights_start[0]
    range_elements = test_heights_start[1]
    print("\n" + "=" * 100)
    print("Average heights of Binary Search Trees for random elements. 3 executions.")
    print("Columns: ranges [20, 200, 1000, 10000000].")
    print("Lines: elements [10, 50, 500, 1000, 10000, 50000]")
    print("=" * 100 + "\n")
    result_random_height_abr = []
    for p in elements:
        average_array_height_abr = []
        for i in range_elements:
            array_height_abr = []
            for _ in range(3):
                abr_tree = ABR.BinarySearchTree()
                for _ in range(p):
                    abr_tree.insert(random.randint(0, i))
                height_abr = abr_tree.get_height(abr_tree.root)
                array_height_abr.append(height_abr)
            average_height_abr = sum(array_height_abr) / len(array_height_abr)
            average_array_height_abr.append(average_height_abr)
        result_random_height_abr.append(average_array_height_abr)
        print(average_array_height_abr)
    return result_random_height_abr
def test_height_rb(test_heights_start):
    elements = test_heights_start[0]
    range_elements = test_heights_start[1]
    print("\n" + "=" * 100)
    print("Average heights of Red-Black Trees for random elements. 10 executions.")
    print("Columns: ranges [20, 200, 1000, 10000000].")
    print("Lines: elements [10, 50, 500, 1000, 10000, 50000]")
    print("=" * 100 + "\n")
    result_random_height_rb = []
    result_ordered_height_rb = []
    for p in elements:
        average_array_height_rb = []
        for i in range_elements:
            array_height_rb = []
            for _ in range(10):
                rb_tree = RB.RedBlackTree()
                for _ in range(p):
                    rb_tree.insert(random.randint(0, i))
                height_rb = rb_tree.get_height(rb_tree.root)
                array_height_rb.append(height_rb)
            average_height_rb = sum(array_height_rb) / len(array_height_rb)
            average_array_height_rb.append(average_height_rb)
        result_random_height_rb.append(average_array_height_rb)
        print(average_array_height_rb)
    print("\n" + "=" * 100)
    print("Average heights of Red-Black Trees for ordered elements. 5 executions.")
    print("Columns: ranges [20, 200, 1000, 10000000].")
    print("Lines: elements [10, 50, 500, 1000, 10000, 50000]")
    print("=" * 100 + "\n")
    for p in elements:
        average_array_ordered_height_rb = []
        for i in range(len(range_elements)):
            array_ordered_height_rb = []
            for _ in range(5):
                rb_tree = RB.RedBlackTree()
                for k in range(p):
                    rb_tree.insert(k)
                height_rb = rb_tree.get_height(rb_tree.root)
                array_ordered_height_rb.append(height_rb)
            average_ordered_height_rb = sum(array_ordered_height_rb) / len(array_ordered_height_rb)
            average_array_ordered_height_rb.append(average_ordered_height_rb)
        result_ordered_height_rb.append(average_array_ordered_height_rb)
        print(average_array_ordered_height_rb)
    return result_random_height_rb, result_ordered_height_rb
if __name__ == "__main__":
    test_heights()