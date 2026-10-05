import json
import difflib
import re
from urllib.parse import unquote
from termcolor import colored
import os
def fonk1(b6, b5):
    b1 = []
    for filename in os.listdir(b6):
        if filename.endswith(b5):
            with open(os.path.join(b6, filename), 'r', b2 = "utf-8") as f:
                try:
                    b3 = f.read()
                    b3 = b3[b3.index("[\"java.util.ArrayList"):b3.index("]")] + "]"
                    b3 = b3.replace("\\", "\\\\")
                    b1 += json.loads(b3)
                except Exception as e:
                    print(f"Error reading file {filename}: {e}")
    return b1
def fonk2(b1):
    return [x for x in b1 if "\\x3C" in x]
def fonk3(b7, b1):
    return difflib.get_close_matches(b7, b1)
def fonk4(match):
    b4 = re.sub(r"<B>(.*)<\/B>", colored(r"\1", "green"), unquote(match.replace("\\x", "%")))
    print('', b4, '\n')
def fonk5():
    b5 = "b3.txt"
    b6 = "."
    b1 = fonk1(b6, b5)
    b1 = fonk2(b1)
    while True:
        b7 = input("Enter the given b7: ")
        b8 = fonk3(b7, b1)
        if b8:
            fonk4(b8[0])
        else:
            print('', colored("There is no mistake", "green"), '\n')
if b9 = = "__main__":
    fonk5()