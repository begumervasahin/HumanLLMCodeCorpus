import random
def load_words(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]
def generate_sentence(adjectives, nouns, verbs, adverbs):
    return (
        f"A {random.choice(adjectives)} {random.choice(nouns)} "
        f"{random.choice(verbs)} a {random.choice(adjectives)} "
        f"{random.choice(nouns)} {random.choice(adverbs)}."
    )
def get_number_of_sentences():
    while True:
        try:
            num_sentences = int(input("How many sentences do you want to generate? "))
            if num_sentences > 0:
                return num_sentences
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
def main():
    adjectives = load_words("adjective.txt")
    nouns = load_words("noun.txt")
    verbs = load_words("verb.txt")
    adverbs = load_words("adverb.txt")
    num_sentences = get_number_of_sentences()
    for _ in range(num_sentences):
        print(generate_sentence(adjectives, nouns, verbs, adverbs))
if __name__ == "__main__":
    main()