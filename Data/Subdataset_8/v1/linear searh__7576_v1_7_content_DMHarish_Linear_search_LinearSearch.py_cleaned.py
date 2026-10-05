import random
def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return True
    return False
data = [1, 2, 3, 4, 5, 6]
target = random.randrange(1, 10)
print("List:", data)
print("Target:", target)
result = linear_search(data, target)
if result:
    print("The target value is present in the list.")
else:
    print("The target value is not present in the list.")