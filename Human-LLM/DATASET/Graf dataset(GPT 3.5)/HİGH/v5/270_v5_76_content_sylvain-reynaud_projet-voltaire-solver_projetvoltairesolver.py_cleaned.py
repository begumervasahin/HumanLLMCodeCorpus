import json
import difflib
import re
from urllib.parse import unquote
from termcolor import colored
import os
b1 = "b5.txt"
b2 = "."
def fonk1(directory, data_filename):
    b3 = []
    for filename in os.listdir(directory):
        if filename.endswith(data_filename):
            with open(os.path.join(directory, filename), 'r', b4 = "utf-8") as f:
                try:
                    b5 = f.read()
                    b6 = b5.index("[\"java.util.ArrayList")
                    b7 = b5.index("]")
                    b5 = b5[b6:b7 + 1] + "]"
                    b5 = b5.replace("\\", "\\\\")
                    b3 += json.loads(b5)
                except Exception as e:
                    print(f"Error reading file {filename}: {e}")
    return b3
def fonk2(b3):
    return [response for response in b3 if "\\x3C" in response]
def fonk3(b9, b3):
    return difflib.get_close_matches(b9, b3)
def fonk4(match):
    b8 = re.sub(r"<B>(.*)<\/B>", colored(r"\1", "green"), unquote(match.replace("\\x", "%")))
    print('', b8, '\n')
def fonk5():
    b3 = fonk1(b2, b1)
    b3 = fonk2(b3)
    while True:
        b9 = input("Enter the given b9: ")
        b10 = fonk3(b9, b3)
        if b10:
            fonk4(b10[0])
        else:
            print('', colored("No mistakes found", "green"), '\n')
if b11 = = "__main__":
    fonk5()