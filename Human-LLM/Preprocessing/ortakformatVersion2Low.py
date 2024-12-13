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

def remove_triple_quotes_comments(code):
    return re.sub(r'"""[^"]*"""', '', code, flags=re.DOTALL)

def remove_double_slash_comments(code):
    return re.sub(r'//.*', '', code)

def remove_extra_spaces_and_empty_lines(code):
    code = re.sub(r'[ \t]+$', '', code, flags=re.MULTILINE)
    code = re.sub(r'\n\s*\n', '\n', code)
    return code

def main():
    source_directory = "C:/Users/ervas/OneDrive/Masaüstü/ayrılmıs/ham"
    output_directory = 'C:/Users/ervas/OneDrive/Masaüstü/ayrılmıs/Ortakformat low/ham'
    file_counter = 1  # Sayaç başlangıcı
 
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in os.listdir(source_directory):
        if filename.endswith('.txt'):  # Process only .txt files
            file_path = os.path.join(source_directory, filename)

            with open(file_path, 'r', encoding='latin-1') as file:
                code = file.read()

            cleaned_code = remove_comments_from_file(code)
            cleaned_code = remove_triple_quotes_comments(cleaned_code)
            cleaned_code = remove_double_slash_comments(cleaned_code)
            compact_code = remove_extra_spaces_and_empty_lines(cleaned_code)

            # Sıra numarasını dosya adının başına ekleyerek kaydet
            output_file_path = os.path.join(output_directory, f"{file_counter}_{os.path.splitext(filename)[0]}_cleaned.py")
            file_counter += 1  # Sayaç artırımı

            with open(output_file_path, 'w', encoding='utf-8') as outfile:
                outfile.write(compact_code)

if __name__ == '__main__':
    main()
