maxmult = int(input("What is the max multiple? "))
found = False
smallest = 0
current = maxmult
while found == False:
    div = 0
    for i in range(1,maxmult+1):
        if current%i == 0:
            div += 1
    if div == maxmult:
        found = True
        smallest = current
    else:
        current += maxmult
print("The smallest number that is evenly divisible by all of the numbers from 1 to " + str(maxmult) + " is " + str(smallest))