import fnmatch
import re
b1 = fnmatch.translate('*.txt')
b2 = re.compile(b1)
b3 = b2.match('foobar.txt')