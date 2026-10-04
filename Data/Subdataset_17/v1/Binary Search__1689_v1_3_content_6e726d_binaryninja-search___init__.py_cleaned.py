from binaryninja import *
def instruction_text_token_to_string(instruction_token_list):
    if not all(isinstance(token, function.InstructionTextToken) for token in instruction_token_list):
        raise TypeError('List must contain InstructionTextToken objects only.')
    return " ".join(token.text.strip() for token in instruction_token_list)
def process_immediate(immediate):
    if not isinstance(immediate, str):
        raise TypeError('Immediate must be a string object.')
    return int(immediate, 16) if immediate.startswith("0x") else int(immediate)
def lookup_for_immediate(bv, immediate):
    result = []
    for function_item in bv.functions:
        function_instructions = function_item.instructions
        for address, instruction in function_instructions:
            for token in instruction:
                if token.type == InstructionTextTokenType.PossibleAddressToken and token.value == immediate:
                    instruction_text = instruction_text_token_to_string(instruction)
                    result.append((address, function_item.name, instruction_text))
    return result
def show_results_report(bv, value, results):
    html = [
        "<!DOCTYPE html>",
        "<html>",
        "<body>",
        "<table>",
        "<tr>",
        "<th width=\"150\">Address</th>",
        "<th width=\"150\">Function</th>",
        "<th>Instruction</th>",
        "</tr>"
    ]
    for address, function_name, instruction_text in results:
        html.append(f"<tr>")
        html.append(f"<td><pre>0x{address:016X}</pre></td>")
        html.append(f"<td><pre>{function_name}</pre></td>")
        html.append(f"<td><pre>{instruction_text}</pre></td>")
        html.append(f"</tr>")
    html.append("</table>")
    html.append("</body>")
    html.append("</html>")
    bv.show_html_report(f"Search Immediate - 0x{value:X}", "\n".join(html))
def do_stuff(bv):
    immediate_str = get_text_line_input('Value to search', 'Search Immediate')
    if immediate_str:
        immediate = process_immediate(immediate_str)
        results = lookup_for_immediate(bv, immediate)
        if results:
            show_results_report(bv, immediate, results)
        else:
            show_message_box("Search Immediate", "No results found.", MessageBoxButtonSet.OKButtonSet, MessageBoxIcon.InformationIcon)
name = "Search Immediate"
description = "Search for a specific immediate value in instruction operands."
PluginCommand.register(name, description, do_stuff)