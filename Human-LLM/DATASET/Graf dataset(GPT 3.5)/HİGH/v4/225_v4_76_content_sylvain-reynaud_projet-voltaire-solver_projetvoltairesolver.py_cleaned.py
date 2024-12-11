import json
import difflib
import re
from urllib.parse import unquote
from termcolor import colored
import os
b1 = "b5.txt"
b2 = "."
def fonk1(b2, b1):
    b3 = []
    for filename in os.listdir(b2):
        if filename.endswith(b1):
            with open(os.path.join(b2, filename), 'r', b4 = "utf-8") as f:
                try:
                    b5 = f.read()
                    b5 = b5[b5.index("[\"java.util.ArrayList"):b5.index("]")] + "]"
                    b5 = b5.replace("\\", "\\\\")
                    b3 += json.loads(b5)
                except Exception as e:
                    print(f"Error reading file {filename}: {e}")
    return b3
def fonk2(b3):
    return [response for response in b3 if "\\x3C" in response]
def fonk3():
    b3 = fonk1(b2, b1)
    b3 = fonk2(b3)
    while True:
        b6 = input("Enter the given b6: ")
        b7 = difflib.get_close_matches(b6, b3)
        if b7:
            b8 = re.sub(r"<B>(.*)<\/B>", colored(r"\1", "green"), unquote(b7[0].replace("\\x", "%")))
            print('', b8, '\n')
        else:
            print('', colored("No mistakes found", "green"), '\n')
if b9 = = "__main__":
    fonk3()