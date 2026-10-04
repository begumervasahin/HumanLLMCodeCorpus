import re
def concat_files(readme):
    result_doc = ""
    matched = False
    with open(readme, "r", encoding="utf-8") as f:
        lines = f.readlines()
    for line in lines:
        if not matched:
            result_doc += line
        match = re.search(r"<!--\s*include\s+(.+?)\s*-->", line)
        if match and not matched:
            matched = True
            include_filename = match.group(1).strip()
            with open(include_filename, "r", encoding="utf-8") as inc_file:
                result_doc += inc_file.read()
        if re.search(r"<!--\s*end\s*-->", line):
            matched = False
            result_doc += "\n" + line
    with open(readme, "w", encoding="utf-8") as f:
        f.write(result_doc)
if __name__ == '__main__':
    concat_files("README.md")