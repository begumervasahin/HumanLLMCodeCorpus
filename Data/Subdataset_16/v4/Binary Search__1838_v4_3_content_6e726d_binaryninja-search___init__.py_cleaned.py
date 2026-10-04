from binaryninja import *
def fonk1(instruction_token_list):
    if not all(isinstance(token, function.InstructionTextToken) for token in instruction_token_list):
        raise TypeError("List must contain InstructionTextToken objects only.")
    return " ".join(token.text.strip() for token in instruction_token_list)
def fonk2(b8):
    if not isinstance(b8, str):
        raise TypeError("Immediate must be a string object.")
    if b8.startswith("0x"):
        return int(b8, 16)
    return int(b8)
def fonk3(bv, b8):
    b1 = []
    for function_item in bv.functions:
        b2 = function_item.instructions
        for instruction, address in b2:
            for token in instruction:
                if token.b3 = = InstructionTextTokenType.PossibleAddressToken and token.value == b8:
                    b4 = fonk1(instruction)
                    b1.append((address, function_item.name, b4))
    return b1
def fonk4(bv, value, b1):
    b5 = """
    <!DOCTYPE b5>
    <b5>
        <body>
            <table>
                <tr>
                    <th b6 = "150">Address</th>
                    <th b6 = "150">Function</th>
                    <th>Instruction</th>
                </tr>
                <tr>
                    <td><pre>0x{address:016X}</pre></td>
                    <td><pre>{function_name}</pre></td>
                    <td><pre>{b4}</pre></td>
                </tr>
            </table>
        </body>
    </b5>
    """
    bv.show_html_report(f"Search b8 - 0x{value:X}", b5)
def fonk5(bv):
    b7 = get_text_line_input("Value to search", "Search Immediate")
    b8 = fonk2(b7)
    b1 = fonk3(bv, b8)
    fonk4(bv, b8, b1)
PluginCommand.register("Search Immediate", "Search for the specific value in the instruction operands.", do_stuff)