
names = ["", "", "ROSE", "ALGERNON", "CLARENCE", "VIOLET", "CECIL", "CUTHBERT"]
genders = ["", "", "FEMALE", "MALE", "MALE", "FEMALE", "MALE", "MALE"]
links = [0, 0]
def initialise():
    for index in range(2, len(names)):
        if genders[index] == "FEMALE":
            que = 0
            links[index] = links[que]
            links[que] = index
        if genders[index] == "MALE":
            que = 1
            links[index] = links[que]
            links[que] = index
def ripple_sort():
    for index in range(2, len(names)):
        swop = False
        current = links[0]
        for index1 in range(2, len(names) - index):
            previous = current
            current = links[current]
            following = links[current]
            if names[current] >= names[following]:
                swop = True
                temp = links[previous]
                links[previous] = links[current]
                links[current] = links[following]
                links[following] = temp
                current = following
        swop = False
        if not swop:
            return
initialise()
ripple_sort()
print("Sorted names:", [names[index] for index in links if index != 0])