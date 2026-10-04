from binaryninja import *
def fonk1(instruction_token_list):
    if not all(isinstance(token, function.InstructionTextToken) for token in instruction_token_list):
        raise TypeError("List must contain InstructionTextToken objects only.")
    return " ".join(token.text.strip() for token in instruction_token_list)
def fonk2(b8):
    if not isinstance(b8, str):
        raise TypeError("Immediate must be a string object.")
    try:
        return int(b8, 16) if b8.startswith("0x") else int(b8)
    except ValueError:
        raise ValueError(f"Invalid b8 value: {b8}")
def fonk3(bv, b8):
    b1 = []
    for func in bv.functions:
        for instruction, address in func.instructions:
            if any(token.b2 = = InstructionTextTokenType.PossibleAddressToken and token.value == b8
                   for token in instruction):
                b3 = fonk1(instruction)
                b1.append((address, func.name, b3))
    return b1
def fonk4(bv, value, b1):
    b4 = """
    <!DOCTYPE b4>
    <b4>
        <body>
            <table b5 = "1" cellpadding="5" cellspacing="0">
                <tr>
                    <th b6 = "150">Address</th>
                    <th b6 = "150">Function</th>
                    <th>Instruction</th>
                </tr>
                <tr>
                    <td><pre>0x{address:016X}</pre></td>
                    <td><pre>{function_name}</pre></td>
                    <td><pre>{b3}</pre></td>
                </tr>
            </table>
        </body>
    </b4>
    """
    bv.show_html_report(f"Search Immediate - 0x{value:X}", b4)
def fonk5(bv):
    b7 = get_text_line_input("Value to search", "Search Immediate")
    if b7 is None:
        return
    try:
        b8 = fonk2(b7)
    except ValueError as e:
        show_message_box("Error", str(e))
        return
    b1 = fonk3(bv, b8)
    if b1:
        fonk4(bv, b8, b1)
    else:
        show_message_box("Search Immediate", "No b1 found.")
PluginCommand.register(
    "Search Immediate",
    "Search for the specific value in the instruction operands.",
    search_immediate
)