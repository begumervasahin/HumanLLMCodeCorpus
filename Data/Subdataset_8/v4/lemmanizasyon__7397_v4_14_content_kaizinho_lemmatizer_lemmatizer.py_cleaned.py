import re
def lemmatize(sentence, word_list):
    lemm_sentence = ""
    for word in sentence.split():
        lemm_sentence += word_list.get(word, word) + " "
    return lemm_sentence.strip()
def extract_words(raw_data_file, filename="data/swedish_words.json"):
    pattern1 = r"^(===(Verb|Substantiv|Adjektiv|Adverb|Konjuktion|Pronomen|RÃ¤kneord|Interjektion|Konjugation)===)$"
    pattern2 = r"^'''([a-zA-ZÃ¥Ã¤Ã¶Ã
ÃÃ]+)'''$"
    pattern3 = r"^(.*?)$"
    data = ""
    matching_strings = []
    with open(raw_data_file, "r") as input_file:
        with open(filename, "w") as output_file:
            output_file.write("{\r\n")
            for line in input_file:
                match1 = re.search(pattern1, line)
                match2 = re.search(pattern2, line)
                match3 = re.search(pattern3, line)
                if len(matching_strings) == 0:
                    if match1:
                        matching_strings.append(match1.group())
                elif len(matching_strings) == 1:
                    if match2:
                        matching_strings.append(match2.group(1))
                    else:
                        matching_strings = []
                elif len(matching_strings) == 2:
                    if match3:
                        data += '\t"' + matching_strings[1] + '": "' + match3.group(1) + '",\r\n'
                    matching_strings = []
            output_file.write(data.rstrip(',\r\n'))
            output_file.write("\r\n}\r\n")
