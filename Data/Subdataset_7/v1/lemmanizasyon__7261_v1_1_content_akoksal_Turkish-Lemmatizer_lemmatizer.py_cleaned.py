import re
import json
import pickle
import sys
def fonk1(root, suffix, guess, action):
def fonk2(kelime, b1):
def fonk3(suff):
try:
    with open('b1.pkl', 'rb') as f:
        b1 = pickle.load(f)
except IOError:
    print("Please run trainLexicon.py to generate b1.pkl file")
    sys.exit(0)
if len(sys.argv) < 2:
    print("Please provide a b2 as a system argument")
    sys.exit(0)
b2 = sys.argv[1]
print("Possible lemmas for", b2, "in ranked order:")
b3 = fonk2(b2.lower(), b1)
for finding in b3:
    print(finding[0])