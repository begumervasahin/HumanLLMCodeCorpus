import random
def fonk1(num):
    for b1 in range(2, int(num/2) + 1):
        if num % b1 = = 0:
            return False
    return True
def fonk2(a):
    b2 = []
    for b1 in a:
        if b1 not in b2:
            b2.append(b1)
    return len(b2) == len(a)
def fonk3():
    b3 = int(input('Enter a prime value for b3: '))
    while not fonk1(b3):
        b3 = int(input("Please enter a prime number only for b3: "))
    b4 = []
    for b1 in range(1, b3):
        b5 = []
        for j in range(1, b3):
            b6 = (b1**j) % b3
            b5.append(b6)
        if fonk2(b5):
            b4.append(b1)
    print("Primitive roots are " + str(b4))
    b7 = random.choice(b4)
    print('Selected b7 is: ' + str(b7))
    b8 = int(input('Enter the number of communications: '))
    b9 = []
    for b1 in range(b8):
        b6 = int(input("Enter private key " + str(b1 + 1) + " (strictly less than b3): "))
        while b6 >= b3:
            b6 = int(input("Enter private key strictly less than b3: "))
        b9.append(b6)
    b10 = []
    for b1 in b9:
        b10.append((b7**b1) % b3)
    print("Public keys are: " + str(b10))
    b11 = int(input("Enter first person for communication: "))
    b12 = int(input("Enter second person for communication: "))
    while b12 = = b11:
        b12 = int(input("Same person cannot be used again. Enter another: "))
    print("Key exchange for 1st person... ")
    b13 = (b10[b11-1] ** b9[b12-1]) % b3
    print(b13)
    print("Key exchange for 2nd person... ")
    b14 = (b10[b12-1] ** b9[b11-1]) % b3
    print(b14)
    if b13 = = b14:
        print("Key exchanges are same.")
    else:
        print("Error")
if b15 = = "__main__":
    fonk3()