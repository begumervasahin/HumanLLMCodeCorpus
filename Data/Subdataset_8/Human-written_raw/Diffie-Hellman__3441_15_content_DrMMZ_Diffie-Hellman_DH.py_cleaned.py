import getpass
import re
def generators(p) :
    L = set()
    for x in range(1,p) :
        S_x = set()
        for i in range(1,p) :
            y = (x**i)%p
            S_x.add(y)
        print("<",x,"> =",S_x)
        if len(S_x) == p-1 :
            L.add(x)
    print("\nGenerators of Z mod",p,"are",L)
print()
print("------------------------------------------------------------")
print("     The Diffie-Hellman public key exchange protocol        ")
print("------------------------------------------------------------")
print()
p = input("Choose a prime: ")
p = int(p)
print()
generators(p)
print()
g = input("Choose a generator: ")
g = int(g)
print()
q = p-1
while True :
    print("Choose an integer in [",1,",",q,"]")
    a = getpass.getpass()
    if re.findall("[a-zA-Z]",a) or int(a) <= 0 or int(a) > q:
        print("Wrong format!")
    else :
        a = int(a)
        break
print()
s = (g**a)%p
print("Send:",s)
r = input("Receive: ")
r = int(r)
print()
k = (r**a)%p
print("The secret common key:",k)
print()