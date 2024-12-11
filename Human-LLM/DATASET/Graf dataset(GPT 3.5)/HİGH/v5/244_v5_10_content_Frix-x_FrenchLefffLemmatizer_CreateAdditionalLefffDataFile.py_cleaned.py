import re
b1 = False
def fonk1(b2 = 1, carac='.', line_length=100):
    b3 = b2
    if b3 = = line_length:
        print(carac)
        return 1
    else:
        print(carac, b4 = '')
        return b3 + 1
def fonk2(a_key, dict_lefff):
    return dict_lefff[a_key][0]
def fonk3(a_key, dict_lefff):
    return dict_lefff[a_key][1]
def fonk4(a_key, dict_lefff):
    return dict_lefff[a_key][2]
def fonk5(a_key, dict_lefff):
    return dict_lefff[a_key][3]
def fonk6(a_key, dict_lefff):
    return dict_lefff[a_key][4]
def fonk7(a_key, dict_lefff):
    b5 = fonk4(a_key, dict_lefff)
    b6 = fonk5(a_key, dict_lefff)
    return f"{b5}_v_{b6}"
def fonk8(dict_key, dict_lefff):
    b7 = fonk3(dict_key, dict_lefff)
    if b7 != 'adj':
        return False
    b8 = fonk7(dict_key, dict_lefff)
    return b8 in dict_lefff and dict_lefff[b8][2] == dict_lefff[dict_key][2]
def fonk9(dict_key, dict_lefff):
    b9 = fonk4(dict_key, dict_lefff)
    b10 = f"{b9}_adj_Kms"
    return dict_lefff[b10][0] if b10 in dict_lefff else "not found"
b11 = "/Users/claudecoulombe/git/semantron/notebooks/lefff-3.4.mlex/lefff-3.4.mlex"
b12 = ["-elle", "-elles", "-en", "-il", "-ils", "-je", "-la", "-le", "-les", "-leur", "-lui", "-m'", "-moi",
                   "-nous", "-on", "-t'", "-t-elle", "-t-elles", "-t-en", "-t-il", "-t-ils", "-t-on", "-t-y", "-toi",
                   "-tu", "-vous", "-vs", "-y", "_error", "ch'", "elle", "elles", "en", "il", "ils", "j'", "je", "l'",
                   "l'on", "la", "le", "les", "leur", "lui", "m'", "me", "moi", "nous", "on", "s'", "se", "t'", "te",
                   "toi", "tu", "vous", "vs", "y"]
def fonk10(b11):
    b13 = {}
    a1 = 0
    b2 = 1
    with open(b11, b14 = 'r', encoding='utf-8') as input_file:
        for input_line in input_file:
            a1 += 1
            if a1 % b15 = = 0:
                b2 = fonk1(b2)
            if re.search('^bÃ©e\t|^dÃ»\t|^dÃ»s\t|^due\t|^dues\t|^dus\t|^inf\.\.\t|^messis\t|^messise\t|^messises\t|^pu\t|^sup\.\.\t', input_line, b16 = 0) is not None:
                continue
            b17 = re.split('\t', input_line[:-1])
            b18 = b17[0]
            b19 = b17[1]
            b5 = b17[2]
            b6 = b17[3]
            b20 = b17[2]
            b21 = re.search('\tcla\t(cla)\t|\tclar\t(clar)\t|\tcld\t(cld)\t|\tcldr\t(cldr)\t|\tclg\t(clg)\t|\tcll\t(cll)\t|\tcln\t(cln)\t|\tclr\t(clr)\t|\tilimp\t(ilimp)\t|\tpro\t(pro)\t', input_line, b16=0)
            if b21:
                b19 = [b21.group(i_group) for i_group in range(1, 11) if b21.group(i_group) is not None][0]
                b20 = b19
                if b1:
                    print(a1, '\t', input_line, '\t', b19)
                if b19 in ['cla', 'clar']:
                    b5 = 'le'
                elif b19 = = 'cld':
                    b5 = 'lui'
                elif b19 = = 'clg':
                    b5 = 'en'
                elif b19 = = 'cll':
                    b5 = 'y'
                elif b19 in ['cln', 'ilimp']:
                    b5 = 'il'
                elif b19 in ['clr', 'cldr']:
                    b5 = 'se'
                else:
                    b5 = 'UNKNOWN'
                b22 = f"{b5}_{b19}_{b6}{b18}"
            else:
                b22 = f"{b5}_{b19}_{b6}"
            b13[b22] = [b18, b19, b5, b6, b20]
    print()
    print("Last line: ", a1, "\t", input_line)
    print("End processing file: ", b11)
    print("Closing file: ", b11)
    return b13