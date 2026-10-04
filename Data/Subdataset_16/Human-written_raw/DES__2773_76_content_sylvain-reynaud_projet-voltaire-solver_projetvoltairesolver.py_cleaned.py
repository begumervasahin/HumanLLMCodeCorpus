import json
import difflib
import re
from urllib.parse import unquote
from termcolor import colored
import os
b1 = "b5.txt"
b2 = "."
b3 = []
for filename in os.listdir(b2):
    if filename.endswith(b1):
        with open(filename, 'r', b4 = "utf-8") as f:
            b5 = f.read()
            try:
                b5 = b5[b5.index("[\"java.util.ArrayList"):b5.index("]")] + "]"
                b5 = b5.replace("\\", "\\\\")
                b3 += json.loads(b5)
            except:
                pass
b3 = [x for x in b3 if "\\x3C" in x]
while(1):
    b6 = input("Entrer la b6 donnee : ")
    b7 = difflib.get_close_matches(b6, b3)
    if len(b7) != 0:
        b8 = re.sub(r"<B>(.*)<\/B>", colored(r"\1", "green"), unquote(b7[0].replace("\\x", "%")))
        print('', b8, '\n')
    else:
        print('', colored("Il n'y a pas de faute", "green"), '\n')