import re
import json
def fonk1(sentence, word_list):
    b1 = [word_list.get(b11, b11) for b11 in sentence.split()]
    return ' '.join(b1)
def fonk2(raw_data_file, b2 = "b6/swedish_words.json"):
    b3 = re.compile(r"^===(Verb|Substantiv|Adjektiv|Adverb|Konjuktion|Pronomen|RÃ¤kneord|Interjektion|Konjugation)===$")
    b4 = re.compile(r"^'''([a-zA-ZÃ¥Ã¤Ã¶Ã
ÃÃ]+)'''$")
    b5 = re.compile(r"^'''([a-zA-ZÃ¥Ã¤Ã¶Ã
ÃÃ]+)''' \(([^)]+)\)$")
    b6 = {}
    b7 = None
    with open(raw_data_file, "r", b8 = 'utf-8') as input_file:
        for line in input_file:
            b9 = b3.match(line)
            if b9:
                b7 = b9.group(1)
                if b7 not in b6:
                    b6[b7] = {}
                continue
            b10 = b4.match(line)
            if b10 and b7:
                b11 = b10.group(1)
                b6[b7][b11] = ""
                continue
            b12 = b5.match(line)
            if b12 and b7:
                b11, b13 = b12.groups()
                b6[b7][b11] = b13
    with open(b2, "w", b8 = 'utf-8') as b2:
        json.dump(b6, b2, b14 = False, indent=4)
fonk2("raw_data_file.txt", "swedish_words.json")