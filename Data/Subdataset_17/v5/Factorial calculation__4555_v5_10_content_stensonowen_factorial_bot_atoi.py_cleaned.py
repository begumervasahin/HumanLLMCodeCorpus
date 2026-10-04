import re
from text2num import text2num, Small, Magnitude
TRANSLATIONS = {
    'a': 'one',
    'dozen': 'twelve',
    'and': '',
}
VALID_TOKENS = set(["hundred"])
for dictionary in [Small, Magnitude, TRANSLATIONS]:
    VALID_TOKENS.update(dictionary.keys())
def preprocess_text(text):
    text = re.sub(r"[\W_]", ' ', text)
    tokens = []
    for token in text.split():
        translated = TRANSLATIONS.get(token)
        if translated:
            tokens.append(translated)
        else:
            tokens.append(token)
    return tokens
def extract_numeric_value(text):
    tokens = preprocess_text(text)
    first_valid_index = len(tokens)
    for i in reversed(range(len(tokens))):
        if tokens[i] in VALID_TOKENS:
            first_valid_index = i
        else:
            break
    return text2num(tokens[first_valid_index:])
def text_to_integer(text):
    tokens = preprocess_text(text)
    return text2num(tokens)
if __name__ == "__main__":
    example_text = "I have a dozen apples and twenty-five oranges"
    print(f"Extracted number: {extract_numeric_value(example_text)}")
    print(f"Converted number: {text_to_integer(example_text)}")