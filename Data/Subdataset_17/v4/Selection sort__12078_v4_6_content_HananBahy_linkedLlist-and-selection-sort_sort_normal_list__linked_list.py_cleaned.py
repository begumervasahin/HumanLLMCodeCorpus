import time
from random import randrange
from linkedlistuno import LinkedListUno
from selectionsort import selection_sort
def main():
    my_list = []
    my_linked_list = LinkedListUno()
    for _ in range(10000):
        num = randrange(-1000, 1001)
        my_list.insert(0, num)
        my_linked_list.add(num)
    start_time_list = time.time()
    selection_sort(my_list)
    end_time_list = time.time()
    start_time_linked_list = time.time()
    my_linked_list.selection_sort()
    end_time_linked_list = time.time()
    print("Time for normal list:", end_time_list - start_time_list)
    print("Time for linked list:", end_time_linked_list - start_time_linked_list)
if __name__ == "__main__":
    main()