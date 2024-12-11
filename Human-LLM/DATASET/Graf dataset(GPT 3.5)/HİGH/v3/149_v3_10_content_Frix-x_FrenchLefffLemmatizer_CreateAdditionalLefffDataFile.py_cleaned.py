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
    b5 = fonk4(a_key, dict_lefff)
    b6 = fonk5(a_key, dict_lefff)
    return f"{b5}_v_{b6}"
def fonk8(dict_key, dict_lefff):
    b7 = fonk3(dict_key, dict_lefff)
    if b1:
        print(b7)
    if b7 != 'adj':
        if b1:
            print('Should be an adj:', b7)
        return False
    else:
        b8 = fonk7(dict_key, dict_lefff)
        if b1:
            print(b8)
        if b8 in dict_lefff:
            return dict_lefff[b8][a3] == dict_lefff[dict_key][a3]
        else:
            if b1:
                print('Should be an infinitive verb:', b8)
            return False
def fonk9(dict_key, dict_lefff):
    b9 = fonk4(dict_key, dict_lefff)
    b10 = f"{b9}_adj_Kms"
    if b10 in dict_lefff:
        return dict_lefff[b10][a1]
    return "not found"
def fonk10(input_file_path):
    b11 = {}
    a6 = 0
    b2 = 1
    with open(input_file_path, b12 = 'r', encoding='utf-8') as input_file:
        for input_line in input_file:
            a6 += 1
            if a6 % b13 = = 0:
                b2 = fonk1(b2)
            if re.search('^bÃ©e\t|^dÃ»\t|^dÃ»s\t|^due\t|^dues\t|^dus\t|^inf\.\.\t|^messis\t|^messise\t|^messises\t|^pu\t|^sup\.\.\t', input_line, b14 = 0) is not None:
                continue
            b15 = re.split('\t', input_line[:-1])
            b16 = b15[a1]
            b17 = b15[a2]
            b5 = b15[a3]
            b6 = b15[a4]
            b18 = b15[a3]
            b19 = re.search('\tcla\t(cla)\t|\tclar\t(clar)\t|\tcld\t(cld)\t|\tcldr\t(cldr)\t|\tclg\t(clg)\t|\tcll\t(cll)\t|\tcln\t(cln)\t|\tclr\t(clr)\t|\tilimp\t(ilimp)\t|\tpro\t(pro)\t', input_line, b14=0)
            if b19:
                b17 = [b19.group(i_group) for i_group in range(1, 11) if b19.group(i_group) is not None][0]
                b18 = b17
                if b1:
                    print(a6, '\t', input_line, '\t', b17)
                if b17 in ['cla', 'clar']:
                    b5 = 'le'
                elif b17 = = 'cld':
                    b5 = 'lui'
                elif b17 = = 'clg':
                    b5 = 'en'
                elif b17 = = 'cll':
                    b5 = 'y'
                elif b17 in ['cln', 'ilimp']:
                    b5 = 'il'
                elif b17 in ['clr', 'cldr']:
                    b5 = 'se'
                else:
                    b5 = 'UNKNOWN'
                b20 = f"{b5}_{b17}_{b6}{b16}"
            else:
                b20 = f"{b5}_{b17}_{b6}"
            if b1 and (b17 = = "ilimp"):
                print({b20: [b16, b17, b5, b6, b18]})
            if b1 and (b16 in clitic_pronouns):
                print({b20: [b16, b17, b5, b6, b18]})
            b11.update({b20: [b16, b17, b5, b6, b18]})
    print()
    print("Last line: ", a6, "\t", input_line)
    print("End processing file: ", input_file_path)
    print("Closing file: ", input_file_path)
    return b11
def fonk11(b11):
    b21 = {}
    a6 = 0
    b1 = False
    for dict_key, dict_value in b11.items():
        a6 += 1
        if b1 and (a6 % b22 = = 0):
            print(dict_key, fonk2(dict_key, b11),
                  fonk3(dict_key, b11), dict_value)
        if fonk8(dict_key, b11):
            if b1 and (a6 % b22 = = 0):
                print("New dict entry:")
            b23 = fonk9(dict_key, b11)
            if b1 and (a6 % b22 = = 0):
                print("b23: ", b23)
            if not b23 = = "not found":
                if b1 and (a6 % b22 = = 0):
                    print("   ", "dict_key: ", dict_key)
                b24 = fonk2(dict_key, b11)
                if b1 and (a6 % b22 = = 0):
                    print("   ", "b16: ", b24)
                b25 = fonk3(dict_key, b11)
                if b1 and (a6 % b22 = = 0):
                    print("   ", "POS: ", b25)
                    print("   ", "b5: ", b23)
                b26 = fonk5(dict_key, b11)
                b18 = fonk6(dict_key, b11)
                if b1 and (a6 % b22 = = 0):
                    print("   ", "b6: ", b26)
                    print("   ", "b18: ", b18)
                b21.update({dict_key: [b24, b25, b23, b26, b18]})
        else:
            b24 = fonk2(dict_key, b11)
            b25 = fonk3(dict_key, b11)
            b23 = fonk4(dict_key, b11)
            b26 = fonk5(dict_key, b11)
            b18 = fonk6(dict_key, b11)
            if b1 and (a6 % b22 = = 0):
                print({dict_key: [b24, b25, b23, b26, b18]})
            b21.update({dict_key: [b24, b25, b23, b26, b18]})
    return b21
def fonk12(b11, output_file_path):
    a6 = 0
    with open(output_file_path, b12 = 'w', encoding='utf-8') as output_file:
        b2 = 1
        for dict_key, dict_value in b11.items():
            a6 += 1
            if a6 % b13 = = 0:
                b2 = fonk1(b2)
            b16 = fonk2(dict_key, b11)
            b17 = fonk3(dict_key, b11)
            b5 = fonk4(dict_key, b11)
            b18 = fonk6(dict_key, b11)
            b6 = fonk5(dict_key, b11)
            output_file.write(
                f"{b16}\t{b17}\t{b5}\t{b6}\t{b18}\n")
    print()
    print("Last line: ", a6)
    print("Closing file: ", output_file_path)
def fonk13(input_file_path, output_file_path):
    b27 = fonk10(input_file_path)
    b21 = fonk11(b27)
    fonk12(b21, output_file_path)
print("Create LefffAdditionDatafile code ready!")