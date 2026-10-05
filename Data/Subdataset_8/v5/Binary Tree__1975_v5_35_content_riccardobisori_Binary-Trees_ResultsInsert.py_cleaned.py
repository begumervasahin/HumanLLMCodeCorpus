import pickle
import TestInsert
import matplotlib.pyplot as plt
def save_test_values(filename, test_values):
    with open(filename, "wb") as file:
        pickle.dump(test_values, file)
def load_results(filename):
    with open(filename, "rb") as file:
        return pickle.load(file)
def plot_results(x_values, y_values, title):
    plt.plot(x_values, y_values)
    plt.xlabel('Range of elements')
    plt.ylabel('Time to insert (max(range) + 1)')
    plt.title(title)
    plt.show()
elements = (10, 50, 1000, 10000, 50000)
range_elements = (30, 1500, 1000000000)
test_values = (elements, range_elements)
save_test_values("test_insert.p", test_values)
TestInsert.test_insert()
result_insert_abr = load_results("result_insert_abr.p")
result_insert_rb = load_results("result_insert_rb.p")
x_abr = (30, 100, 500, 1000)
plot_results(x_abr, result_insert_abr[1], "Insertion times in a Binary Search Tree\n with elements previously inserted in ascending order")
x_rb = (30, 100, 500, 1000, 1500)
plot_results(x_rb, result_insert_rb[1], "Insertion times in a Red-Black Tree\n with elements previously inserted in ascending order")