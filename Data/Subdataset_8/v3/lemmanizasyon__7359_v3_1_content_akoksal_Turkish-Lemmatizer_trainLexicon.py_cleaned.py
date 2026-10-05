import pickle
import sys
def load_word(dataset):
    word_dict = {}
    def load_from_file(file_path):
        with open(file_path, 'rb') as file:
            return pickle.load(file)
    if dataset == "wiktionary":
        word_list = load_from_file('Datasets/wiktionary.pkl')
        word_dict = {find_id({}, word): ["kok", find_id({}, word)] for word in word_list}
    elif dataset == "zargan":
        zargan_dict = load_from_file('Datasets/zargan.pkl')
        word_dict = {find_id({}, word): ["kok", find_id({}, word)] for word in zargan_dict.keys()}
    return word_dict
def find_id(word_dict, word):
    count = 1
    while f"{word}_{count}" in word_dict:
        count += 1
    return f"{word}_{count}"
def generate(word_dict, action):
    new_dict = {}
    def add_entry(base_word, suffix, new_suffix, event):
        new_dict[find_id(word_dict, base_word + new_suffix)] = [event, f"{base_word}_{suffix}"]
    if action == "negative_suffix":
        for word, value_list in word_dict.items():
            index = word.index("_") + 1
            base_word = word[:index - 1] if word.endswith("mak") or word.endswith("mek") else word[:-3]
            if base_word.endswith(("p", "ç", "t")):
                add_entry(base_word, index, "b", "unsuz yumusamasi")
            elif base_word.endswith("k"):
                add_entry(base_word, index, "g" if base_word.endswith("nk") else "ð", "unsuz yumusamasi")
    return new_dict
def append_dict(revised_dict, new_dict):
    for word, value_list in new_dict.items():
        revised_dict[find_id(revised_dict, word.split("_")[0])] = value_list
    return revised_dict
def main():
    dataset = "zargan"
    if len(sys.argv) > 1:
        dataset = sys.argv[1]
    word_dict = load_word(dataset)
    word_dict = append_dict(word_dict, generate(word_dict, "negative_suffix"))
    print("Negative verbs are added.")
    word_dict = append_dict(word_dict, generate(word_dict, "fiil"))
    print("Zero infinitive forms of verbs are added.")
    revised_dict = dict(word_dict)
    for action in ["consonant_softening", "vowel_becoming_close", "vowel_dropping"]:
        new_dict = generate(word_dict, action)
        revised_dict = append_dict(revised_dict, new_dict)
        print(f"{action.capitalize().replace('_', ' ')} forms are added.")
    with open('revisedDict.pkl', 'wb') as file:
        pickle.dump(revised_dict, file)
    print("Transformed lexicon is saved to revisedDict.pkl")
if __name__ == "__main__":
    main()