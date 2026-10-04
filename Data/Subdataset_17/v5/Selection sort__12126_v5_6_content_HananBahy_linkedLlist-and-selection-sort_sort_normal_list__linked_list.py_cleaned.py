import time
from random import randrange
from linkedlistuno import LinkedListUno
from selectionsort import selection_sort
def populate_lists(num_elements, value_range):
    my_list = []
    my_linked_list = LinkedListUno()
    for _ in range(num_elements):
        num = randrange(*value_range)
        my_list.append(num)
        my_linked_list.add(num)
    return my_list, my_linked_list
def measure_sort_time(sort_function, data_structure):
    start_time = time.time()
    sort_function(data_structure)
    end_time = time.time()
    return end_time - start_time
def main():
    num_elements = 10000
    value_range = (-1000, 1001)
    my_list, my_linked_list = populate_lists(num_elements, value_range)
    list_sort_time = measure_sort_time(selection_sort, my_list.copy())
    linked_list_sort_time = measure_sort_time(my_linked_list.selection_sort, my_linked_list)
    print("Time for normal list:", list_sort_time)
    print("Time for linked list:", linked_list_sort_time)
if __name__ == "__main__":
    main()