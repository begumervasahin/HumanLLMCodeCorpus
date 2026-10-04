import re
def fonk1(readme_path):
    b1 = []
    b2 = False
    with open(readme_path, "r", b3 = "utf-8") as readme_file:
        b4 = readme_file.readlines()
    for line in b4:
        if not b2:
            b1.append(line)
        b5 = re.search(r"<!--\s*include\s+(.+?)\s*-->", line)
        if b5 and not b2:
            b2 = True
            b6 = b5.group(1).strip()
            with open(b6, "r", b3 = "utf-8") as include_file:
                b1.extend(include_file.readlines())
        b7 = re.search(r"<!--\s*end\s*-->", line)
        if b7:
            b2 = False
            b1.append("\n" + line)
    with open(readme_path, "w", b3 = "utf-8") as readme_file:
        readme_file.writelines(b1)
if b8 = = "__main__":
    fonk1("README.md")