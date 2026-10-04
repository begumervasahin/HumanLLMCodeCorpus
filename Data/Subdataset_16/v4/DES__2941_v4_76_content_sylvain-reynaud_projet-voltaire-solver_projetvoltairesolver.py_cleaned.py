import json
import difflib
import re
from urllib.parse import unquote
from termcolor import colored
import os
b1 = "b6.txt"
b2 = "."
b3 = []
def fonk1(directory, filename):
    b4 = []
    for file in os.listdir(directory):
        if file.endswith(filename):
            with open(file, 'r', b5 = "utf-8") as f:
                b6 = f.read()
                try:
                    b7 = b6.index("[\"java.util.ArrayList")
                    b8 = b6.index("]") + 1
                    b9 = b6[b7:b8].replace("\\", "\\\\")
                    b4.extend(json.loads(b9))
                except (ValueError, json.JSONDecodeError):
                    pass
    return b4
def fonk2(b3):
    return [response for response in b3 if "\\x3C" in response]
def fonk3(possibility):
    b10 = unquote(possibility.replace("\\x", "%"))
    return re.sub(r"<B>(.*?)<\/B>", lambda match: colored(match.group(1), "green"), b10)
def fonk4():
    b3 = fonk1(b2, b1)
    b11 = fonk2(b3)
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