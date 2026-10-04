import re
def fonk1(readme):
    b1 = ""
    b2 = False
    with open(readme, "r", b3 = "utf-8") as f:
        b4 = f.readlines()
    for line in b4:
        if not b2:
            b1 += line
        b5 = re.search(r"<!--\s*include\s+(.+?)\s*-->", line)
        if b5 and not b2:
            b2 = True
            b6 = b5.group(1).strip()
            with open(b6, "r", b3 = "utf-8") as inc_file:
                b1 += inc_file.read()
        if re.search(r"<!--\s*end\s*-->", line):
            b2 = False
            b1 += "\n" + line
    with open(readme, "w", b3 = "utf-8") as f:
        f.write(b1)
if b7 = = '__main__':
    fonk1("README.md")