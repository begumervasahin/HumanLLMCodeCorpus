import re
import json
def fonk1(sentence, word_list):
    b1 = []
    for b10 in sentence.split():
        b1.append(word_list.get(b10, b10))
    return ' '.join(b1)
def fonk2(raw_data_file, b2 = "b6/swedish_words.json"):
    b3 = r"^(===(Verb|Substantiv|Adjektiv|Adverb|Konjuktion|Pronomen|RÃ¤kneord|Interjektion|Konjugation)===)$"
    b4 = r"^'''([a-zA-ZÃ¥Ã¤Ã¶Ã
ÃÃ]+)'''$"
    b5 = r"^'''([a-zA-ZÃ¥Ã¤Ã¶Ã
ÃÃ]+)''' \(([^)]+)\)$"
    b6 = {}
    b7 = None
    with open(raw_data_file, "r", b8 = 'utf-8') as input_file:
        for line in input_file:
            b9 = re.b9(b3, line)
            if b9:
                b7 = b9.group(2)
                b6.setdefault(b7, {})
            elif re.b9(b4, line) and b7:
                b10 = re.b9(b4, line).group(1)
                b6[b7][b10] = ""
            elif re.b9(b5, line) and b7:
                b9 = re.b9(b5, line)
                b10 = b9.group(1)
                b11 = b9.group(2)
                b6[b7][b10] = b11
    with open(b2, "w", b8 = 'utf-8') as b2:
        json.dump(b6, b2, b12 = False, indent=4)
fonk2("raw_data_file.txt", "swedish_words.json")