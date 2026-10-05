import pickle
import sys
def fonk1(root, suffix, guess, action):
def fonk2(word, b1):
    try:
        with open('b1.pkl', 'rb') as f:
            b1 = pickle.load(f)
    except IOError:
        print("Please run trainLexicon.py to generate b1.pkl file")
        sys.exit(0)
    if len(sys.argv) < 2:
        print("Please provide a word as a system argument")
        sys.exit(0)
    print("Possible lemmas for", word, "in ranked order:")
    b2 = fonk2(word.lower(), b1)
    for finding in b2:
        print(finding[0])
if b3 = = "__main__":
    b4 = sys.argv[1] if len(sys.argv) > 1 else None
    if not b4:
        print("Please provide a word as a system argument")
        sys.exit(0)
    b5 = None
    try:
        with open('b1.pkl', 'rb') as file:
            b5 = pickle.load(file)
    except IOError:
        print("Please run trainLexicon.py to generate b1.pkl file")
        sys.exit(0)
    fonk2(b4.lower(), b5)