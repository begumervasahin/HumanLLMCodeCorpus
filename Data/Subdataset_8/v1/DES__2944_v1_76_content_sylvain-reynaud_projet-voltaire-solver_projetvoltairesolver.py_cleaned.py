import json
import difflib
import re
from urllib.parse import unquote
from termcolor import colored
import os
data_filename = "data.txt"
directory = "."
reponses = []
for filename in os.listdir(directory):
    if filename.endswith(data_filename):
        with open(os.path.join(directory, filename), 'r', encoding="utf-8") as f:
            data = f.read()
            try:
                data = data[data.index("[\"java.util.ArrayList"):data.index("]")] + "]"
                data = data.replace("\\", "\\\\")
                reponses += json.loads(data)
            except:
                pass
reponses = [x for x in reponses if "\\x3C" in x]
while True:
    phrase = input("Enter the given phrase: ")
    possibilites = difflib.get_close_matches(phrase, reponses)
    if len(possibilites) != 0:
        toPrint = re.sub(r"<B>(.*)<\/B>", colored(r"\1", "green"), unquote(possibilites[0].replace("\\x", "%")))
        print('', toPrint, '\n')
    else:
        print('', colored("There is no mistake", "green"), '\n')