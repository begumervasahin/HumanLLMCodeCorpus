
from difflib import Differ
from pprint import pprint
text1 = '''  1. Beautiful is better than ugly.
      2. Explicit is better than implicit.
      3. Simple is better than complex.
      4. Complex is better than complicated.
    '''.splitlines(keepends=True)
text2 = '''  1. Beautiful is better than ugly.
      3.   Simple is better than complex.
      4. Complicated is better than complex.
      5. Flat is better than nested.
    '''.splitlines(keepends=True)
differ = Differ()
differences = list(differ.compare(text1, text2))
pprint(differences)
with open('output.txt', 'w') as output_file:
    output_file.writelines(differences)