from difflib import Differ
from pprint import pprint
import sys
def fonk1():
    b1 = '''  1. Beautiful is better than ugly.
          2. Explicit is better than implicit.
          3. Simple is better than complex.
          4. Complex is better than complicated.
        '''.splitlines(b2 = True)
    b3 = '''  1. Beautiful is better than ugly.
          3.   Simple is better than complex.
          4. Complicated is better than complex.
          5. Flat is better than nested.
        '''.splitlines(b2 = True)
    fonk2(b1)
    fonk3(b1)
    b4 = fonk4(b1, b3)
    pprint(b4)
    fonk5(b4)
def fonk2(text):
    print("Length of b1:", len(text))
def fonk3(text):
    if text:
        print("Last character of the first line in b1:", repr(text[0][-1]))
def fonk4(b1, b3):
    b5 = Differ()
    return list(b5.compare(b1, b3))
def fonk5(b4):
    sys.stdout.writelines(b4)
if b6 = = "__main__":
    fonk1()