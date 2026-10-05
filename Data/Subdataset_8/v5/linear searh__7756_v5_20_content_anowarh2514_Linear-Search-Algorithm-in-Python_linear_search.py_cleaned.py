def linear_search(lst, target):
    for index, number in enumerate(lst):
        if number == int(target):
            global position
            position = index
            return True
    return False
position = -1
number_list = [21, 33, 45, 9, 24, 9, 34, 7, 88, 96, 54, 35, 66, 77]
target_number = input("Enter the number you want to search for: ")
if linear_search(number_list, target_number):
    print("The number is found at position:", position + 1)
else:
    print("Number not found.")