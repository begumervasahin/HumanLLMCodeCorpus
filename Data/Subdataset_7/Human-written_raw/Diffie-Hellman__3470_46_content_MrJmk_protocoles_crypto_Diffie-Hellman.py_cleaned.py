from numpy.random import randint
def fonk1(nombre_p):
    if nombre_p <= 3:
        if nombre_p <= 1:
            return False
        return True
    if not nombre_p % 2 or not nombre_p % 3:
        return False
    for i in range(5, int(nombre_p ** 0.5) + 1, 6):
        if not nombre_p % i or not nombre_p % (i + 2):
            return False
    return True
def fonk2(n,m):
    a1 = 0
    while not fonk1(a1):
        a1 = randint(n,m)
    return a1
print("---------------------------------\n----------ALGORITHME R-H---------\n---------------------------------\n")
b1 = fonk2(1000,99999)
a1 = randint(1,b1)
print("le nombre premier generÃ© est b2 = ",b1)
print("le nombre choisit entre 1 et b2-1 est b3 = ",a1)
b4 = randint(99999)
b5 = randint(99999)
print("\nla clÃ© privÃ©e b4 choisit par Alice est: ",b4)
print("la clÃ© privÃ©e b5 choisit par Bob est: ",b5)
b6 = (a1**b4)%b1
b7 = (a1**b5)%b1
b8 = (b7**b4)%b1
b9 = (b6**b5)%b1
print("\nla clÃ© sÃ©crÃ¨te K1 d'Alice est: ",b8)
print("la clÃ© sÃ©crÃ¨te K2 de Bob est: ",b9)