
max_multiple = int(input("What is the max multiple? "))
found = False
smallest = 0
current = max_multiple
while not found:
    div_count = 0
    for i in range(1, max_multiple + 1):
        if current % i == 0:
            div_count += 1
    if div_count == max_multiple:
        found = True
        smallest = current
    else:
        current += max_multiple
print(f"The smallest number that is evenly divisible by all of the numbers from 1 to {max_multiple} is {smallest}")