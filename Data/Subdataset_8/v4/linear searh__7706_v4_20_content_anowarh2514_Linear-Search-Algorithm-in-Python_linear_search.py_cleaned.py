def linear_search(lst, target):
    index = 0
    while index < len(lst):
        if lst[index] == int(target):
            global position
            position = index
            return True
        index += 1
    return False
position = -1
lst = [21, 33, 45, 9, 24, 9, 34, 7, 88, 96, 54, 35, 66, 77]
target_number = input("Enter the number you want to search for: ")
if linear_search(lst, target_number):
    print("The number is found at position:", position + 1)
else:
    print("Number not found.")