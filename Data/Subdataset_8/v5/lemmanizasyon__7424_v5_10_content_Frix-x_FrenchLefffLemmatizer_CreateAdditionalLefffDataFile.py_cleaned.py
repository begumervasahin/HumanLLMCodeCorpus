import re
TRACE = False
def print_carac_on_the_same_line(index_output=1, carac='.', line_length=100):
    i = index_output
    if i == line_length:
        print(carac)
        return 1
    else:
        print(carac, end='')
        return i + 1
def extract_inflected_from_key(a_key, dict_lefff):
    return dict_lefff[a_key][0]
def extract_pos_from_key(a_key, dict_lefff):
    return dict_lefff[a_key][1]
def extract_lemma_from_key(a_key, dict_lefff):
    return dict_lefff[a_key][2]
def extract_misc_from_key(a_key, dict_lefff):
    return dict_lefff[a_key][3]
def extract_old_lemma_from_key(a_key, dict_lefff):
    return dict_lefff[a_key][4]
def create_verbal_key(a_key, dict_lefff):
    lemma = extract_lemma_from_key(a_key, dict_lefff)
    misc = extract_misc_from_key(a_key, dict_lefff)
    return f"{lemma}_v_{misc}"
def is_verb_inf_lemma_for_adj(dict_key, dict_lefff):
    current_pos = extract_pos_from_key(dict_key, dict_lefff)
    if current_pos != 'adj':
        return False
    verbal_key = create_verbal_key(dict_key, dict_lefff)
    return verbal_key in dict_lefff and dict_lefff[verbal_key][2] == dict_lefff[dict_key][2]
def find_lemma_adj_masc_sing(dict_key, dict_lefff):
    lemmatized_form = extract_lemma_from_key(dict_key, dict_lefff)
    new_key = f"{lemmatized_form}_adj_Kms"
    return dict_lefff[new_key][0] if new_key in dict_lefff else "not found"
INPUT_FILE_PATH = "/Users/claudecoulombe/git/semantron/notebooks/lefff-3.4.mlex/lefff-3.4.mlex"
clitic_pronouns = ["-elle", "-elles", "-en", "-il", "-ils", "-je", "-la", "-le", "-les", "-leur", "-lui", "-m'", "-moi",
                   "-nous", "-on", "-t'", "-t-elle", "-t-elles", "-t-en", "-t-il", "-t-ils", "-t-on", "-t-y", "-toi",
                   "-tu", "-vous", "-vs", "-y", "_error", "ch'", "elle", "elles", "en", "il", "ils", "j'", "je", "l'",
                   "l'on", "la", "le", "les", "leur", "lui", "m'", "me", "moi", "nous", "on", "s'", "se", "t'", "te",
                   "toi", "tu", "vous", "vs", "y"]
def load_lefff_dict(INPUT_FILE_PATH):
    additional_dict_lefff = {}
    line_number = 0
    index_output = 1
    with open(INPUT_FILE_PATH, mode='r', encoding='utf-8') as input_file:
        for input_line in input_file:
            line_number += 1
            if line_number % 1000 == 0:
                index_output = print_carac_on_the_same_line(index_output)
            if re.search('^bÃ©e\t|^dÃ»\t|^dÃ»s\t|^due\t|^dues\t|^dus\t|^inf\.\.\t|^messis\t|^messise\t|^messises\t|^pu\t|^sup\.\.\t', input_line, flags=0) is not None:
                continue
            line_data = re.split('\t', input_line[:-1])
            inflected_form = line_data[0]
            pos_tag = line_data[1]
            lemma = line_data[2]
            misc = line_data[3]
            old_lemma = line_data[2]
            clitic_pronoun_match = re.search('\tcla\t(cla)\t|\tclar\t(clar)\t|\tcld\t(cld)\t|\tcldr\t(cldr)\t|\tclg\t(clg)\t|\tcll\t(cll)\t|\tcln\t(cln)\t|\tclr\t(clr)\t|\tilimp\t(ilimp)\t|\tpro\t(pro)\t', input_line, flags=0)
            if clitic_pronoun_match:
                pos_tag = [clitic_pronoun_match.group(i_group) for i_group in range(1, 11) if clitic_pronoun_match.group(i_group) is not None][0]
                old_lemma = pos_tag
                if TRACE:
                    print(line_number, '\t', input_line, '\t', pos_tag)
                if pos_tag in ['cla', 'clar']:
                    lemma = 'le'
                elif pos_tag == 'cld':
                    lemma = 'lui'
                elif pos_tag == 'clg':
                    lemma = 'en'
                elif pos_tag == 'cll':
                    lemma = 'y'
                elif pos_tag in ['cln', 'ilimp']:
                    lemma = 'il'
                elif pos_tag in ['clr', 'cldr']:
                    lemma = 'se'
                else:
                    lemma = 'UNKNOWN'
                entry_key = f"{lemma}_{pos_tag}_{misc}{inflected_form}"
            else:
                entry_key = f"{lemma}_{pos_tag}_{misc}"
            additional_dict_lefff[entry_key] = [inflected_form, pos_tag, lemma, misc, old_lemma]
    print()
    print("Last line: ", line_number, "\t", input_line)
    print("End processing file: ", INPUT_FILE_PATH)
    print("Closing file: ", INPUT_FILE_PATH)
    return additional_dict_lefff