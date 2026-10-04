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
print("Length of text1:", len(text1))
print("Last character of the first line in text1:", repr(text1[0][-1]))
d = Differ()
result = list(d.compare(text1, text2))
pprint(result)
import sys
sys.stdout.writelines(result)