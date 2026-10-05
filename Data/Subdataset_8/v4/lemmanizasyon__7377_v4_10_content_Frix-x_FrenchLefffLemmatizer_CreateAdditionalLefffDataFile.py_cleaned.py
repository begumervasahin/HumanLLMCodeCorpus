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
inflected_i = 0
pos_i = 1
lemma_i = 2
misc_i = 3
old_lemma_i = 4
def extract_inflected_from_key(a_key, dict_lefff):
    return dict_lefff[a_key][inflected_i]
def extract_pos_from_key(a_key, dict_lefff):
    return dict_lefff[a_key][pos_i]
def extract_lemma_from_key(a_key, dict_lefff):
    return dict_lefff[a_key][lemma_i]
def extract_misc_from_key(a_key, dict_lefff):
    return dict_lefff[a_key][misc_i]
def extract_old_lemma_from_key(a_key, dict_lefff):
    return dict_lefff[a_key][old_lemma_i]
def create_verbal_key(a_key, dict_lefff):
    return extract_lemma_from_key(a_key, dict_lefff) + "_v_" + extract_misc_from_key(a_key, dict_lefff)
def is_verb_inf_lemma_for_adj(dict_key, dict_lefff):
    current_pos = extract_pos_from_key(dict_key, dict_lefff)
    if TRACE:
        print(current_pos)
    if not current_pos == 'adj':
        if TRACE:
            print('Should be an adj:', current_pos)
        return False
    else:
        verbal_key = create_verbal_key(dict_key, dict_lefff)
        if TRACE:
            print(verbal_key)
        if verbal_key in dict_lefff.keys():
            return (dict_lefff[verbal_key][lemma_i] == dict_lefff[dict_key][lemma_i])
        else:
            if TRACE:
                print('Should be an infinitive verb:', verbal_key)
            return False
def find_lemma_adj_masc_sing(dict_key, dict_lefff):
    lemmatized_form = extract_lemma_from_key(dict_key, dict_lefff)
    new_key = lemmatized_form + "_adj_Kms"
    if new_key in dict_lefff.keys():
        if TRACE:
            print('new_key:', new_key, 'inflected_i:', inflected_i)
            print(dict_leff[new_key])
        return dict_lefff[new_key][inflected_i]
    return "not found"
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
                pass
            else:
                line_data = re.split('\t', input_line[:-1])
                inflected_form = line_data[inflected_i]
                pos_tag = line_data[pos_i]
                lemma = line_data[lemma_i]
                misc = line_data[misc_i]
                old_lemma = line_data[lemma_i]
                clitic_pronoun = re.search('\tcla\t(cla)\t|\tclar\t(clar)\t|\tcld\t(cld)\t|\tcldr\t(cldr)\t|\tclg\t(clg)\t|\tcll\t(cll)\t|\tcln\t(cln)\t|\tclr\t(clr)\t|\tilimp\t(ilimp)\t|\tpro\t(pro)\t', input_line, flags=0)
                if clitic_pronoun is not None:
                    pos_tag = [clitic_pronoun.group(i_group) for i_group in range(1, 11) if not clitic_pronoun.group(i_group) == None][0]
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
                    entry_key = lemma + '_' + pos_tag + '_' + misc + inflected_form
                else:
                    entry_key = lemma + '_' + pos_tag + '_' + misc
                if TRACE and (pos_tag == "ilimp"):
                    print({entry_key: [inflected_form, pos_tag, lemma, misc, old_lemma]})
                if TRACE and (inflected_form in clitic_pronouns):
                    print({entry_key: [inflected_form, pos_tag, lemma, misc, old_lemma]})
                additional_dict_lefff.update({entry_key: [inflected_form, pos_tag, lemma, misc, old_lemma]})
    print()
    print("Last line: ", line_number, "\t", input_line)
    print("End processing file: ", INPUT_FILE_PATH)
    print("Closing file: ", INPUT_FILE_PATH)
    return additional_dict_lefff
def transform_additional_lefff_dict(additional_dict_lefff):
    new_additional_dict_lefff = {}
    line_number = 0
    TRACE = False