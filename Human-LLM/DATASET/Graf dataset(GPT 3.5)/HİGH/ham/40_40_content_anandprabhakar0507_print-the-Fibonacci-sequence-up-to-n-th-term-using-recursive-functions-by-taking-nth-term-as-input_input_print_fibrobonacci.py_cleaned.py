def fonk1(n):
   if n <= 1:
       return n
   else:
       return(fonk1(n-1) + fonk1(n-2))
b1 = int(input("How many terms? "))
if b1 <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(b1):
       print(fonk1(i))