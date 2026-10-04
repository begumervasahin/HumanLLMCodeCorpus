from binaryninja import *
def instruction_text_token_to_string(tokens):
    if not all(isinstance(token, function.InstructionTextToken) for token in tokens):
        raise TypeError('List must contain InstructionTextToken objects only.')
    return " ".join(token.text.strip() for token in tokens)
def process_immediate(immediate_str):
    if not isinstance(immediate_str, str):
        raise TypeError('Immediate must be a string object.')
    return int(immediate_str, 16) if immediate_str.startswith("0x") else int(immediate_str)
def search_for_immediate(bv, immediate_value):
    results = []
    for func in bv.functions:
        for address, instruction in func.instructions:
            for token in instruction:
                if token.type == InstructionTextTokenType.PossibleAddressToken and token.value == immediate_value:
                    instruction_str = instruction_text_token_to_string(instruction)
                    results.append((address, func.name, instruction_str))
    return results
def show_search_results(bv, value, results):
    html_content = [
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
    for address, func_name, instruction_text in results:
        html_content.extend([
            "<tr>",
            f"<td><pre>0x{address:016X}</pre></td>",
            f"<td><pre>{func_name}</pre></td>",
            f"<td><pre>{instruction_text}</pre></td>",
            "</tr>"
        ])
    html_content.extend(["</table>", "</body>", "</html>"])
    bv.show_html_report(f"Search Immediate - 0x{value:X}", "\n".join(html_content))
def prompt_and_search_immediate(bv):
    immediate_str = get_text_line_input('Value to search', 'Search Immediate')
    if immediate_str:
        try:
            immediate_value = process_immediate(immediate_str)
            results = search_for_immediate(bv, immediate_value)
            if results:
                show_search_results(bv, immediate_value, results)
            else:
                show_message_box(
                    "Search Immediate",
                    "No results found.",
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