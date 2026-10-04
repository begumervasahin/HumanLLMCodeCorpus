from binaryninja import *
def fonk1(instruction_token_list):
    if not all(isinstance(token, function.InstructionTextToken) for token in instruction_token_list):
        raise TypeError('List must contain InstructionTextToken objects only.')
    return " ".join(token.text.strip() for token in instruction_token_list)
def fonk2(b8):
    if not isinstance(b8, str):
        raise TypeError('Immediate must be a string object.')
    return int(b8, 16) if b8.startswith("0x") else int(b8)
def fonk3(bv, b8):
    b1 = []
    for function_item in bv.functions:
        b2 = function_item.instructions
        for address, instruction in b2:
            for token in instruction:
                if token.b3 = = InstructionTextTokenType.PossibleAddressToken and token.value == b8:
                    b4 = fonk1(instruction)
                    b1.append((address, function_item.b10, b4))
    return b1
def fonk4(bv, value, b9):
    b5 = [
        "<!DOCTYPE b5>",
        "<b5>",
        "<body>",
        "<table>",
        "<tr>",
        "<th b6 = \"150\">Address</th>",
        "<th b6 = \"150\">Function</th>",
        "<th>Instruction</th>",
        "</tr>"
    ]
    for address, function_name, b4 in b9:
        b5.append(f"<tr>")
        b5.append(f"<td><pre>0x{address:016X}</pre></td>")
        b5.append(f"<td><pre>{function_name}</pre></td>")
        b5.append(f"<td><pre>{b4}</pre></td>")
        b5.append(f"</tr>")
    b5.append("</table>")
    b5.append("</body>")
    b5.append("</b5>")
    bv.show_html_report(f"Search Immediate - 0x{value:X}", "\n".join(b5))
def fonk5(bv):
    b7 = get_text_line_input('Value to search', 'Search Immediate')
    if b7:
        b8 = fonk2(b7)
        b9 = fonk3(bv, b8)
        if b9:
            fonk4(bv, b8, b9)
        else:
            show_message_box("Search Immediate", "No b9 found.", MessageBoxButtonSet.OKButtonSet, MessageBoxIcon.InformationIcon)
b10 = "Search Immediate"
b11 = "Search for a specific b8 value in instruction operands."
PluginCommand.register(b10, b11, do_stuff)