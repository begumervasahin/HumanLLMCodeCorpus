
class InstructionTextToken:
    def __init__(self, text):
        self.text = text
class InstructionTextTokenType:
    PossibleAddressToken = 1
class BinaryView:
    def __init__(self, functions):
        self.functions = functions
    def show_html_report(self, title, html, plaintext):
        print("HTML Report Title:", title)
        print("HTML Report:", html)
        print("Plaintext Report:", plaintext)
class Function:
    def __init__(self, instructions, name):
        self.instructions = instructions
        self.name = name
class FunctionInstructions:
    def __init__(self, instructions):
        self.instructions = instructions
        self.idx = 0
    def next(self):
        if self.idx < len(self.instructions):
            inst = self.instructions[self.idx]
            self.idx += 1
            return inst
        else:
            raise StopIteration
def instruction_text_token_to_string(instruction_token_list):
    instructions = [token.text.strip() for token in instruction_token_list if isinstance(token, InstructionTextToken)]
    return " ".join(instructions)
def process_immediate(immediate):
    if not isinstance(immediate, str):
        raise TypeError('Immediate must be a string.')
    if immediate.startswith("0x"):
        return int(immediate, 16)
    else:
        return int(immediate)
def lookup_for_immediate(bv, immediate):
    results = []
    for function_item in bv.functions:
        function_instructions = FunctionInstructions(function_item.instructions)
        try:
            while True:
                (instruction, address) = function_instructions.next()
                for token in instruction:
                    if token.type == InstructionTextTokenType.PossibleAddressToken:
                        if token.value == immediate:
                            instruction_text = instruction_text_token_to_string(instruction)
                            results.append((address, function_item.name, instruction_text))
        except StopIteration:
            pass
    return results
def show_results_report(bv, value, results):
    html = "<!DOCTYPE html>\n<html>\n\t<body>\n\t\t<table>\n\t\t\t<tr>\n\t\t\t\t<th width=\"150\">Address</th>\n\t\t\t\t<th width=\"150\">Function</th>\n\t\t\t\t<th>Instruction</th>\n\t\t\t</tr>\n"
    for item in results:
        html += "\t\t\t<tr>\n"
        html += "\t\t\t\t<td><pre>0x%016X</pre></td>\n" % item[0]
        html += "\t\t\t\t<td><pre>%s</pre></td>\n" % item[1]
        html += "\t\t\t\t<td><pre>%s</pre></td>\n" % item[2]
        html += "\t\t\t</tr>\n"
    html += "\t\t</table>\n\t</body>\n</html>"
    bv.show_html_report("Search immediate - 0x%X" % value, html, "")
def do_stuff(bv):
    immediate_str = input('Value to search: ')
    immediate = process_immediate(immediate_str)
    results = lookup_for_immediate(bv, immediate)
    show_results_report(bv, immediate, results)
instruction_tokens = [InstructionTextToken("mov"), InstructionTextToken("[0x1234]")]
instructions = [(instruction_tokens, 0x1000)]
function = Function(instructions, "sample_function")
functions = [function]
binary_view = BinaryView(functions)
do_stuff(binary_view)