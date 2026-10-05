import pickle
import sys
def check(root, suffix, guess, action):
def find_possible_lemmas(word, revised_dict):
    try:
        with open('revisedDict.pkl', 'rb') as file:
            revised_dict = pickle.load(file)
    except IOError:
        print("Please run trainLexicon.py to generate revisedDict.pkl file")
        sys.exit(0)
    if len(sys.argv) < 2:
        print("Please provide a word as a system argument")
        sys.exit(0)
    print("Possible lemmas for", word, "in ranked order:")
    findings = find_possible_lemmas(word.lower(), revised_dict)
    for finding in findings:
        print(finding[0])
if __name__ == "__main__":
    word_to_check = sys.argv[1] if len(sys.argv) > 1 else None
    if not word_to_check:
        print("Please provide a word as a system argument")
        sys.exit(0)
    revised_dictionary = None
    try:
        with open('revisedDict.pkl', 'rb') as file:
            revised_dictionary = pickle.load(file)
    except IOError:
        print("Please run trainLexicon.py to generate revisedDict.pkl file")
        sys.exit(0)
    find_possible_lemmas(word_to_check.lower(), revised_dictionary)