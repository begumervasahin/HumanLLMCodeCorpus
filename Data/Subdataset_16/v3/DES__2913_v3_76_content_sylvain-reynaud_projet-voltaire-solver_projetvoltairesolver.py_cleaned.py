import json
import difflib
import re
from urllib.parse import unquote
from termcolor import colored
import os
b1 = "b5.txt"
b2 = "."
def fonk1(directory, filename):
    b3 = []
    for file in os.listdir(directory):
        if file.endswith(filename):
            with open(os.path.join(directory, file), 'r', b4 = "utf-8") as f:
                b5 = f.read()
                try:
                    b6 = b5.index("[\"java.util.ArrayList")
                    b7 = b5.index("]") + 1
                    b8 = b5[b6:b7].replace("\\", "\\\\")
                    b3.extend(json.loads(b8))
                except (ValueError, json.JSONDecodeError):
                    pass
    return b3
def fonk2(b10):
    return [response for response in b10 if "\\x3C" in response]
def fonk3(possibility):
    b9 = unquote(possibility.replace("\\x", "%"))
    return re.sub(r"<B>(.*?)<\/B>", lambda match: colored(match.group(1), "green"), b9)
def fonk4():
    b10 = fonk1(b2, b1)
    b11 = fonk2(b10)
    while True:
        b12 = input("Entrer la b12 donnee : ")
        b13 = difflib.get_close_matches(b12, b11)
        if b13:
            b14 = fonk3(b13[0])
            print(b14, '\n')
        else:
            print(colored("Il n'y a pas de faute", "green"), '\n')
if b15 = = '__main__':
    fonk4()