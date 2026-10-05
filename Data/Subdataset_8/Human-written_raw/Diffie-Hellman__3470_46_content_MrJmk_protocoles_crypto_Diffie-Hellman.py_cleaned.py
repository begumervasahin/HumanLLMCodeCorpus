from numpy.random import randint
def est_premier(nombre_p):
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
def genPrime(n,m):
    a = 0
    while not est_premier(a):
        a = randint(n,m)
    return a
print("---------------------------------\n----------ALGORITHME R-H---------\n---------------------------------\n")
p=genPrime(1000,99999)
a=randint(1,p)
print("le nombre premier generÃ© est P = ",p)
print("le nombre choisit entre 1 et P-1 est A = ",a)
x1=randint(99999)
x2=randint(99999)
print("\nla clÃ© privÃ©e x1 choisit par Alice est: ",x1)
print("la clÃ© privÃ©e x2 choisit par Bob est: ",x2)
y1=(a**x1)%p
y2=(a**x2)%p
k1=(y2**x1)%p
k2=(y1**x2)%p
print("\nla clÃ© sÃ©crÃ¨te K1 d'Alice est: ",k1)
print("la clÃ© sÃ©crÃ¨te K2 de Bob est: ",k2)