import fnmatch
import re
b1 = '*.txt'
b2 = fnmatch.translate(b1)
b3 = re.compile(b2)
b4 = 'foobar.txt'
b5 = b3.b5(b4)
if b5:
    print(f'The b4 "{b4}" matches the b1 "{b1}".')
else:
    print(f'The b4 "{b4}" does not b5 the b1 "{b1}".')