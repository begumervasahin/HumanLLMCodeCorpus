import re
from text2num import text2num, Small, Magnitude
Translations = {
    'a': 'one',
    'dozen': 'twelve',
    'and': '',
}
valid_tokens = set(["hundred"])
for dictionary in [Small, Magnitude, Translations]:
    valid_tokens.update(dictionary.keys())
def prep(text):
    text = re.sub(r"[\W_]", ' ', text)
    tokens = []
    for token in text.split():
        translated = Translations.get(token)
        if translated:
            tokens.append(translated)
        else:
            tokens.append(token)
    return tokens
def extract(text):
    tokens = prep(text)
    first_valid_index = len(tokens)
    for i in reversed(range(len(tokens))):
        if tokens[i] in valid_tokens:
            first_valid_index = i
        else:
            break
    return text2num(tokens[first_valid_index:])
def atoi(text):
    tokens = prep(text)
    return text2num(tokens)
if __name__ == "__main__":
    example_text = "I have a dozen apples and twenty-five oranges"
    print(f"Extracted number: {extract(example_text)}")
    print(f"Converted number: {atoi(example_text)}")