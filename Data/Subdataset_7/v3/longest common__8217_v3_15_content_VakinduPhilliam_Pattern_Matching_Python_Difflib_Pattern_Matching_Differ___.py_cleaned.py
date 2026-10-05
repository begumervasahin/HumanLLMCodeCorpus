from difflib import Differ
from pprint import pprint
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
b4 = Differ()
b5 = list(b4.compare(b1, b3))
pprint(b5)
with open('output.txt', 'w') as output_file:
    output_file.writelines(b5)