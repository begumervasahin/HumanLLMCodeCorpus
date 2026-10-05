from binaryninja import *
def fonk1(instruction_token_list):
    b1 = []
    for instruction_token in instruction_token_list:
        if not isinstance(instruction_token, InstructionTextToken):
            raise TypeError('The list must contain InstructionTextToken objects only.')
        b1.append(instruction_token.text.strip())
    return " ".join(b1)
def fonk2(b8):
    if not isinstance(b8, str):
        raise TypeError('Immediate must be a string object.')
    if b8.startswith("0x"):
        return int(b8, 16)
    else:
        return int(b8)
def fonk3(bv, b8):
    b2 = []
    for function_item in bv.functions:
        for block in function_item:
            for instruction in block:
                for token in instruction:
                    if token.b3 = = InstructionTextTokenType.PossibleAddressToken and token.value == b8:
                        b4 = fonk1(instruction.tokens)
                        b2.append((block.start, function_item.b9, b4))
    return b2
def fonk4(bv, value, b2):
    b5 = "<!DOCTYPE b5>\n<b5>\n\t<body>\n"
    b5 += "\t\t<table>\n\t\t\t<tr>\n"
    b5 += "\t\t\t\t<th b6 = \"150\">Address</th>\n"
    b5 += "\t\t\t\t<th b6 = \"150\">Function</th>\n"
    b5 += "\t\t\t\t<th>Instruction</th>\n\t\t\t</tr>\n"
    for address, function_name, b4 in b2:
        b5 += "\t\t\t<tr>\n"
        b5 += f"\t\t\t\t<td><pre>0x{address:016X}</pre></td>\n"
        b5 += f"\t\t\t\t<td><pre>{function_name}</pre></td>\n"
        b5 += f"\t\t\t\t<td><pre>{b4}</pre></td>\n"
        b5 += "\t\t\t</tr>\n"
    b5 += "\t\t</table>\n\t</body>\n</b5>"
    bv.show_html_report(f"Search b8 - 0x{value:X}", b5)
def fonk5(bv):
    b7 = get_text_line_input('Value to search', 'Search Immediate')
    b8 = fonk2(b7)
    b2 = fonk3(bv, b8)
    fonk4(bv, b8, b2)
b9 = "Search Immediate"
b10 = "Search for a specific value in the instruction operands."
PluginCommand.register(b9, b10, do_stuff)