
names = ["", "", "ROSE", "ALGERNON", "CLARENCE", "VIOLET", "CECIL", "CUTHBERT"]
genders = ["", "", "FEMALE", "MALE", "MALE", "FEMALE", "MALE", "MALE"]
links = [0, 0]
def initialise_links():
    for index in range(2, len(names)):
        gender_index = 0 if genders[index] == "FEMALE" else 1
        links[index] = links[gender_index]
        links[gender_index] = index
def ripple_sort_names():
    for index in range(2, len(names)):
        swapped = False
        current = links[0]
        for index1 in range(2, len(names) - index):
            previous = current
            current = links[current]
            following = links[current]
            if names[current] >= names[following]:
                swapped = True
                temp = links[previous]
                links[previous] = links[current]
                links[current] = links[following]
                links[following] = temp
                current = following
        if not swapped:
            return
initialise_links()
ripple_sort_names()
sorted_names = [names[index] for index in links if index != 0]
print("Sorted names:", sorted_names)