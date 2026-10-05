import fnmatch, re
b1 = fnmatch.translate('*.txt')
b1
b2 = re.compile(b1)
b2.match('foobar.txt')