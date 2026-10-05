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
    tokens = re.findall(r"[\w']+|[.,!?;]", text)
    for i, token in enumerate(tokens):
        tr = Translations.get(token)
        if tr:
            tokens[i] = tr
        elif tr is None:
            tokens[i] = token
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
text = "a dozen apples and two hundred oranges"
print("Extracted number:", extract(text))
print("Converted to integer:", atoi(text))