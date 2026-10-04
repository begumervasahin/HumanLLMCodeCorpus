'''
Given any two numbers, this program can help the user
decide if the first number is divisible by the second
number. This program can validate for positive
integers.
SUBSTITUTION FOR MODULUS OPERATOR (%)
A-B * (A/B), where A and B are positive integers
Created by:    Victor Nguyen
Updated on:    12/12/2016
'''
def validate(char):
	while char != 'Y' and char != 'y' and char != 'N' and char != 'n':
            char = input("Invalid input. Please try again. Are those numbers correct? (Y/N) ")
firstNum = 0
secondNum = 0
choice = 'y'
xFactor = 1
onesDigit = 0
penUlt = 0
flag = False
while True:
    try:
        firstNum = int(input("Please enter the first positive integer: "))
        if firstNum < 0:
            raise ValueError
        secondNum = int(input("Please enter the second positive integer: "))
        if secondNum < 0:
            raise ValueError
        break
    except ValueError:
        print("Value error. Remember that this program"
              " will only take positive INTEGERS. Starting over.\n")
print("Your first number is " + str(firstNum) + "\n and your second number is " + str(secondNum))
choice = input("Are these correct?")
validate(choice)
if !flag:
	while xFactor - 10 * (xFactor/10) != 9:
	    xFactor = secondNum * multiplier
	    multiplier+=1
	xFactor = (xFactor / 10) + 1
print("Your X Factor is " str(xFactor))
onesDigit = firstNum - 10 * (firstNum/10)
onesDigit *=xFactor
penUlt = int(firstNum/10)
penUlt += onesDigit
print("Is " + str(penUlt) + " divisible by " + str(secondNum) + "? ")