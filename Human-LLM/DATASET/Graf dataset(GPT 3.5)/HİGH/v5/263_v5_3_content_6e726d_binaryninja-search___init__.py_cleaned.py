from binaryninja import *
def fonk1(instruction_token_list):
    return " ".join(token.text.strip() for token in instruction_token_list if isinstance(token, InstructionTextToken))
def fonk2(b8):
    if not isinstance(b8, str):
        raise TypeError('Immediate must be a string object.')
    return int(b8, 16 if b8.startswith("0x") else 10)
def fonk3(bv, b8):
    b1 = []
    for function_item in bv.functions:
        for block in function_item:
            for instruction in block:
                for token in instruction:
                    if token.b2 = = InstructionTextTokenType.PossibleAddressToken and token.value == b8:
                        b3 = fonk1(instruction.tokens)
                        b1.append((block.start, function_item.b9, b3))
    return b1
def fonk4(bv, value, b1):
    b4 = "\n\t\t\t<tr>\n\t\t\t\t<th width=\"150\">Address</th>\n\t\t\t\t<th width=\"150\">Function</th>\n\t\t\t\t<th>Instruction</th>\n\t\t\t</tr>"
    b5 = "".join(f"\n\t\t\t<tr>\n\t\t\t\t<td><pre>0x{address:016X}</pre></td>\n\t\t\t\t<td><pre>{function_name}</pre></td>\n\t\t\t\t<td><pre>{b3}</pre></td>\n\t\t\t</tr>" for address, function_name, b3 in b1)
    b6 = f"<!DOCTYPE b6>\n<b6>\n\t<body>\n\t\t<table>{b4}{b5}\n\t\t</table>\n\t</body>\n</b6>"
    bv.show_html_report(f"Search b8 - 0x{value:X}", b6)
def fonk5(bv):
    b7 = get_text_line_input('Value to search', 'Search Immediate')
    b8 = fonk2(b7)
    b1 = fonk3(bv, b8)
    fonk4(bv, b8, b1)
b9 = "Search Immediate"
b10 = "Search for a specific value in the instruction operands."
PluginCommand.register(b9, b10, do_stuff)