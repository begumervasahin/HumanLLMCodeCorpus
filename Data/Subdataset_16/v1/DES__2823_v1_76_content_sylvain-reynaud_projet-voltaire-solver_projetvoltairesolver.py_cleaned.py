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
        with open(os.path.join(b2, filename), 'r', b4 = "utf-8") as f:
            b5 = f.read()
            try:
                b6 = b5.index("[\"java.util.ArrayList")
                b7 = b5.index("]") + 1
                b5 = b5[b6:b7]
                b5 = b5.replace("\\", "\\\\")
                b3 += json.loads(b5)
            except (ValueError, json.JSONDecodeError):
                pass
b3 = [x for x in b3 if "\\x3C" in x]
while True:
    b8 = input("Entrer la b8 donnee : ")
    b9 = difflib.get_close_matches(b8, b3)
    if b9:
        b10 = unquote(b9[0].replace("\\x", "%"))
        b11 = re.sub(r"<B>(.*?)<\/B>", lambda match: colored(match.group(1), "green"), b10)
        print(b11, '\n')
    else:
        print(colored("Il n'y a pas de faute", "green"), '\n')