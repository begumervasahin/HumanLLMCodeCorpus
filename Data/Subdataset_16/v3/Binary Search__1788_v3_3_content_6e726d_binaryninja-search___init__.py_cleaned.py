from binaryninja import *
def fonk1(tokens):
    if not all(isinstance(token, function.InstructionTextToken) for token in tokens):
        raise TypeError('List must contain InstructionTextToken objects only.')
    return " ".join(token.text.strip() for token in tokens)
def fonk2(b6):
    if not isinstance(b6, str):
        raise TypeError('Immediate must be a string object.')
    return int(b6, 16) if b6.startswith("0x") else int(b6)
def fonk3(bv, b7):
    b1 = []
    for func in bv.functions:
        for address, instruction in func.instructions:
            for token in instruction:
                if token.b2 = = InstructionTextTokenType.PossibleAddressToken and token.value == b7:
                    b3 = fonk1(instruction)
                    b1.append((address, func.name, b3))
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
    for address, func_name, instruction_text in b1:
        b4.extend([
            "<tr>",
            f"<td><pre>0x{address:016X}</pre></td>",
            f"<td><pre>{func_name}</pre></td>",
            f"<td><pre>{instruction_text}</pre></td>",
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
                show_message_box(
                    "Search Immediate",
                    "No b1 found.",
                    MessageBoxButtonSet.OKButtonSet,
                    MessageBoxIcon.InformationIcon
                )
        except ValueError:
            show_message_box(
                "Search Immediate",
                "Invalid immediate value format.",
                MessageBoxButtonSet.OKButtonSet,
                MessageBoxIcon.ErrorIcon
            )
PluginCommand.register(
    "Search Immediate",
    "Search for a specific immediate value in instruction operands.",
    prompt_and_search_immediate
)