from binaryninja import *
def instruction_text_token_to_string(instruction_token_list):
    if not all(isinstance(token, function.InstructionTextToken) for token in instruction_token_list):
        raise TypeError("List must contain InstructionTextToken objects only.")
    return " ".join(token.text.strip() for token in instruction_token_list)
def process_immediate(immediate):
    if not isinstance(immediate, str):
        raise TypeError("Immediate must be a string object.")
    if immediate.startswith("0x"):
        return int(immediate, 16)
    return int(immediate)
def lookup_for_immediate(bv, immediate):
    results = []
    for function_item in bv.functions:
        function_instructions = function_item.instructions
        for instruction, address in function_instructions:
            for token in instruction:
                if token.type == InstructionTextTokenType.PossibleAddressToken and token.value == immediate:
                    instruction_text = instruction_text_token_to_string(instruction)
                    results.append((address, function_item.name, instruction_text))
    return results
def show_results_report(bv, value, results):
    html = """
    <!DOCTYPE html>
    <html>
        <body>
            <table>
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
    bv.show_html_report(f"Search immediate - 0x{value:X}", html)
def do_stuff(bv):
    immediate_str = get_text_line_input("Value to search", "Search Immediate")
    immediate = process_immediate(immediate_str)
    results = lookup_for_immediate(bv, immediate)
    show_results_report(bv, immediate, results)
PluginCommand.register("Search Immediate", "Search for the specific value in the instruction operands.", do_stuff)