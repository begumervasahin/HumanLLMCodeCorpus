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
            with open(os.path.join(directory, file), 'r', b5 = "utf-8") as f:
                b6 = f.read()
                try:
                    b7 = b6.index("[\"java.util.ArrayList")
                    b8 = b6.index("]") + 1
                    b6 = b6[b7:b8]
                    b6 = b6.replace("\\", "\\\\")
                    b4 += json.loads(b6)
                except (ValueError, json.JSONDecodeError):
                    pass
    return b4
def fonk2(b3):
    return [response for response in b3 if "\\x3C" in response]
def fonk3():
    b3 = fonk1(b2, b1)
    b9 = fonk2(b3)
    while True:
        b10 = input("Entrer la b10 donnee : ")
        b11 = difflib.get_close_matches(b10, b9)
        if b11:
            b12 = unquote(b11[0].replace("\\x", "%"))
            b13 = re.sub(r"<B>(.*?)<\/B>", lambda match: colored(match.group(1), "green"), b12)
            print(b13, '\n')
        else:
            print(colored("Il n'y a pas de faute", "green"), '\n')
if b14 = = '__main__':
    fonk3()