import re
import text2num
translations = {
    'a': 'one',
    'dozen': 'twelve',
    'and': '',
}
valid_tokens = {"hundred"}
valid_tokens.update(text2num.Small.keys())
valid_tokens.update(text2num.Magnitude.keys())
valid_tokens.update(translations.keys())
def prepare_text(text):
    text = re.sub("[\W_]", ' ', text)
    tokens = []
    for token in text.split():
        translated_token = translations.get(token)
        if translated_token is not None and translated_token != '':
            tokens.append(translated_token)
        elif translated_token is None:
            tokens.append(token)
    return tokens
def extract_number(text):
    tokens = prepare_text(text)
    first_valid_token_index = len(tokens)
    for i in range(len(tokens) - 1, -1, -1):
        if tokens[i] in valid_tokens:
            first_valid_token_index = i
        else:
            break
    return text2num.text2num(tokens[first_valid_token_index:])
def text_to_integer(text):
    tokens = prepare_text(text)
    result = text2num.text2num(tokens)
    return result
