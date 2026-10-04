from binaryninja import *
def fonk1(instruction_token_list):
    if not all(isinstance(token, function.InstructionTextToken) for token in instruction_token_list):
        raise TypeError('List must contain InstructionTextToken objects only.')
    return " ".join(token.text.strip() for token in instruction_token_list)
def fonk2(b7):
    if not isinstance(b7, str):
        raise TypeError('Immediate must be a string object.')
    return int(b7, 16) if b7.startswith("0x") else int(b7)
def fonk3(bv, b7):
    b1 = []
    for function_item in bv.functions:
        for address, instruction in function_item.instructions:
            for token in instruction:
                if token.b2 = = InstructionTextTokenType.PossibleAddressToken and token.value == b7:
                    b3 = fonk1(instruction)
                    b1.append((address, function_item.name, b3))
    return b1
def fonk4(bv, value, b1):
    b4 = [
        "<!DOCTYPE html>",
        "<html>",
        "<body>",
        "<table>",
        "<tr>",
        "<th b5 = \"150\">Address</th>",
        "<th b5 = \"150\">Function</th>",
        "<th>Instruction</th>",
        "</tr>"
    ]
    for address, function_name, b3 in b1:
        b4.extend([
            "<tr>",
            f"<td><pre>0x{address:016X}</pre></td>",
            f"<td><pre>{function_name}</pre></td>",
            f"<td><pre>{b3}</pre></td>",
            "</tr>"
        ])
    b4.extend(["</table>", "</body>", "</html>"])
    bv.show_html_report(f"Search Immediate - 0x{value:X}", "\n".join(b4))
def fonk5(bv):
    b6 = get_text_line_input('Value to search', 'Search Immediate')
    if b6:
        try:
            b7 = fonk2(b6)
            b1 = fonk3(bv, b7)
            if b1:
                fonk4(bv, b7, b1)
            else:
                show_message_box("Search Immediate", "No b1 found.",
                                 MessageBoxButtonSet.OKButtonSet,
                                 MessageBoxIcon.InformationIcon)
        except ValueError:
            show_message_box("Search Immediate", "Invalid b7 value format.",
                             MessageBoxButtonSet.OKButtonSet,
                             MessageBoxIcon.ErrorIcon)
PluginCommand.register(
    "Search Immediate",
    "Search for a specific b7 value in instruction operands.",
    do_stuff
)