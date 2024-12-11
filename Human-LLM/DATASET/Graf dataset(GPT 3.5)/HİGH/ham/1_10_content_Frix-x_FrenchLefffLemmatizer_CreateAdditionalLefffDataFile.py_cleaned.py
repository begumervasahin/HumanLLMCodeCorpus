import re
b1 = False
def fonk1(b2 = 1,carac='.',line_length=100):
    b3 = b2
    if b3 = = line_length:
        print(carac)
        return 1
    else:
        print( carac, b4 = '' )
        return b3 + 1
a1 = 0
a2 = 1
a3 = 2
a4 = 3
a5 = 4
def fonk2(a_key,dict_lefff):
    return dict_lefff[a_key][a1]
def fonk3(a_key,dict_lefff):
    return dict_lefff[a_key][a2]
def fonk4(a_key,dict_lefff):
    return dict_lefff[a_key][a3]
def fonk5(a_key,dict_lefff):
    return dict_lefff[a_key][a4]
def fonk6(a_key,dict_lefff):
    return dict_lefff[a_key][a5]
def fonk7(a_key,dict_lefff):
    return fonk4(a_key,dict_lefff)+"_v_"+fonk5(a_key,dict_lefff)
def fonk8(dict_key,dict_lefff):
    b5 = fonk3(dict_key,dict_lefff)
    if b1:
        print(b5)
    if not b5 = = 'adj':
        if b1:
            print('Should be an adj:',b5)
        return False
    else:
        b6 = fonk7(dict_key,dict_lefff)
        if b1:
            print(b6)
        if b6 in dict_lefff.keys():
            return (dict_lefff[b6][a3] == dict_lefff[dict_key][a3])
        else:
            if b1:
                print('Should be an infinitive verb:',b6)
            return False
def fonk9(dict_key,dict_lefff):
    b7 = fonk4(dict_key,dict_lefff)
    b8 = b7 + "_adj_Kms"
    if b8 in dict_lefff.keys():
        if b1:
            print('b8:',b8,'a1:',a1)
            print(dict_leff[b8])
        return dict_lefff[b8][a1]
    return "not found"
b9 = "/Users/claudecoulombe/git/semantron/notebooks/lefff-3.4.mlex/lefff-3.4.mlex"
b10 = ["-elle", "-elles", "-en", "-il", "-ils", "-je", "-la", "-le", "-les",\
                   "-leur", "-lui", "-m'", "-moi", "-nous", "-on", "-t'", "-t-elle", "-t-elles",\
                   "-t-en", "-t-il", "-t-ils", "-t-on", "-t-y", "-toi", "-tu", "-vous", "-vs",\
                   "-y", "_error", "ch'", "elle", "elles", "en", "il", "ils", "j'", "je", "l'",\
                   "l'on", "la", "le", "les", "leur", "lui", "m'", "me", "moi", "nous", "on",\
                   "s'", "se", "t'", "te", "toi", "tu", "vous", "vs", "y" ]
def fonk10(b9):
    b11 = {}
    a6 = 0
    b2 = 1
    with open(b9,b12 = 'r',encoding='utf-8') as input_file:
        for input_line in input_file:
            a6 += 1
            if a6 % b13 = = 0 :
                b2 = fonk1(b2)
            if ( re.search('^bÃ©e\t|^dÃ»\t|^dÃ»s\t|^due\t|^dues\t|^dus\t|^inf\.\.\t|^messis\t|^messise\t|^messises\t|^pu\t|^sup\.\.\t',input_line, b14 = 0) != None ):
                    pass
            else:
                b15 = re.split('\t',input_line[:-1])
                b16 = b15[a1]
                b17 = b15[a2]
                b18 = b15[a3]
                b19 = b15[a4]
                b20 = b15[a3]
                b21 = re.search('\tcla\t(cla)\t|\tclar\t(clar)\t|\tcld\t(cld)\t|\tcldr\t(cldr)\t|\tclg\t(clg)\t|\tcll\t(cll)\t|\tcln\t(cln)\t|\tclr\t(clr)\t|\tilimp\t(ilimp)\t|\tpro\t(pro)\t',input_line, b14=0)
                if ( b21 != None ):
                    b17 = [b21.group(i_group) for i_group in range(1,11) if not b21.group(i_group) == None ][0]
                    b20 = b17
                    if b1:
                        print(a6,'\t',input_line,'\t',b17)
                    if b17 in ['cla','clar']:
                        b18 = 'le'
                    elif b17 = = 'cld':
                        b18 = 'lui'
                    elif b17 = = 'clg':
                        b18 = 'en'
                    elif b17 = = 'cll':
                        b18 = 'y'
                    elif b17 in ['cln', 'ilimp']:
                        b18 = 'il'
                    elif b17 in ['clr', 'cldr']:
                        b18 = 'se'
                    else:
                        b18 = 'UNKNOWN'
                    b22 = b18 + '_' + b17 + '_' + b19 + b16
                else:
                    b22 = b18 + '_' + b17 + '_' + b19
                if b1 and (b17 = = "ilimp"):
                    print({b22:[b16,b17,b18,b19,b20]})
                if b1 and (b16 in b10):
                    print({b22:[b16,b17,b18,b19,b20]})
                b11.update({b22:[b16,b17,b18,b19,b20]})
    print()
    print( "Last line: ",a6,"\t",input_line )
    print( "End processing file: ", b9 )
    print( "Closing file: ", b9 )
    return b11
