from binaryninja import *
def instruction_text_token_to_string(instruction_token_list):
    instruction_str_list = []
    for instruction_token in instruction_token_list:
        if not isinstance(instruction_token, InstructionTextToken):
            raise TypeError('The list must contain InstructionTextToken objects only.')
        instruction_str_list.append(instruction_token.text.strip())
    return " ".join(instruction_str_list)
def process_immediate(immediate):
    if not isinstance(immediate, str):
        raise TypeError('Immediate must be a string object.')
    if immediate.startswith("0x"):
        return int(immediate, 16)
    else:
        return int(immediate)
def lookup_for_immediate(bv, immediate):
    results = []
    for function_item in bv.functions:
        for block in function_item:
            for instruction in block:
                for token in instruction:
                    if token.type == InstructionTextTokenType.PossibleAddressToken and token.value == immediate:
                        instruction_str = instruction_text_token_to_string(instruction.tokens)
                        results.append((block.start, function_item.name, instruction_str))
    return results
def show_results_report(bv, value, results):
    html = "<!DOCTYPE html>\n<html>\n\t<body>\n"
    html += "\t\t<table>\n\t\t\t<tr>\n"
    html += "\t\t\t\t<th width=\"150\">Address</th>\n"
    html += "\t\t\t\t<th width=\"150\">Function</th>\n"
    html += "\t\t\t\t<th>Instruction</th>\n\t\t\t</tr>\n"
    for address, function_name, instruction_str in results:
        html += "\t\t\t<tr>\n"
        html += f"\t\t\t\t<td><pre>0x{address:016X}</pre></td>\n"
        html += f"\t\t\t\t<td><pre>{function_name}</pre></td>\n"
        html += f"\t\t\t\t<td><pre>{instruction_str}</pre></td>\n"
        html += "\t\t\t</tr>\n"
    html += "\t\t</table>\n\t</body>\n</html>"
    bv.show_html_report(f"Search immediate - 0x{value:X}", html)
def do_stuff(bv):
    immediate_str = get_text_line_input('Value to search', 'Search Immediate')
    immediate = process_immediate(immediate_str)
    results = lookup_for_immediate(bv, immediate)
    show_results_report(bv, immediate, results)
name = "Search Immediate"
description = "Search for a specific value in the instruction operands."
PluginCommand.register(name, description, do_stuff)