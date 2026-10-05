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
def tokenize_text(text):
    tokens = re.findall(r"[\w']+|[.,!?;]", text)
    for i, token in enumerate(tokens):
        translation = Translations.get(token)
        if translation:
            tokens[i] = translation
    return tokens
def extract_numeric_value(text):
    tokens = tokenize_text(text)
    first_valid_index = len(tokens)
    for i in range(len(tokens))[::-1]:
        if tokens[i] in valid_tokens:
            first_valid_index = i
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