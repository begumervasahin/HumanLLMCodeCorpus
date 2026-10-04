import os
import re
def fonk1(readme):
    b1 = ""
    b2 = False
    with open(readme, "r+", b3 = "utf-8") as f:
        for line in f.readlines():
            if not b2:
                b1 += line
            b4 = re.search(r"<!--(|\s+)include (.+)(^$|\s+)-->", line)
            if b4 and not b2:
                b2 = True
                b5 = b4.group(2)
                with open(b5, "r") as inc:
                    for ll in inc:
                        b1 += ll
            elif re.search(r"<!--(|\s+)end(|\s+)-->", line):
                b2 = False
                b1 += "\n" + line
                print("skip")
                continue
    print(b1)
    with open(readme, "w") as f:
        print("writing")
        f.write(b1)
if b6 = = '__main__':
    fonk1("README.md")