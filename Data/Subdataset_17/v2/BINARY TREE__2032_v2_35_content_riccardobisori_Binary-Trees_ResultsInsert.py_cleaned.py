import pickle
import time
from random import randint
from BinarySearchTree import BinarySearchTree
from RedBlackTree import RedBlackTree
def test_insert():
    test_values = pickle.load(open("testInsert.p", "rb"))
    elements, range_elements = test_values
    bst_times = []
    for num_elements in elements:
        bst = BinarySearchTree(randint(0, range_elements[0]))
        start_time = time.time()
        for _ in range(num_elements):
            bst.insert(randint(0, range_elements[0]))
        end_time = time.time()
        bst_times.append(end_time - start_time)
    rbt_times = []
    for num_elements in elements:
        rbt = RedBlackTree(randint(0, range_elements[0]))
        start_time = time.time()
        for _ in range(num_elements):
            rbt.insert(randint(0, range_elements[0]))
        end_time = time.time()
        rbt_times.append(end_time - start_time)
    with open("resultInsertABR.p", "wb") as f:
        pickle.dump((elements, bst_times), f)
    with open("resultInsertRB.p", "wb") as f:
        pickle.dump((elements, rbt_times), f)
if __name__ == "__main__":
    test_insert()
import pickle
import matplotlib.pyplot as plt
def load_results(filename):
    with open(filename, "rb") as f:
        return pickle.load(f)
def plot_results(elements, times, title, ylabel):
    plt.plot(elements, times)
    plt.xlabel('Number of Elements')
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()
def main():
    elements = (10, 50, 1000, 10000, 50000)
    range_elements = (30, 1500, 1000000000)
    test_values = (elements, range_elements)
    with open("testInsert.p", "wb") as f:
        pickle.dump(test_values, f)
    import TestInsert
    TestInsert.test_insert()
    result_insert_abr = load_results("resultInsertABR.p")
    result_insert_rb = load_results("resultInsertRB.p")
    plot_results(result_insert_abr[0], result_insert_abr[1],
                 "Insertion Times in a Binary Search Tree\nwith elements previously inserted in ascending order",
                 "Insertion Time (seconds)")
    plot_results(result_insert_rb[0], result_insert_rb[1],
                 "Insertion Times in a Red-Black Tree\nwith elements previously inserted in ascending order",
                 "Insertion Time (seconds)")
if __name__ == "__main__":
    main()