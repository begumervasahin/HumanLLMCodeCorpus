import re
import json
def fonk1(sentence, word_list):
    b1 = " ".join(word_list.get(b12, b12) for b12 in sentence.split())
    return b1.strip()
def fonk2(raw_data_file, b2 = "b6/swedish_words.json"):
    b3 = r"===(Verb|Substantiv|Adjektiv|Adverb|Konjuktion|Pronomen|Räkneord|Interjektion|Konjugation)==="
    b4 = r"'''([a-zA-ZåäöÅÄÖ]+)'''"
    b5 = r"'''([a-zA-ZåäöÅÄÖ]+)''' \(([^)]+)\)"
    b6 = {}
    b7 = None
    with open(raw_data_file, "r", b8 = 'utf-8') as input_file:
        for line in input_file:
            b9 = re.match(b3, line)
            b10 = re.match(b4, line)
            b11 = re.match(b5, line)
            if b9:
                b7 = b9.group(1)
            elif b10 and b7:
                b12 = b10.group(1)
                b6.setdefault(b7, {})[b12] = ""
            elif b11 and b7:
                b12 = b11.group(1)
                b13 = b11.group(2)
                b6.setdefault(b7, {})[b12] = b13
    with open(b2, "w", b8 = 'utf-8') as output_file:
        json.dump(b6, output_file, b14 = False, indent=4)
fonk2("raw_data_file.txt", "swedish_words.json")