import pickle
import TestInsert
import matplotlib.pyplot as plt
def save_test_values(filename, values):
    with open(filename, "wb") as file:
        pickle.dump(values, file)
def load_results(filename):
    with open(filename, "rb") as file:
        return pickle.load(file)
def plot_results(x, y, xlabel, ylabel, title):
    plt.plot(x, y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()
elements = (10, 50, 1000, 10000, 50000)
range_elements = (30, 1500, 1000000000)
test_values = (elements, range_elements)
save_test_values("testInsert.p", test_values)
TestInsert.testInsert()
result_insert_abr = load_results("resultInsertABR.p")
result_insert_rb = load_results("resultInsertRB.p")
abr_x = (30, 100, 500, 1000)
plot_results(
    abr_x,
    result_insert_abr[1],
    'Range of Elements',
    'Insertion Time of (max(range) + 1)',
    "Insertion Times in a Binary Search Tree\n with Elements Previously Inserted in Ascending Order"
)
rb_x = (30, 100, 500, 1000, 1500)
plot_results(
    rb_x,
    result_insert_rb[1],
    'Range of Elements',
    'Insertion Time of (max(range) + 1)',
    "Insertion Times in a Red-Black Tree\n with Elements Previously Inserted in Ascending Order"
)