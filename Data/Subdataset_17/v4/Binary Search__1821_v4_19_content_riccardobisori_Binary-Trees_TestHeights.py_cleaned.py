import random
import ABR
import RB
import sys
import pickle
sys.setrecursionlimit(4400)
def test_heights():
    test_heights_start = pickle.load(open("tests.p", "rb"))
    result_ABR = test_height_ABR(test_heights_start)
    result_RB = test_height_RB(test_heights_start)
    pickle.dump(result_ABR, open("resultHeightABR.p", "wb"))
    pickle.dump(result_RB, open("resultHeightRB.p", "wb"))
def test_height_ABR(test_heights_start):
    elements = test_heights_start[0]
    range_elements = test_heights_start[1]
    result_random_height_ABR = []
    print("\n", "=" * 100)
    print("Average heights of Binary Search Trees for random elements. 3 executions.")
    print("Columns: ranges [20, 200, 1000, 10000000].")
    print("Lines: elements [10, 50, 500, 1000, 10000, 50000]")
    print("=" * 100, "\n")
    for num_elements in elements:
        average_heights = []
        for range_limit in range_elements:
            heights = []
            for _ in range(3):
                ABR_tree = ABR.BinarySearchTree()
                for _ in range(num_elements):
                    ABR_tree.insert(random.randint(0, range_limit))
                height_ABR = ABR_tree.getHeight(ABR_tree.root)
                heights.append(height_ABR)
            average_heights.append(sum(heights) / len(heights))
        result_random_height_ABR.append(average_heights)
        print(average_heights)
    return result_random_height_ABR
def test_height_RB(test_heights_start):
    elements = test_heights_start[0]
    range_elements = test_heights_start[1]
    result_random_height_RB = []
    result_ordered_height_RB = []
    print("\n", "=" * 100)
    print("Average heights of Red-Black Trees for random elements. 10 executions.")
    print("Columns: ranges [20, 200, 1000, 10000000].")
    print("Lines: elements [10, 50, 500, 1000, 10000, 50000]")
    print("=" * 100, "\n")
    for num_elements in elements:
        average_heights = []
        for range_limit in range_elements:
            heights = []
            for _ in range(10):
                RB_tree = RB.RedBlackTree()
                for _ in range(num_elements):
                    RB_tree.insert(random.randint(0, range_limit))
                height_RB = RB_tree.getHeight(RB_tree.root)
                heights.append(height_RB)
            average_heights.append(sum(heights) / len(heights))
        result_random_height_RB.append(average_heights)
        print(average_heights)
    print("\n", "=" * 100)
    print("Average heights of Red-Black Trees for ordered elements. 5 executions.")
    print("Columns: ranges [20, 200, 1000, 10000000].")
    print("Lines: elements [10, 50, 500, 1000, 10000, 50000]")
    print("=" * 100, "\n")
    for num_elements in elements:
        average_heights = []
        for _ in range(len(range_elements)):
            heights = []
            for _ in range(5):
                RB_tree = RB.RedBlackTree()
                for k in range(num_elements):
                    RB_tree.insert(k)
                height_RB = RB_tree.getHeight(RB_tree.root)
                heights.append(height_RB)
            average_heights.append(sum(heights) / len(heights))
        result_ordered_height_RB.append(average_heights)
        print(average_heights)
    return result_random_height_RB, result_ordered_height_RB
if __name__ == "__main__":
    test_heights()