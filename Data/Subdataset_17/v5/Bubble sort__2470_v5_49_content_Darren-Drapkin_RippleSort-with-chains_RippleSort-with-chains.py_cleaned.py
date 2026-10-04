names = ["", "", "ROSE", "ALGERNON", "CLARENCE", "VIOLET", "CECIL", "CUTHBERT"]
genders = ["", "", "FEMALE", "MALE", "MALE", "FEMALE", "MALE", "MALE"]
links = [0, 0] + [0] * (len(names) - 2)
def initialise():
    for index in range(2, len(names)):
        if genders[index] == "FEMALE":
            queue = 0
        elif genders[index] == "MALE":
            queue = 1
        else:
            continue
        links[index] = links[queue]
        links[queue] = index
def ripple_sort():
    for i in range(2, len(names)):
        swapped = False
        current = links[0]
        for j in range(2, len(names) - i + 1):
            previous = current
            current = links[current]
            following = links[current]
            if names[current] >= names[following]:
                swapped = True
                links[previous], links[current], links[following] = links[current], links[following], links[previous]
                current = following
        if not swapped:
            break
if __name__ == "__main__":
    initialise()
    print("Initial links:", links)
    ripple_sort()
    print("Sorted links:", links)
    def get_sorted_names(queue_index):
        sorted_names = []
        current = links[queue_index]
        while current != 0:
            sorted_names.append(names[current])
            current = links[current]
        return sorted_names
    sorted_females = get_sorted_names(0)
    sorted_males = get_sorted_names(1)
    print("Sorted female names:", sorted_females)
    print("Sorted male names:", sorted_males)