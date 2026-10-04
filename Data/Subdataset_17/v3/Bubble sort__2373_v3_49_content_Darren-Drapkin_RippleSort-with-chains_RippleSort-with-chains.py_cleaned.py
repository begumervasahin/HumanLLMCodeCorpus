names = ["", "", "ROSE", "ALGERNON", "CLARENCE", "VIOLET", "CECIL", "CUTHBERT"]
genders = ["", "", "FEMALE", "MALE", "MALE", "FEMALE", "MALE", "MALE"]
links = [0] * len(names)
def initialise():
    links[0] = 0
    links[1] = 0
    for index in range(2, len(names)):
        if genders[index] == "FEMALE":
            queue = 0
        else:
            queue = 1
        links[index] = links[queue]
        links[queue] = index
def ripple_sort(queue_start):
    for _ in range(2, len(names)):
        swapped = False
        current = links[queue_start]
        while current != 0 and links[current] != 0:
            next_index = links[current]
            if names[current] > names[next_index]:
                links[current], links[next_index] = links[next_index], links[current]
                swapped = True
            current = links[current]
        if not swapped:
            break
def print_sorted_list():
    print("Sorted Females:")
    current = links[0]
    while current != 0:
        print(names[current])
        current = links[current]
    print("\nSorted Males:")
    current = links[1]
    while current != 0:
        print(names[current])
        current = links[current]
def main():
    initialise()
    ripple_sort(0)
    ripple_sort(1)
    print_sorted_list()
if __name__ == "__main__":
    main()