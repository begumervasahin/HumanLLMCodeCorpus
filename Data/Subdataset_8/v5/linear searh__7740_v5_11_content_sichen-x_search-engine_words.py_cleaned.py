import os
import re
import string
def filelist(root):
    file_list = [os.path.join(dp, f) for dp, dn, filenames in os.walk(root) for f in filenames]
    return file_list
def get_text(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    return text
def extract_words(text):
    regex = re.compile('[' + re.escape(string.punctuation) + '0-9\\r\\t\\n]')
    text = regex.sub(" ", text)
    word_list = [word.lower() for word in text.split() if len(word) > 2]
    return word_list
def extract_words_v2(text):
    word_list = []
    if len(text) < 3:
        return word_list
    regex_pattern_str = re.escape(string.punctuation)
    t = iter(regex_pattern_str)
    regex_pattern_str = '|'.join(a+b for a, b in zip(t, t))
    regex_pattern_str += '|[0-9]|\r|\t|\n|]'
    pattern = re.compile(regex_pattern_str)
    text_with_space = re.sub(pattern, ' ', text)
    word_list = [word.lower() for word in text_with_space.split() if len(word) > 2]
    return word_list
def compile_relevant_content(file_path, terms):
    relevant_lines = set()
    with open(file_path, 'r') as file:
        for line in file:
            words_in_line = extract_words(line)
            for term in terms:
                if term in words_in_line:
                    relevant_lines.add(line)
                    if len(relevant_lines) == 2:
                        return relevant_lines
    return relevant_lines
def generate_html_results(file_paths, search_terms):
    if search_terms is None:
        search_terms_str = ' !!!nothing to be found!!! '
    else:
        search_terms_str = ' '.join(search_terms)
    if not file_paths:
        number_of_files = 0
    else:
        number_of_files = len(file_paths)
    html_content = '<html>\n<body>\n'
    html_h2 = f'<h2>Search results for <b>{search_terms_str}</b> in {number_of_files} files</h2>'
    html_content += html_h2 + '\n\n'
    if file_paths:
        section_counter = 0
        for file_path in file_paths:
            file_local_url = 'file:
            html_each_section = f'<p><a href="{file_local_url}">{file_path}</a><br>'
            lines = compile_relevant_content(file_path, search_terms)
            html_lines = '<br>'.join(lines)
            html_each_section += html_lines + '<br>\n\n'
            html_content += html_each_section
            section_counter += 1
            if section_counter >= 100:
                break
    html_content += '</body>\n</html>\n'
    return html_content
def extract_filenames(file_paths):
    if not file_paths:
        return []
    return [os.path.basename(path) for path in file_paths]
if __name__ == '__main__':
    test_str_a = 'aaaa!bbbb"cccc,mmmm-nnnn.oooo/pppp:qqqq;rrrr<ssss=tttt>uuuu?vvvv@wwww[xxxx\\yyyy]zzzz^AAAA_BBBB`CCCC{DDDD|EEEE}FF~GHH[]IJK{}LMNOPQRSTUVWXYZ'
    print(extract_words(test_str_a))
    print(extract_words_v2(test_str_a))
    test_str_b =
    print(extract_words(test_str_b))
    print(extract_words_v2(test_str_b))