def fonk11(b11):
    b23 = {}
    a6 = 0
    b1 = False
    for dict_key,dict_value in b11.items():
        a6 += 1
        if b1 and (a6 % b24 = = 0):
            print(dict_key,fonk2(dict_key,b11),fonk3(dict_key,b11),dict_value)
        if fonk8(dict_key,b11):
            if b1 and (a6 % b24 = = 0):
                print("New dict entry:")
            b25 = fonk9(dict_key,b11)
            if b1 and (a6 % b24 = = 0):
                print("b25: ",b25)
            if not b25 = = "not found":
                if b1 and (a6 % b24 = = 0):
                    print("   ","dict_key: ",dict_key)
                b26 = fonk2(dict_key,b11)
                if b1 and (a6 % b24 = = 0):
                    print("   ","b16: ",b26)
                b27 = fonk3(dict_key,b11)
                if b1 and (a6 % b24 = = 0):
                    print("   ","POS: ",b27)
                    print("   ","b18: ",b25)
                b28 = fonk5(dict_key,b11)
                b20 = fonk6(dict_key,b11)
                if b1 and (a6 % b24 = = 0):
                    print("   ","b19: ",b28)
                    print("   ","b20: ",b20)
                b23.update({dict_key:[b26,b27,b25,b28,b20]})
        else:
            b26 = fonk2(dict_key,b11)
            b27 = fonk3(dict_key,b11)
            b25 = fonk4(dict_key,b11)
            b28 = fonk5(dict_key,b11)
            b20 = fonk6(dict_key,b11)
            if b1 and (a6 % b24 = = 0):
                print({dict_key:[b26,b27,b25,b28,b20]})
            b23.update({dict_key:[b26,b27,b25,b28,b20]})
    return b23
b29 = "/Users/claudecoulombe/git/semantron/notebooks/lefff-3.4.mlex/lefff-3.4-addition.mlex"
b30 = False
def fonk12(b11,b29):
    a6 = 0
    if b30:
        b29 = "/Users/claudecoulombe/git/semantron/notebooks/lefff-3.4.mlex/lefff-3.4-new.mlex"
    with open(b29,b12 = 'w',encoding='utf-8') as output_file:
        b2 = 1
        for dict_key,dict_value in b11.items():
            a6 += 1
            if a6 % b13 = = 0 :
                b2 = fonk1(b2)
            b16 = fonk2(dict_key,b11)
            b17 = fonk3(dict_key,b11)
            b18 = fonk4(dict_key,b11)
            b20 = fonk6(dict_key,b11)
            b19 = fonk5(dict_key,b11)
            if b30:
                output_file.write( b16 + "\t" + b17 + "\t" + b18 + "\t" + b19 + "\t" + b20 + '\n' )
            elif b17 in ['adj','cla','clar','cld','cldr','clg','cll','cln','clr','ilimp','pro']:
                output_file.write( b16 + "\t" + b17 + "\t" + b18 + "\t" + b19 + "\t" + b20 + '\n' )
        output_file.write( 'bÃ©e' + "\t" + 'adj' + "\t" + 'bÃ©e' + "\t" + 'Kfs' + "\t" + 'bÃ©er' + '\n')
        output_file.write( 'dÃ»' + "\t" + 'adj' + "\t" + 'dÃ»' + "\t" + 'Kms' + "\t" + 'devoir' + '\n')
        output_file.write( 'dÃ»s' + "\t" + 'adj' + "\t" + 'dÃ»' + "\t" + 'Kmp' + "\t" + 'devoir' + '\n')
        output_file.write( 'dus' + "\t" + 'adj' + "\t" + 'dÃ»' + "\t" + 'Kmp' + "\t" + 'devoir' + '\n')
        output_file.write( 'due' + "\t" + 'adj' + "\t" + 'dÃ»' + "\t" + 'Kfs' + "\t" + 'devoir' + '\n')
        output_file.write( 'dues' + "\t" + 'adj' + "\t" + 'dÃ»' + "\t" + 'Kfp' + "\t" + 'devoir' + '\n')
        output_file.write( 'messis' + "\t" + 'adj' + "\t" + 'messis' + "\t" + 'Km' + "\t" + 'messeoir' + '\n')
        output_file.write( 'messise' + "\t" + 'adj' + "\t" + 'messis' + "\t" + 'Kfs' + "\t" + 'messeoir' + '\n')
        output_file.write( 'messises' + "\t" + 'adj' + "\t" + 'messis' + "\t" + 'Kfp' + "\t" + 'messeoir' + '\n')
        output_file.write( 'pu' + "\t" + 'adj' + "\t" + 'pu' + "\t" + 'K' + "\t" + 'pouvoir' + '\n')
        output_file.write( 'au' + "\t" + 'det' + "\t" + 'ms' + "\t" + 'au' + "\t" + 'au' + '\n')
        output_file.write( 'aux' + "\t" + 'det' + "\t" + 'p' + "\t" + 'au' + "\t" + 'aux' + '\n')
    print()
    print( "Last line: ",a6 )
    print( "Closing file: ", b29)
def fonk13(b9,b29):
    b31 = fonk10(b9)
    b23 = fonk11(b31)
    fonk12(b23,b29)
print("Create LefffAdditionDatafile code ready!")