import random
def fonk1(number):
    for b1 in range(2, int(number / 2) + 1):
        if number % b1 = = 0:
            return False
    return True
def fonk2(sequence):
    return len(set(sequence)) == len(sequence)
def fonk3(b4):
    b2 = []
    for i in range(1, b4):
        b3 = [(i ** j) % b4 for j in range(1, b4)]
        if fonk2(b3):
            b2.append(i)
    return b2
def fonk4():
    b4 = int(input('Enter a prime value for b4: '))
    while not fonk1(b4):
        b4 = int(input("Please enter a prime number only for b4: "))
    b2 = fonk3(b4)
    print("Primitive roots are: " + str(b2))
    b5 = random.choice(b2)
    print('Selected b5 is: ' + str(b5))
    b6 = int(input('Enter the number of communications: '))
    b7 = []
    for i in range(b6):
        b8 = int(input(f"Enter private key {i + 1} (strictly less than b4): "))
        while b8 >= b4:
            b8 = int(input("Enter private key strictly less than b4: "))
        b7.append(b8)
    b9 = [(b5 ** b8) % b4 for b8 in b7]
    print("Public keys are: " + str(b9))
    b10 = int(input("Enter the first person for communication: "))
    b11 = int(input("Enter the second person for communication: "))
    while b11 = = b10:
        b11 = int(input("Same person cannot be used again. Enter another: "))
    print("Key exchange for the first person...")
    b12 = (b9[b10 - 1] ** b7[b11 - 1]) % b4
    print("Shared secret key for first person:", b12)
    print("Key exchange for the second person...")
    b13 = (b9[b11 - 1] ** b7[b10 - 1]) % b4
    print("Shared secret key for second person:", b13)
    if b12 = = b13:
        print("Key exchanges are the same. Secure communication established.")
    else:
        print("Error in key exchange. Communication may not be secure.")
if b14 = = "__main__":
    fonk4()