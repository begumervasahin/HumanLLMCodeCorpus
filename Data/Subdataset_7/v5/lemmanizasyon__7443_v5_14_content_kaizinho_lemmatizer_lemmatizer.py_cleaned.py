import re
def fonk1(sentence, word_list):
    b1 = ""
    for b11 in sentence.split():
        b1 += word_list.get(b11, b11) + " "
    return b1.strip()
def fonk2(raw_data_file, b2 = "b6/swedish_words.json"):
    b3 = r"^(===(Verb|Substantiv|Adjektiv|Adverb|Konjuktion|Pronomen|RÃ¤kneord|Interjektion|Konjugation)===)$"
    b4 = r"^'''([a-zA-ZÃ¥Ã¤Ã¶Ã
ÃÃ]+)'''$"
    b5 = r"^(.*?)$"
    b6 = ""
    b7 = ""
    with open(raw_data_file, "r") as input_file, open(b2, "w") as output_file:
        output_file.write("{\n")
        for line in input_file:
            b8 = re.search(b3, line)
            b9 = re.search(b4, line)
            b10 = re.search(b5, line)
            if b8:
                b7 = b8.group(2)
            elif b9 and b7:
                b11 = b9.group(1)
                b6 += f'\t"{b7}": "{b11}",\n'
            elif b10 and b7:
                continue
        output_file.write(b6.rstrip(',\n') + "\n}\n")