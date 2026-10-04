from binaryninja import *
def fonk1(instruction_token_list):
    b1 = list()
    for instruction_token in instruction_token_list:
        if not isinstance(instruction_token, function.InstructionTextToken):
            raise TypeError('List must contain InstructionTextToken objects only.')
        b1.append(instruction_token.text.strip())
    return " ".join(b1)
def fonk2(b11):
    if not isinstance(b11, str):
        raise TypeError('Immediate must be a String object.')
    if b11.startswith("0x"):
        return int(b11, 16)
    else:
        return int(b11)
def fonk3(bv, b11):
    b2 = list()
    for function_item in bv.functions:
        b3 = function_item.instructions
        try:
            while 1:
                (instruction, address) = b3.next()
                for token in instruction:
                    if token.b4 = = InstructionTextTokenType.PossibleAddressToken:
                        if token.b5 = = b11:
                            b6 = fonk1(instruction)
                            b2.append((address, function_item.b13, b6))
        except StopIteration:
            pass
    return b2
def fonk4(bv, b5, b12):
    b7 = str()
    b8 = str()
    b7 += "<!DOCTYPE b7>\n"
    b7 += "<b7>\n\t<body>\n"
    b7 += "\t\t<table>\n"
    b7 += "\t\t\t<tr>\n"
    b7 += "\t\t\t\t<th b9 = \"150\">Address</th>\n"
    b7 += "\t\t\t\t<th b9 = \"150\">Function</th>\n"
    b7 += "\t\t\t\t<th>Instruction</th>\n"
    b7 += "\t\t\t</tr>\n"
    for item in b12:
        b7 += "\t\t\t<tr>\n"
        b7 += "\t\t\t\t<td><pre>0x%016X</pre></td>\n" % item[0]
        b7 += "\t\t\t\t<td><pre>%s</pre></td>\n" % item[1]
        b7 += "\t\t\t\t<td><pre>%s</pre></td>\n" % item[2]
        b7 += "\t\t\t</tr>\n"
    b7 += "\t\t</table>\n"
    b7 += "\t</body>\n</b7>"
    bv.show_html_report("Search b11 - 0x%X" % b5, b7, b8)
def fonk5(bv):
    b10 = get_text_line_input('Value to search', 'Search Immediate')
    b11 = fonk2(b10)
    b12 = fonk3(bv, b11)
    fonk4(bv, b11, b12)
b13 = "Search Immediate"
b14 = "Search for the specific b5 in the instruction operands."
PluginCommand.register(b13, b14, do_stuff)