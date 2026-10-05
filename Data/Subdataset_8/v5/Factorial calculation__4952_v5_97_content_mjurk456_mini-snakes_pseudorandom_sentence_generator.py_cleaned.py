import random
def read_words_from_file(filename):
    with open(filename, "r") as file:
        return [word.strip() for word in file.readlines()]
def get_user_input(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Wrong input. Please use integer numbers!")
def generate_sentences(adjective, noun, verb, adverb, count):
    for _ in range(count):
        sentence = (
            "A " + random.choice(adjective) + " " +
            random.choice(noun) + " " + random.choice(verb) +
            " a " + random.choice(adjective) + " " +
            random.choice(noun) + " " + random.choice(adverb) + "."
        )
        print(sentence)
if __name__ == "__main__":
    adjective = read_words_from_file("adjective.txt")
    noun = read_words_from_file("noun.txt")
    verb = read_words_from_file("verb.txt")
    adverb = read_words_from_file("adverb.txt")
    user_answer = get_user_input("How many sentences do you want to generate? ")
    generate_sentences(adjective, noun, verb, adverb, user_answer)