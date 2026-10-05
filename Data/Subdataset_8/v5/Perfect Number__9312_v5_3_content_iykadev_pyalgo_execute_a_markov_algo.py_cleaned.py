import re
def extract_replacements(grammar):
    replacements = []
    syntax_re = r
    for matchobj in re.finditer(syntax_re, grammar):
        if matchobj.group('rule'):
            pattern = matchobj.group('pat')
            replacement = matchobj.group('repl')
            termination = bool(matchobj.group('term'))
            replacements.append((pattern, replacement, termination))
    return replacements
def replace(text, replacements):
    while True:
        for pattern, replacement, termination in replacements:
            if pattern in text:
                text = text.replace(pattern, replacement, 1)
                if termination:
                    return text
                break
        else:
            return text
grammar = '''\
A -> apple
B -> bag
S -> .shop
T -> the
the shop -> my brother
a never used -> .terminating rule
'''
text = "I bought a B of As from T S."
if __name__ == '__main__':
    replacements = extract_replacements(grammar)
    result = replace(text, replacements)
    print(result)