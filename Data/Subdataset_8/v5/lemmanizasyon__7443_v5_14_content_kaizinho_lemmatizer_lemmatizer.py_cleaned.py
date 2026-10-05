import re
def lemmatize(sentence, word_list):
    lemm_sentence = ""
    for word in sentence.split():
        lemm_sentence += word_list.get(word, word) + " "
    return lemm_sentence.strip()
def extract_words(raw_data_file, filename="data/swedish_words.json"):
    heading_pattern = r"^(===(Verb|Substantiv|Adjektiv|Adverb|Konjuktion|Pronomen|RÃ¤kneord|Interjektion|Konjugation)===)$"
    bold_pattern = r"^'''([a-zA-ZÃ¥Ã¤Ã¶Ã
ÃÃ]+)'''$"
    line_pattern = r"^(.*?)$"
    data = ""
    current_heading = ""
    with open(raw_data_file, "r") as input_file, open(filename, "w") as output_file:
        output_file.write("{\n")
        for line in input_file:
            heading_match = re.search(heading_pattern, line)
            bold_match = re.search(bold_pattern, line)
            line_match = re.search(line_pattern, line)
            if heading_match:
                current_heading = heading_match.group(2)
            elif bold_match and current_heading:
                word = bold_match.group(1)
                data += f'\t"{current_heading}": "{word}",\n'
            elif line_match and current_heading:
                continue
        output_file.write(data.rstrip(',\n') + "\n}\n")