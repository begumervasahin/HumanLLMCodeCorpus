"""
A Pay-Per-Ride MetroCard costs
= = = = = = = = = = = = = = = = = = PARAMETERS
- The fare for a subway or local bus ride is $2.75.
- Initial MetroCard purchase can be from $5.50 to $80
	+ $1 for new card
- Put $5.50 or more on your card and receive an 11 percent bonus.
	For example, a $20 purchase gives you $22.20 on your card.
	Refill your card to use the balance.
- Given current MC value, how much s/b added to have value come out divisible by 2.75?
= = = = = = = = = = = = = = = = = = VALUES/VARIABLES NEEDED
fare = 2.75
card_value_1 = int(raw_input)
card_value_2 = int(raw_input) + card_value_1
cust_adding = int(raw_input)
card_value_final = int(value)
= = = = = = = = = = = = = = = = = = OUTLINE OF STEPS
- VALUE OF CURRENT MC
	new card?
	if yes:
		card_value_1 += 1
		call addl_value  MOD
	else:
		call addl_value  MOD
- ADDL_VALUE MOD
	^ how much value is cust adding? 	(cust_adding = raw_input)
	if amt not divisible by .05:
		print "Values must be 5-cent increments"
	elif > $80:
		print "Sorry, cannot add more than $80 to your card."
	elif <= $5.50:
		call value_small()
	else:
		call value_big()
- VALUE_SMALL MOD
	^ add card_value_1
	^ what is lowest amt to add to have total divisible by 2.75?
	^ print that amount
- VALUE_BIG MOD
	^ add card_value_1
	^ add 11% of cust_adding
	^ what are next 3 amounts that are divisible by 2.75?
	^ throw each of the 3 amounts into list, print list
= = = = = = = = = = = = = = = = = = END OF OUTLINE
"""
def addl_value():
	cust_adding = float(raw_input("How much do you want to add to your card?\n"))
	print "print cust_adding"
	print cust_adding
	if (cust_adding * 1000) % 5 != 0:
		print "Values must be in 5-cent increments"
	elif cust_adding > 80.00:
		print "Sorry, you cannot add more than $80 to your card at one time."
	elif cust_adding <= 5.50:
		value_small()
	else:
		value_big()
def value_small():
	print "This will be for values less than $5.50"
def value_big():
	print "This will be for values greater than $5.50"
if __name__ == "__main__":
	raw_input("Is this a new card?")
	if raw_input() == "Y" or "y":
		card_value_1 = 0
		addl_value()
	else:
		card_value_1 = (raw_input("What is the value on your card now?"))
		addl_value()