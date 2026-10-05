import re
b1 = False
a1 = 0
a2 = 1
a3 = 2
a4 = 3
a5 = 4
def fonk1(b2 = 1, carac='.', line_length=100):
    b3 = b2
    if b3 = = line_length:
        print(carac)
        return 1
    else:
        print(carac, b4 = '')
        return b3 + 1
def fonk2(a_key, dict_lefff):
    return dict_lefff[a_key][a1]
def fonk3(a_key, dict_lefff):
    return dict_lefff[a_key][a2]
def fonk4(a_key, dict_lefff):
    return dict_lefff[a_key][a3]
def fonk5(a_key, dict_lefff):
    return dict_lefff[a_key][a4]
def fonk6(a_key, dict_lefff):
    return dict_lefff[a_key][a5]
def fonk7(a_key, dict_lefff):
    return fonk4(a_key, dict_lefff) + "_v_" + fonk5(a_key, dict_lefff)
def fonk8(dict_key, dict_lefff):
    b5 = fonk3(dict_key, dict_lefff)
    if b1:
        print(b5)
    if not b5 = = 'adj':
        if b1:
            print('Should be an adj:', b5)
        return False
    else:
        b6 = fonk7(dict_key, dict_lefff)
        if b1:
            print(b6)
        if b6 in dict_lefff.keys():
            return (dict_lefff[b6][a3] == dict_lefff[dict_key][a3])
        else:
            if b1:
                print('Should be an infinitive verb:', b6)
            return False
def fonk9(dict_key, dict_lefff):
    b7 = fonk4(dict_key, dict_lefff)
    b8 = b7 + "_adj_Kms"
    if b8 in dict_lefff.keys():
        return dict_lefff[b8][a1]
    return "not found"
def fonk10(INPUT_FILE_PATH):
    b9 = {}
    a6 = 0
    b2 = 1
    with open(INPUT_FILE_PATH, b10 = 'r', encoding='utf-8') as input_file:
        for input_line in input_file:
            a6 += 1
            if a6 % b11 = = 0:
                b2 = fonk1(b2)
            if (re.search('^bÃ©e\t|^dÃ»\t|^dÃ»s\t|^due\t|^dues\t|^dus\t|^inf\.\.\t|^messis\t|^messise\t|^messises\t|^pu\t|^sup\.\.\t', input_line, b12 = 0) != None):
                pass
            else:
                b13 = re.split('\t', input_line[:-1])
                b14 = b13[a1]
                b15 = b13[a2]
                b16 = b13[a3]
                b17 = b13[a4]
                b18 = b13[a3]
                b19 = re.search('\tcla\t(cla)\t|\tclar\t(clar)\t|\tcld\t(cld)\t|\tcldr\t(cldr)\t|\tclg\t(clg)\t|\tcll\t(cll)\t|\tcln\t(cln)\t|\tclr\t(clr)\t|\tilimp\t(ilimp)\t|\tpro\t(pro)\t', input_line, b12=0)
                if (b19 != None):
                    b15 = [b19.group(i_group) for i_group in range(1, 11) if not b19.group(i_group) == None][0]
                    b18 = b15
                    if b1:
                        print(a6, '\t', input_line, '\t', b15)
                    if b15 in ['cla', 'clar']:
                        b16 = 'le'
                    elif b15 = = 'cld':
                        b16 = 'lui'
                    elif b15 = = 'clg':
                        b16 = 'en'
                    elif b15 = = 'cll':
                        b16 = 'y'
                    elif b15 in ['cln', 'ilimp']:
                        b16 = 'il'
                    elif b15 in ['clr', 'cldr']:
                        b16 = 'se'
                    else:
                        b16 = 'UNKNOWN'
                    b20 = b16 + '_' + b15 + '_' + b17 + b14
                else:
                    b20 = b16 + '_' + b15 + '_' + b17
                if b1 and (b15 = = "ilimp"):
                    print({b20: [b14, b15, b16, b17, b18]})
                if b1 and (b14 in clitic_pronouns):
                    print({b20: [b14, b15, b16, b17, b18]})
                b9.update({b20: [b14, b15, b16, b17, b18]})
    print()
    print("Last line: ", a6, "\t", input_line)
    print("End processing file: ", INPUT_FILE_PATH)
    print("Closing file: ", INPUT_FILE_PATH)
    return b9
def fonk11(b9):
    b21 = {}
    a6 = 0
    b1 = False
    for dict_key, dict_value in b9.items():
        a6 += 1
        if b1 and (a6 % b22 = = 0):
            print(dict_key, fonk2(dict_key, b9),
                  fonk3(dict_key, b9), dict_value)
        if fonk8(dict_key, b9):
            if b1 and (a6 % b22 = = 0):
                print("New dict entry:")
            b23 = fonk9(dict_key, b9)
            if b1 and (a6 % b22 = = 0):
                print("b23: ", b23)
            if not b23 = = "not found":
                if b1 and (a6 % b22 = = 0):
                    print("   ", "dict_key: ", dict_key)
                b24 = fonk2(dict_key, b9)
                if b1 and (a6 % b22 = = 0):
                    print("   ", "b14: ", b24)
                b25 = fonk3(dict_key, b9)
                if b1 and (a6 % b22 = = 0):
                    print("   ", "POS: ", b25)
                    print("   ", "b16: ", b23)
                b26 = fonk5(dict_key, b9)
                b18 = fonk6(dict_key, b9)
                if b1 and (a6 % b22 = = 0):
                    print("   ", "b17: ", b26)
                    print("   ", "b18: ", b18)
                b21.update({dict_key: [b24, b25, b23, b26, b18]})
        else:
            b24 = fonk2(dict_key, b9)
            b25 = fonk3(dict_key, b9)
            b23 = fonk4(dict_key, b9)
            b26 = fonk5(dict_key, b9)
            b18 = fonk6(dict_key, b9)
            if b1 and (a6 % b22 = = 0):
                print({dict_key: [b24, b25, b23, b26, b18]})
            b21.update({dict_key: [b24, b25, b23, b26, b18]})
    return b21
def fonk12(b9, OUTPUT_FILE_PATH):
    a6 = 0
    with open(OUTPUT_FILE_PATH, b10 = 'w', encoding='utf-8') as output_file:
        b2 = 1
        for dict_key, dict_value in b9.items():
            a6 += 1
            if a6 % b11 = = 0:
                b2 = fonk1(b2)
            b14 = fonk2(dict_key, b9)
            b15 = fonk3(dict_key, b9)
            b16 = fonk4(dict_key, b9)
            b18 = fonk6(dict_key, b9)
            b17 = fonk5(dict_key, b9)
            output_file.write(
                b14 + "\t" + b15 + "\t" + b16 + "\t" + b17 + "\t" + b18 + '\n')
    print()
    print("Last line: ", a6)
    print("Closing file: ", OUTPUT_FILE_PATH)
def fonk13(INPUT_FILE_PATH, OUTPUT_FILE_PATH):
    b27 = fonk10(INPUT_FILE_PATH)
    b21 = fonk11(b27)
    fonk12(b21, OUTPUT_FILE_PATH)
print("Create LefffAdditionDatafile code ready!")