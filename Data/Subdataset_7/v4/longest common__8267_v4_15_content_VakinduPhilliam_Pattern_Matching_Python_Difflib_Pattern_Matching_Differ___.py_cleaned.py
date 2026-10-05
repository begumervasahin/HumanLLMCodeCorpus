
b1 = '''
1. Beautiful is better than ugly.
2. Explicit is better than implicit.
3. Simple is better than complex.
4. Complex is better than complicated.
'''.splitlines(b2 = True)
b3 = '''
1. Beautiful is better than ugly.
3.   Simple is better than complex.
4. Complicated is better than complex.
5. Flat is better than nested.
'''.splitlines(b2 = True)
from difflib import Differ
b4 = Differ()
b5 = list(b4.compare(b1, b3))
from pprint import pprint
pprint(b5)
import sys
sys.stdout.writelines(b5)