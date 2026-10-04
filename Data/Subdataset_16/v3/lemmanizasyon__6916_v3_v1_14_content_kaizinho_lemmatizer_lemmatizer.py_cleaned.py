import re
import json
def fonk1(sentence, word_list):
    b1 = sentence.split()
    b2 = " ".join(word_list.get(b14, b14) for b14 in b1)
    return b2
def fonk2(raw_data_file, b3 = "swedish_words.json"):
    b4 = r"^(===(Verb|Substantiv|Adjektiv|Adverb|Konjuktion|Pronomen|RÃ¤kneord|Interjektion|Konjugation)===)$"
    b5 = r"^'''([a-zA-ZÃ¥Ã¤Ã¶Ã
ÃÃ]+)'''$"
    b6 = r"^'''([a-zA-ZÃ¥Ã¤Ã¶Ã
ÃÃ]+)''' \(([^)]+)\)$"
    b7 = {}
    b8 = None
    with open(raw_data_file, "r", b9 = 'utf-8') as input_file:
        for b10 in input_file:
            b10 = b10.strip()
            if not b10:
                continue
            b11 = re.match(b4, b10)
            b12 = re.match(b5, b10)
            b13 = re.match(b6, b10)
            if b11:
                b8 = b11.group(2)
                if b8 not in b7:
                    b7[b8] = {}
            elif b8 and b12:
                b14 = b12.group(1)
                b7[b8][b14] = ""
            elif b8 and b13:
                b14 = b13.group(1)
                b15 = b13.group(2)
                b7[b8][b14] = b15
    with open(b3, "w", b9 = 'utf-8') as b3:
        json.dump(b7, b3, b16 = False, indent=4)
if b17 = = "__main__":
    fonk2("raw_data_file.txt", "swedish_words.json")