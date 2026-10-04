names = ["", "", "ROSE", "ALGERNON", "CLARENCE", "VIOLET", "CECIL", "CUTHBERT"]
genders = ["", "", "FEMALE", "MALE", "MALE", "FEMALE", "MALE", "MALE"]
links = [0, 0]
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
    for index in range(2, len(names)):
        swap = False
        current = links[0]
        for index1 in range(2, len(names) - index + 1):
            previous = current
            current = links[current]
            following = links[current]
            if names[current] >= names[following]:
                swap = True
                temp = links[previous]
                links[previous] = links[current]
                links[current] = links[following]
                links[following] = temp
                current = following
        if not swap:
            break
if __name__ == "__main__":
    initialise()
    print("Initial links:", links)
    ripple_sort()
    print("Sorted links:", links)
    current = links[0]
    sorted_females = []
    while current != 0:
        sorted_females.append(names[current])
        current = links[current]
    current = links[1]
    sorted_males = []
    while current != 0:
        sorted_males.append(names[current])
        current = links[current]
    print("Sorted female names:", sorted_females)
    print("Sorted male names:", sorted_males)