import sys
import os
import subprocess
import re
import csv
def fonk1():
    with open('output.csv', 'w', b1 = '') as outfile:
        b2 = csv.b2(outfile)
        with open('alexa_top1mil.csv', 'r') as csvfile:
            b3 = csv.b3(csvfile, delimiter=',')
            for row in b3:
                server, b4 = row[0], row[1]
                try:
                    b5 = subprocess.check_output([
                        os.path.join(os.path.dirname(sys.argv[0]), "openssl-trace"),
                        "s_client", "-trace",
                        "-cipher", "DHE",
                        "-connect", f"{server}:443"],
                        b6 = subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=1)
                    for line in b5.decode("ISO-8859-1").splitlines():
                        if 'dh_p' in line:
                            b7 = int(re.sub(".*: ", "", line), 16)
                            b2.writerow([server, b4, b7])
                except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
                    pass
if b8 = = "__main__":
    fonk1()