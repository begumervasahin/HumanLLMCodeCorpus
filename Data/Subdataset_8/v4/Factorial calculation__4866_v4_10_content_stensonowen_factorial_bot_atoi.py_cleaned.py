import re
import text2num
Translations = {
    'a': 'one',
    'dozen': 'twelve',
    'and': '',
}
valid_tokens = set(["hundred"])
for d in [text2num.Small, text2num.Magnitude, Translations]:
    valid_tokens = valid_tokens.union(set(d.keys()))
def prep(text):
    text = re.sub("[\W_]", ' ', text)
    tokens = []
    for token in text.split():
        tr = Translations.get(token)
        if tr is not None and tr != '':
            tokens.append(Translations[token])
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
    return text2num.text2num(tokens[first:])
def atoi(text):
    tokens = prep(text)
    result = text2num.text2num(tokens)
    return result
