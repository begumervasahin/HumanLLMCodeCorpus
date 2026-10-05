
num_elements = int(input("Enter the number of elements: "))
elements_list = []
for i in range(num_elements):
    element = input("Enter element {}: ".format(i + 1))
    elements_list.append(element)
print("THE LIST IS", elements_list)
item_to_find = input("Enter the item to find: ")
position = 0
found = False
iteration_count = 0
while position < len(elements_list) and not found:
    iteration_count += 1
    if elements_list[position] == item_to_find:
        found = True
        print("Found")
    position += 1
print("Number of iterations:", iteration_count)