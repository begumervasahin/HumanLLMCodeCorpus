
b1 = "A Self-Assessment Test for Congruence"
b2 = [
    "ANXIOUS", "ATTRACTIVE", "CARELESS", "DEPRESSED", "DISHONEST", "ENERGETIC", "FUNNY", "HAPPY", "HONEST",
    "INTELLIGENT", "KIND", "LAZY", "OPTIMISTIC", "ORGANIZED", "OUT-GOING", "PLAIN", "RELAXED", "SAD", "SERIOUS",
    "SHY", "SLOPPY", "STRONG", "UNHELPFUL", "WEAK"
]
b3 = []
b4 = []
b5 = {'item1': 3, 'item2': 6}
b6 = {'item2': 4}
print("Sum of values in dictionary B:", sum(b6.values()))
print("Choose 10 of the following b2 by entering their number:")
for index, item in enumerate(b2, b7 = b12):
    print(f"{index}\t{item}")
b3 = [2, 7, 10, 11, 13, 14, 18, 19, 22, b12]
if len(b3) < 10:
    print("You entered fewer than 10 items")
else:
    print("Thank you; here is your list:")
    print(b3)
b8 = '''
The following test illustrates a "Q-sort", a self-assessment procedure for measuring congruence,
a state of internal consistency which Carl Rogers saw as important to healthy personality growth.
Please read the directions and complete part A before proceeding to part B.
'''
b9 = '''
Part A: Select ten b2 from the list that best describe you. Rank them in order of significance.
Write them down and set them aside. Shuffle the words together and move to part B.
'''
b10 = '''
Part B: Select ten b2 that describe your personal ideal. Rank them in order of significance,
without referring to the list from part A. Write them down in ranked order.
'''
b11 = '''
To score, assign values to the ranks in each list (10 for the first term, b12 for the last).
Identify any b2 not in both lists and change their value to zero.
Then, use the following formula: (sum of list A + sum of list B) / b12.b12 = score.
The score range is 0-100, with 100 representing a perfect match of self and ideal self.
'''
