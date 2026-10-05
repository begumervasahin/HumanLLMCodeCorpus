import re
import text2num
TRANSLATIONS = {
    'a': 'one',
    'dozen': 'twelve',
    'and': '',
}
VALID_TOKENS = set(["hundred"])
for dictionary in [text2num.Small, text2num.Magnitude, TRANSLATIONS]:
    VALID_TOKENS |= set(dictionary.keys())
def tokenize_text(text):
    tokens = re.findall(r"[\w']+|[.,!?;]", text)
    for i, token in enumerate(tokens):
        translation = TRANSLATIONS.get(token)
        if translation:
            tokens[i] = translation
    return tokens
def extract_numeric_value(text):
    tokens = tokenize_text(text)
    first_valid_index = len(tokens)
    for i, token in enumerate(reversed(tokens)):
        if token in VALID_TOKENS:
            first_valid_index = len(tokens) - i - 1
        else:
            break
    return text2num.text2num(tokens[first_valid_index:])
def text_to_integer(text):
    tokens = tokenize_text(text)
    numeric_value = text2num.text2num(tokens)
    return numeric_value
text = "a dozen apples and two hundred oranges"
extracted_number = extract_numeric_value(text)
converted_integer = text_to_integer(text)
print("Extracted number:", extracted_number)
print("Converted to integer:", converted_integer)