b1 = int(input("Please enter an integer you want to check"))
b2 = True
a1 = 2
while a1 < b1:
     if (b1 % a1)==0:
        b2 = False
        break
     a1 = a1+1
if b2 = = True:
     print(str(b1) + " is a prime number")
else:
     print(str(b1) + " is not a prime number")