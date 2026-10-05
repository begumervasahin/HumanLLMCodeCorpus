
title = "A Self-Assessment Test for Congruence"
adjectives = [
    "ANXIOUS", "ATTRACTIVE", "CARELESS", "DEPRESSED", "DISHONEST", "ENERGETIC", "FUNNY", "HAPPY",
    "HONEST", "INTELLIGENT", "KIND", "LAZY", "OPTIMISTIC", "ORGANIZED", "OUT-GOING", "PLAIN",
    "RELAXED", "SAD", "SERIOUS", "SHY", "SLOPPY", "STRONG", "UNHELPFUL", "WEAK"
]
list_A = []
list_B = []
dict_A = {'item1': 3, 'item2': 6}
dict_B = {'item2': 4}
sum(dict_B.values())
print("Choose 10 of the following adjectives by entering their number.")
for index, item in enumerate(adjectives):
    print(str(index + 1) + "\t" + str(item))
list_A = [2, 7, 10, 11, 13, 14, 18, 19, 22, 1]
if len(list_A) < 10:
    print("You entered less than 10 items")
else:
    print("Thank you; here is your list:")
    print(list_A)
Introduction = 'The following demonstration test illustrates a version of a "Q-sort", a self-assessment procedure for measuring congruence, a state of internal consistency which Carl Rogers saw as important to healthy personality growth. A brief discussion follows the test, which is self-scoring (as described below). Please read the directions, and complete part A before going on to part B!'
Instruction_A = 'Part A Please select ten adjectives from the following list which you feel describe what you are like. (You may find it useful to write them down on a sheet of paper, or print this page, and cut them out individually.) Try to be as honest and accurate as possible in making the choices to describe yourself. (For example, do not omit an adjective that describes you well if it happens to be somewhat negative, like "anxious".) Once you have selected the ten which best describe you, then arrange them in order, from the most important/significant aspects, to those which are least significant in describing your personality. Write them down, with the rank order, on a piece of paper, then fold it and put it aside. Place all the words together, shuffle them, and then go on to part B.'
Instruction_B = 'Part B You are now requested to do the same task again, but this time selecting ten terms to describe what you wish you were like--that is, your personal ideal. (For example, you may feel that you are shy, but would like to be extraverted.) Do not refer to the list from part A in making your choices! Once you have selected ten, arrange them in rank order, from the most important/significant, to those which are relatively unimportant in your imagined ideal. As in part A, write them down, in ranked order, on a piece of paper.'
Scoring = "Take the two lists from parts A and B, and assign values to the ranks in each list, with the first term = 10, the second term = 9, etc. (the last term will have a value of 1). Now, identify any adjectives that do not appear in both lists (appearing in different positions does not matter). For any terms which do not appear in both lists, change the value to zero. For terms which appear in both lists, give the value assigned for the term in list A to the term in list B. Then, using the values you have assigned to the two lists (including the zero terms), apply the following formula:\n\n(sum of list A + sum of list B) / (1.1) = score\n\nThe score range is from 0 to 100, with 100 representing a perfect match of self and ideal self (i.e., complete congruence); if half the terms appear in both lists (but with different ranks), the median score would be approximately 50. In general, the lower the score, the less congruent is the relationship between one's self and ideal self. (For further information on these concepts, refer to the textbook, or the links to other sites.)\n\nNote that this demonstration is not meant to be a serious clinical device, and no claims are made as to its validity or reliability! (Even the scoring system is an approximation, as a correlation coefficient would provide a more precise indicator.) It is provided here simply as a learning tool, to better understand Rogers' concepts of self, ideal self, and congruence."