import time
import random
from linkedlistuno import linkedlistuno
from selectionsort import selectionsort
def main():
    normal_list = []
    linked_list = linkedlistuno()
    for _ in range(10000):
        random_int = random.randrange(-1000, 1001)
        normal_list.insert(0, random_int)
        linked_list.add(random_int)
    start_time_normal_list = time.time()
    selectionsort(normal_list)
    end_time_normal_list = time.time()
    start_time_linked_list = time.time()
    linked_list.selectionsort()
    end_time_linked_list = time.time()
    print("Time for normal list:", end_time_normal_list - start_time_normal_list)
    print("Time for linked list:", end_time_linked_list - start_time_linked_list)
if __name__ == "__main__":
    main()