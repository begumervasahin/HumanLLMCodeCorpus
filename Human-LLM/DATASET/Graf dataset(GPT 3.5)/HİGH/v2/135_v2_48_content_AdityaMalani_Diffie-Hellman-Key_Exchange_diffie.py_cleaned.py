import random
def fonk1(number):
    for b1 in range(2, int(number/2) + 1):
        if number % b1 = = 0:
            return False
    return True
def fonk2(sequence):
    b2 = []
    for item in sequence:
        if item not in b2:
            b2.append(item)
    return len(b2) == len(sequence)
def fonk3(b5):
    b3 = []
    for i in range(1, b5):
        b4 = [(i**j) % b5 for j in range(1, b5)]
        if fonk2(b4):
            b3.append(i)
    return b3
def fonk4():
    b5 = int(input('Enter a prime value for b5: '))
    while not fonk1(b5):
        b5 = int(input("Please enter a prime number only for b5: "))
    b3 = fonk3(b5)
    print("Primitive roots modulo b5 are: " + str(b3))
    b6 = random.choice(b3)
    print('Selected b6 is: ' + str(b6))
    b7 = int(input('Enter the number of communications: '))
    b8 = []
    for i in range(b7):
        b9 = int(input("Enter private key " + str(i + 1) + " (strictly less than b5): "))
        while b9 >= b5:
            b9 = int(input("Enter private key strictly less than b5: "))
        b8.append(b9)
    b10 = [(b6**b9) % b5 for b9 in b8]
    print("Public keys are: " + str(b10))
    b11 = int(input("Enter the first person for communication: "))
    b12 = int(input("Enter the second person for communication: "))
    while b12 = = b11:
        b12 = int(input("Same person cannot be used again. Enter another: "))
    print("Key exchange for the first person...")
    b13 = (b10[b11 - 1] ** b8[b12 - 1]) % b5
    print(b13)
    print("Key exchange for the second person...")
    b14 = (b10[b12 - 1] ** b8[b11 - 1]) % b5
    print(b14)
    if b13 = = b14:
        print("Key exchanges are the same.")
    else:
        print("Error")
if b15 = = "__main__":
    fonk4()