import time
import random
from linkedlistuno import linkedlistuno
from selectionsort import selectionsort
def main():
    my_list = []
    my_linked_list = linkedlistuno()
    for _ in range(10000):
        random_int = random.randrange(-1000, 1001)
        my_list.insert(0, random_int)
        my_linked_list.add(random_int)
    start_time_list = time.time()
    selectionsort(my_list)
    end_time_list = time.time()
    start_time_linked_list = time.time()
    my_linked_list.selectionsort()
    end_time_linked_list = time.time()
    print("Time for normal list:", end_time_list - start_time_list)
    print("Time for linked list:", end_time_linked_list - start_time_linked_list)
if __name__ == "__main__":
    main()