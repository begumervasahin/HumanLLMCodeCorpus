
title = "A Self-Assessment Test for Congruence"
adjectives = [
    "ANXIOUS", "ATTRACTIVE", "CARELESS", "DEPRESSED", "DISHONEST", "ENERGETIC", "FUNNY", "HAPPY", "HONEST",
    "INTELLIGENT", "KIND", "LAZY", "OPTIMISTIC", "ORGANIZED", "OUT-GOING", "PLAIN", "RELAXED", "SAD", "SERIOUS",
    "SHY", "SLOPPY", "STRONG", "UNHELPFUL", "WEAK"
]
list_A = []
list_B = []
dict_A = {'item1': 3, 'item2': 6}
dict_B = {'item2': 4}
print("Sum of values in dictionary B:", sum(dict_B.values()))
print("Choose 10 of the following adjectives by entering their number:")
for index, item in enumerate(adjectives, start=1):
    print(f"{index}\t{item}")
list_A = [2, 7, 10, 11, 13, 14, 18, 19, 22, 1]
if len(list_A) < 10:
    print("You entered fewer than 10 items")
else:
    print("Thank you; here is your list:")
    print(list_A)
Introduction = '''
The following test illustrates a "Q-sort", a self-assessment procedure for measuring congruence,
a state of internal consistency which Carl Rogers saw as important to healthy personality growth.
Please read the directions and complete part A before proceeding to part B.
'''
Instruction_A = '''
Part A: Select ten adjectives from the list that best describe you. Rank them in order of significance.
Write them down and set them aside. Shuffle the words together and move to part B.
'''
Instruction_B = '''
Part B: Select ten adjectives that describe your personal ideal. Rank them in order of significance,
without referring to the list from part A. Write them down in ranked order.
'''
Scoring = '''
To score, assign values to the ranks in each list (10 for the first term, 1 for the last).
Identify any adjectives not in both lists and change their value to zero.
Then, use the following formula: (sum of list A + sum of list B) / 1.1 = score.
The score range is 0-100, with 100 representing a perfect match of self and ideal self.
'''
