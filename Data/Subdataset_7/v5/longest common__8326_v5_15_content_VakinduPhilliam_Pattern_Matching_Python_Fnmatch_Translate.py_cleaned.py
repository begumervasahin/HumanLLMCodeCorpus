import fnmatch
import re
b1 = '*.txt'
b2 = fnmatch.translate(b1)
b3 = re.compile(b2)
b4 = b3.match('foobar.txt')