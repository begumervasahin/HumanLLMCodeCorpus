import fnmatch, re
regex = fnmatch.translate('*.txt')
regex
reobj = re.compile(regex)
reobj.match('foobar.txt')