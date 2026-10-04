from binaryninja import *
def instruction_text_token_to_string(instruction_token_list):
    if not all(isinstance(token, function.InstructionTextToken) for token in instruction_token_list):
        raise TypeError("List must contain InstructionTextToken objects only.")
    return " ".join(token.text.strip() for token in instruction_token_list)
def process_immediate(immediate):
    if not isinstance(immediate, str):
        raise TypeError("Immediate must be a string object.")
    try:
        return int(immediate, 16) if immediate.startswith("0x") else int(immediate)
    except ValueError:
        raise ValueError(f"Invalid immediate value: {immediate}")
def lookup_immediate_instructions(bv, immediate):
    results = []
    for func in bv.functions:
        for instruction, address in func.instructions:
            if any(token.type == InstructionTextTokenType.PossibleAddressToken and token.value == immediate
                   for token in instruction):
                instruction_text = instruction_text_token_to_string(instruction)
                results.append((address, func.name, instruction_text))
    return results
def display_results_report(bv, value, results):
    html = """
    <!DOCTYPE html>
    <html>
        <body>
            <table border="1" cellpadding="5" cellspacing="0">
                <tr>
                    <th width="150">Address</th>
                    <th width="150">Function</th>
                    <th>Instruction</th>
                </tr>
                <tr>
                    <td><pre>0x{address:016X}</pre></td>
                    <td><pre>{function_name}</pre></td>
                    <td><pre>{instruction_text}</pre></td>
                </tr>
            </table>
        </body>
    </html>
    """
    bv.show_html_report(f"Search Immediate - 0x{value:X}", html)
def search_immediate(bv):
    immediate_str = get_text_line_input("Value to search", "Search Immediate")
    if immediate_str is None:
        return
    try:
        immediate = process_immediate(immediate_str)
    except ValueError as e:
        show_message_box("Error", str(e))
        return
    results = lookup_immediate_instructions(bv, immediate)
    if results:
        display_results_report(bv, immediate, results)
    else:
        show_message_box("Search Immediate", "No results found.")
PluginCommand.register(
    "Search Immediate",
    "Search for the specific value in the instruction operands.",
    search_immediate
)