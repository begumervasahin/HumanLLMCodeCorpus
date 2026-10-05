
n = int(input("Enter the number of elements: "))
li = []
for i in range(0, n):
    li.append(input("Enter the element: "))
print("THE LIST IS", li)
item = input("Enter the item to find: ")
position = 0
found = False
counter = 0
while position < len(li) and not found:
    counter += 1
    if li[position] == item:
        found = True
        print("Found")
    position += 1
print("Number of iterations:", counter)