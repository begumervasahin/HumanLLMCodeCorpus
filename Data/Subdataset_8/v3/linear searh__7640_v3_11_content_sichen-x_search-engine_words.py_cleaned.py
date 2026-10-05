import os
import re
import string
def file_list(root):
    files = []
    for root_path, _, filenames in os.walk(root):
        for filename in filenames:
            files.append(os.path.join(root_path, filename))
    return files
def get_text(file_path):
    with open(file_path, 'r') as file:
        return file.read()
def tokenize(text):
    regex = re.compile('[' + re.escape(string.punctuation) + '0-9\\r\\t\\n]')
    text_without_punctuation = regex.sub(" ", text)
    words = text_without_punctuation.split(" ")
    words = [word.lower() for word in words if len(word) > 2]
    return words
def tokenize_advanced(text):
    words = []
    if len(text) < 3:
        return words
    regex_pattern_str = re.escape(string.punctuation)
    t = iter(regex_pattern_str)
    regex_pattern_str = '|'.join(a + b for a, b in zip(t, t))
    regex_pattern_str += '|[0-9]|\r|\t|\n|]'
    pattern = re.compile(regex_pattern_str)
    text_with_space = re.sub(pattern, ' ', text)
    words = text_with_space.split(' ')
    i = 0
    while i < len(words):
        words[i] = words[i].lower()
        if len(words[i]) < 3:
            words.pop(i)
        else:
            i += 1
    return words
def compile_relevant_content(file_path, terms):
    relevant_lines = set()
    with open(file_path, 'r') as file:
        for line in file:
            words_in_line = tokenize(line)
            for term in terms:
                if term in words_in_line:
                    relevant_lines.add(line)
                    if len(relevant_lines) == 2:
                        return relevant_lines
    return relevant_lines
def generate_html_content(file_paths, terms):
    if terms is None:
        terms_str = ' !!!nothing to be found!!! '
    else:
        terms_str = ' '.join(terms)
    if not file_paths:
        number_of_files = 0
    else:
        number_of_files = len(file_paths)
    html_content = '<html>\n<body>\n'
    html_h2 = f'<h2>Search results for <b>{terms_str}</b> in {number_of_files} files</h2>'
    html_content += html_h2
    html_content += '\n\n'
    if file_paths:
        section_counter = 0
        for file_path in file_paths:
            file_local_url = 'file:
            html_each_section = f'<p><a href="{file_local_url}">{file_path}</a><br>'
            relevant_lines = compile_relevant_content(file_path, terms)
            html_lines = ''
            for line in relevant_lines:
                html_lines += line + '<br>'
            html_each_section += html_lines
            html_each_section += '<br>\n\n'
            html_content += html_each_section
            section_counter += 1
            if section_counter >= 100:
                break
    html_content += '</body>\n</html>\n'
    return html_content
def extract_filenames(file_paths):
    return [os.path.basename(path) for path in file_paths]
if __name__ == '__main__':
    test_str_a = 'aaaa!bbbb"cccc             ",mmmm-nnnn.oooo/pppp:qqqq;rrrr<ssss=tttt>uuuu?vvvv@wwww' \
                 '[xxxx\yyyy]zzzz^AAAA_BBBB`CCCC{DDDD|EEEE}FF~GHH[]IJK{}LMNOPQRSTUVWXYZ'
    print(tokenize(test_str_a))
    print(tokenize_advanced(test_str_a))
    test_str_b =
    print(tokenize(test_str_b))
    print(tokenize_advanced(test_str_b))