import random
def read_words_from_file(file_path):
    with open(file_path, "r") as file:
        words = file.readlines()
    return [word.strip() for word in words]
def generate_sentence(adjective, noun, verb, adverb):
    sentence = (
        "A " + random.choice(adjective) +
        " " + random.choice(noun) +
        " " + random.choice(verb) +
        " a " + random.choice(adjective) +
        " " + random.choice(noun) +
        " " + random.choice(adverb) + "."
    )
    return sentence
def generate_sentences():
    adjective = read_words_from_file("adjective.txt")
    noun = read_words_from_file("noun.txt")
    verb = read_words_from_file("verb.txt")
    adverb = read_words_from_file("adverb.txt")
    while True:
        try:
            user_answer = int(input("How many sentences do you want to generate? "))
            break
        except ValueError:
            print("Wrong input, please use integer numbers!")
    for _ in range(user_answer):
        sentence = generate_sentence(adjective, noun, verb, adverb)
        print(sentence)
if __name__ == "__main__":
    generate_sentences()