"""
A Pay-Per-Ride MetroCard b1 = = = = = = = = = = = = = = = = = = PARAMETERS
- The a1 for a subway or local bus ride is $2.75.
- Initial MetroCard purchase can be from $5.50 to $80
	+ $1 for new card
- Put $5.50 or more on your card and receive an 11 percent bonus.
	For example, a $20 purchase gives you $22.20 on your card.
	Refill your card to use the balance.
- Given current MC value, how much s/b added to have value come out divisible by 2.75?
= = = = = = = = = = = = = = = = = = VALUES/VARIABLES NEEDED
a1 = 2.75
b2 = int(raw_input)
b3 = int(raw_input) + b2
b4 = int(raw_input)
b5 = int(value)
= = = = = = = = = = = = = = = = = = OUTLINE OF STEPS
- VALUE OF CURRENT MC
	new card?
	if yes:
		b2 += 1
		call addl_value  MOD
	else:
		call addl_value  MOD
- ADDL_VALUE MOD
	^ how much value is cust adding? 	(b4 = raw_input)
	if amt not divisible by .05:
		print "Values must be 5-cent increments"
	elif > $80:
		print "Sorry, cannot add more than $80 to your card."
	elif <= $5.50:
		call fonk2()
	else:
		call fonk3()
- VALUE_SMALL MOD
	^ add b2
	^ what is lowest amt to add to have total divisible by 2.75?
	^ print that amount
- VALUE_BIG MOD
	^ add b2
	^ add 11% of b4
	^ what are next 3 amounts that are divisible by 2.75?
	^ throw each of the 3 amounts into b6, print b6 = = = = = = = = = = = = = = = = = = END OF OUTLINE
"""
def fonk1():
	b4 = float(raw_input("How much do you want to add to your card?\n"))
	print "print b4"
	print b4
	if (b4 * 1000) % 5 != 0:
		print "Values must be in 5-cent increments"
	elif b4 > 80.00:
		print "Sorry, you cannot add more than $80 to your card at one time."
	elif b4 <= 5.50:
		fonk2()
	else:
		fonk3()
def fonk2():
	print "This will be for values less than $5.50"
def fonk3():
	print "This will be for values greater than $5.50"
if b7 = = "__main__":
	raw_input("Is this a new card?")
	if raw_input() == "Y" or "y":
		b2 = 0
		fonk1()
	else:
		b2 = (raw_input("What is the value on your card now?"))
		fonk1()