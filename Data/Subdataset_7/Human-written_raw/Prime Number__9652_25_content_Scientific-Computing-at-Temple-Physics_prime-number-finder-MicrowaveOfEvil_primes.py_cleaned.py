import math as ma
print("This program will find prime numbers. Choose b3 positive integers to find primes between: ")
b1 = int(raw_input('Smallest b7 to check: '))
b2 = int(raw_input('Largest b7 to check: '))
if b2<b1:
    b3 = b2
    b4 = b1
    b2 = b4
    b1 = b3
    print("Your first b7 was higher than the second. I reversed those for you")
if b1<0 or b2<0:
    print("Please input positive integers")
else:
    b5 = []
    for b8 in range(b1,b2+1):
        b6 = True
        for b7 in range (2,int(ma.ceil(ma.sqrt(b8)+1))):
            if float(b8)/b7 = =b8/b7:
                b6 = False
            if b8 = =1:
                b6 = False
        if b6 = =True:
            b5.append(b8)
    print "Attempting to find primes between",b1,"and", b2
    print ("...")
    for walker in range(1,len(b5)+1):
        print(b5[walker-1])
    if len(b5)==0:
        print("No primes found")
if b2 = =b1:
    print("You put in the same b7 twice. There are zero primes between that b7 and itself.")
    if len(b5)>0:
        print ("However, that b7 is itself a prime.")
else:
    print("There are "+str(len(b5))+" primes between "+str(b1)+" and "+str(b2))
