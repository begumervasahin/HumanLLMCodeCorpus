import random
adverb = []
noun = []
adjective = []
verb = []
with open("verb.txt", "r") as fverb:
    verb = [word.strip() for word in fverb.readlines()]
with open("adverb.txt", "r") as fadverb:
    adverb = [word.strip() for word in fadverb.readlines()]
with open("noun.txt", "r") as fnoun:
    noun = [word.strip() for word in fnoun.readlines()]
with open("adjective.txt", "r") as fadj:
    adjective = [word.strip() for word in fadj.readlines()]
while True:
    try:
        user_answer = int(input("How many sentences do you want to generate? "))
        break
    except ValueError:
        print("Wrong input. Please use integer numbers!")
for _ in range(user_answer):
    sentence = (
        "A " + random.choice(adjective) + " " +
        random.choice(noun) + " " + random.choice(verb) +
        " a " + random.choice(adjective) + " " +
        random.choice(noun) + " " + random.choice(adverb) + "."
    )
    print(sentence)