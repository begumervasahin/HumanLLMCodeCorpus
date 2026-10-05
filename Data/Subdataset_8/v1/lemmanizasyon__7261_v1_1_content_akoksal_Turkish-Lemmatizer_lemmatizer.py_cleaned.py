import re
import json
import pickle
import sys
def check(root, suffix, guess, action):
def findPos(kelime, revisedDict):
def checkSuffixValidation(suff):
try:
    with open('revisedDict.pkl', 'rb') as f:
        revisedDict = pickle.load(f)
except IOError:
    print("Please run trainLexicon.py to generate revisedDict.pkl file")
    sys.exit(0)
if len(sys.argv) < 2:
    print("Please provide a word as a system argument")
    sys.exit(0)
word = sys.argv[1]
print("Possible lemmas for", word, "in ranked order:")
findings = findPos(word.lower(), revisedDict)
for finding in findings:
    print(finding[0])