import re
def fonk1(sentence, word_list):
    b1 = ""
    for word in sentence.split():
        b1 += word_list.get(word, word) + " "
    return b1.strip()
def fonk2(raw_data_file, b2 = "b6/swedish_words.json"):
    b3 = r"^(===(Verb|Substantiv|Adjektiv|Adverb|Konjuktion|Pronomen|RÃ¤kneord|Interjektion|Konjugation)===)$"
    b4 = r"^'''([a-zA-ZÃ¥Ã¤Ã¶Ã
ÃÃ]+)'''$"
    b5 = r"^(.*?)$"
    b6 = ""
    b7 = []
    with open(raw_data_file, "r") as input_file:
        with open(b2, "w") as output_file:
            output_file.write("{\r\n")
            for line in input_file:
                b8 = re.search(b3, line)
                b9 = re.search(b4, line)
                b10 = re.search(b5, line)
                if len(b7) == 0:
                    if b8:
                        b7.append(b8.group())
                elif len(b7) == 1:
                    if b9:
                        b7.append(b9.group(1))
                    else:
                        b7 = []
                elif len(b7) == 2:
                    if b10:
                        b6 += '\t"' + b7[1] + '": "' + b10.group(1) + '",\r\n'
                    b7 = []
            output_file.write(b6.rstrip(',\r\n'))
            output_file.write("\r\n}\r\n")
