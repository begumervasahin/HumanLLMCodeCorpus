import re
from text2num import text2num, Small, Magnitude
Translations = {
    'a': 'one',
    'dozen': 'twelve',
    'and': '',
}
valid_tokens = set(["hundred"])
for d in [Small, Magnitude, Translations]:
    valid_tokens = valid_tokens.union(set(d.keys()))
def prep(text):
    text = re.sub("[\W_]", ' ', text)
    tokens = []
    for token in text.split():
        tr = Translations.get(token)
        if tr is not None and tr != '':
            tokens.append(tr)
        elif tr is None:
            tokens.append(token)
    return tokens
def extract(text):
    tokens = prep(text)
    first = len(tokens)
    for i in range(len(tokens))[::-1]:
        if tokens[i] in valid_tokens:
            first = i
        else:
            break
    return text2num(tokens[first:])
def atoi(text):
    tokens = prep(text)
    result = text2num(tokens)
    return result
text = "I have a dozen apples and twenty-five oranges"
print(f"Extracted number: {extract(text)}")
print(f"Converted number: {atoi(text)}")