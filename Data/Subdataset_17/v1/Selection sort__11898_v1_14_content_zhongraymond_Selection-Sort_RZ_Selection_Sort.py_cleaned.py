import random
def random_number():
    return random.sample(range(100001), 100)
def selection_sort(li):
    print("Original list:")
    print(li)
    n = len(li)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if li[j] < li[min_index]:
                min_index = j
        li[i], li[min_index] = li[min_index], li[i]
    print("Sorted list:")
    print(li)
    return li
if __name__ == "__main__":
    random_list = random_number()
    selection_sort(random_list)