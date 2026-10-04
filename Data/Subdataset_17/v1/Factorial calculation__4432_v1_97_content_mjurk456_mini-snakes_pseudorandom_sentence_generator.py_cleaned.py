import random
def load_words(file_path):
    with open(file_path, 'r') as file:
        words = file.readlines()
    return [word.strip() for word in words]
def generate_sentence(adjectives, nouns, verbs, adverbs):
    sentence = (
        f"A {random.choice(adjectives)} {random.choice(nouns)} "
        f"{random.choice(verbs)} a {random.choice(adjectives)} "
        f"{random.choice(nouns)} {random.choice(adverbs)}."
    )
    return sentence
def main():
    adjectives = load_words("adjective.txt")
    nouns = load_words("noun.txt")
    verbs = load_words("verb.txt")
    adverbs = load_words("adverb.txt")
    while True:
        try:
            num_sentences = int(input("How many sentences do you want to generate? "))
            if num_sentences <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
    for _ in range(num_sentences):
        print(generate_sentence(adjectives, nouns, verbs, adverbs))
if __name__ == "__main__":
    main()