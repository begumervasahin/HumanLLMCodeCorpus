import os
import re

def remove_comments_from_line(line):
    comment_start = line.find('#')
    if comment_start != -1:
        return line[:comment_start].rstrip() + '\n'
    else:
        return line

def remove_comments_from_file(file_content):
    lines = file_content.splitlines()
    new_lines = [remove_comments_from_line(line) for line in lines]
    return '\n'.join(new_lines)

def remove_double_slash_comments(code):
    return re.sub(r'//.*', '', code)

def is_numeric_value(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def rename_functions_in_code(code):
    function_pattern = re.compile(r'def (\w+)\(')
    function_index = 1
    function_mappings = {}

    def replace_function_name(match):
        nonlocal function_index
        original_name = match.group(1)
        new_name = f'fonk{function_index}'
        function_mappings[original_name] = new_name
        function_index += 1
        return f'def {new_name}('

    code = function_pattern.sub(replace_function_name, code)

    for original_name, new_name in function_mappings.items():
        call_pattern = re.compile(r'\b' + re.escape(original_name) + r'\(')
        code = call_pattern.sub(f'{new_name}(', code)

    return code

def rename_variables_in_code(code):
    variable_pattern = re.compile(r'\b(\w+)\s*=\s*(.*)')
    numeric_index, string_index = 1, 1
    replaced_variables = {}

    def replace_variable_name(match):
        nonlocal numeric_index, string_index
        variable_name, value = match.groups()
        if variable_name not in replaced_variables:
            if is_numeric_value(value.strip()):
                new_name = f'a{numeric_index}'
                numeric_index += 1
            else:
                new_name = f'b{string_index}'
                string_index += 1
            replaced_variables[variable_name] = new_name
            return f'{new_name} = {value}'
        else:
            return f'{replaced_variables[variable_name]} = {value}'

    new_code = variable_pattern.sub(replace_variable_name, code)

    for old_name, new_name in replaced_variables.items():
        usage_pattern = re.compile(r'\b' + re.escape(old_name) + r'\b')
        new_code = usage_pattern.sub(new_name, new_code)

    return new_code

def remove_extra_spaces_and_empty_lines(code):
    code = re.sub(r'[ \t]+$', '', code, flags=re.MULTILINE)
    code = re.sub(r'\n\s*\n', '\n', code)
    return code

def main():
    source_directory = 'kodlar'
    output_directory = 'cleaned_codes'
    file_counter = 1  # Sayaç başlangıcı

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in os.listdir(source_directory):
        if filename.endswith('.txt'):  # Process only .txt files
            file_path = os.path.join(source_directory, filename)

            with open(file_path, 'r', encoding='utf-8') as file:
                code = file.read()

            cleaned_code = remove_comments_from_file(code)
            cleaned_code = remove_double_slash_comments(cleaned_code)
            renamed_functions_code = rename_functions_in_code(cleaned_code)
            renamed_variables_code = rename_variables_in_code(renamed_functions_code)
            compact_code = remove_extra_spaces_and_empty_lines(renamed_variables_code)

            # Sıra numarasını dosya adının başına ekleyerek kaydet
            output_file_path = os.path.join(output_directory, f"{file_counter}_{os.path.splitext(filename)[0]}_cleaned.py")
            file_counter += 1  # Sayaç artırımı

            with open(output_file_path, 'w', encoding='utf-8') as outfile:
                outfile.write(compact_code)

if __name__ == '__main__':
    main()
