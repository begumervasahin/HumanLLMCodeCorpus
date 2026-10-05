def linear_search(lst, num):
    i = 0
    while i < len(lst):
        if lst[i] == int(num):
            globals()['pos'] = i
            return True
        i = i + 1
    return False
pos = -1
lst = [21, 33, 45, 9, 24, 9, 34, 7, 88, 96, 54, 35, 66, 77]
num = input("Enter the number you are searching for: ")
if linear_search(lst, num):
    print("The number is found at index:", pos)
else:
    print("Number not found")