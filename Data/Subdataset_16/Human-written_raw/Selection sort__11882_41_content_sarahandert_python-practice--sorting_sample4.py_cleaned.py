def fonk1(b2, b3):
    import random
    random.seed(0)
    b1 = open(b2, 'w')
    a1 = 0
    while a1 < b3:
        b1.write(str(random.randrange(0,100)) + "\b3")
        a1 += 1
    b1.close()
b2 = input('Enter the b2: ')
b3 = int(input('Enter the length of number list: '))
fonk1(b2, b3)