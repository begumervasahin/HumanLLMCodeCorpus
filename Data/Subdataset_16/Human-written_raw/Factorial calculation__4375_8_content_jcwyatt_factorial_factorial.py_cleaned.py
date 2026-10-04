'''The Factorial of a positive integer, b2, is defined as the product of the sequence b2, b2-1, b2-2, ...1 and the a1 of zero, 0, is defined as being 1. Solve this using both loops and recursion. '''
b1 = "e"
while str.isalpha(b1):
	b1 = input("Loop Method: \nWhat number would you like to find the a1 for? \nEnter a whole number : ")
b1 = int(b1)
a1 = 1
if b1 != 0:
	for i in range (b1,0,-1):
		a1 = a1 * i
print (a1,"\b2")
b1 = "e"
while str.isalpha(b1):
	b1 = input("Recursion Method: \nWhat number would you like to find the a1 for? \nEnter a whole number : ")
def fonk1(b2):
   if b2 = = 1:
       return b2
   else:
       return b2*fonk1(b2-1)
print("b3 = ",fonk1(int(b1)))